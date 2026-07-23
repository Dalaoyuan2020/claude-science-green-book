# -*- coding: utf-8 -*-
"""
SVM 乳腺癌良恶性分类 — 完整可复现脚本
数据集：威斯康星乳腺癌诊断数据集（sklearn.datasets.load_breast_cancer）
目标：以恶性召回率为首要优化目标，对比四种核函数
依赖：scikit-learn, numpy, pandas, matplotlib, seaborn
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    classification_report, confusion_matrix, ConfusionMatrixDisplay,
    roc_curve, auc, recall_score, make_scorer, roc_auc_score,
    precision_score, f1_score, accuracy_score
)
from sklearn.inspection import permutation_importance
from sklearn.decomposition import PCA

# ------------------------------------------------------------------
# 0. 全局配置
# ------------------------------------------------------------------
RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)
sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 150

# 加载数据： malignant=0 作为正类（我们关注漏诊）
data = load_breast_cancer()
X, y = data.data, 1 - data.target  # 0=恶性，1=良性
feature_names = data.feature_names

print(f"样本数: {X.shape[0]}, 特征数: {X.shape[1]}")
print(f"恶性(0): {np.sum(y==0)}, 良性(1): {np.sum(y==1)}")

# ------------------------------------------------------------------
# 1. 数据划分与标准化
# ------------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=RANDOM_STATE
)

scaler = StandardScaler().fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)

print(f"训练集: {X_train_s.shape[0]}, 测试集: {X_test_s.shape[0]}")

# ------------------------------------------------------------------
# 2. 四种核函数独立调优（关键：显式指定 kernel，避免标签错配）
# ------------------------------------------------------------------
scorer = make_scorer(recall_score, pos_label=0)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)

kernels = {
    "Linear": {
        "kernel": ["linear"],
        "C": [0.01, 0.1, 1, 10, 100],
    },
    "RBF": {
        "kernel": ["rbf"],
        "C": [0.1, 1, 10, 100],
        "gamma": ["scale", "auto", 0.001, 0.01, 0.1],
    },
    "Poly-3": {
        "kernel": ["poly"],
        "degree": [3],
        "C": [0.1, 1, 10, 100],
        "gamma": ["scale", "auto", 0.001, 0.01, 0.1],
    },
    "Sigmoid": {
        "kernel": ["sigmoid"],
        "C": [0.1, 1, 10, 100],
        "gamma": ["scale", "auto", 0.001, 0.01, 0.1],
    },
}

results = {}
for name, param_grid in kernels.items():
    print(f"\n正在调优: {name} ...")
    grid = GridSearchCV(
        SVC(class_weight="balanced", probability=True, random_state=RANDOM_STATE),
        param_grid=param_grid,
        scoring=scorer,
        cv=cv,
        n_jobs=-1,
    )
    grid.fit(X_train_s, y_train)
    results[name] = {
        "model": grid.best_estimator_,
        "params": grid.best_params_,
        "cv_recall": grid.best_score_,
    }
    print(f"  最优参数: {grid.best_params_}")
    print(f"  CV 恶性召回率: {grid.best_score_:.4f}")

# ------------------------------------------------------------------
# 3. 测试集评估
# ------------------------------------------------------------------
metrics = []
for name, res in results.items():
    model = res["model"]
    y_pred = model.predict(X_test_s)
    y_prob = model.predict_proba(X_test_s)[:, 0]  # 恶性类的概率

    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

    metrics.append({
        "核函数": name,
        "准确率": accuracy_score(y_test, y_pred),
        "精确率": precision_score(y_test, y_pred, pos_label=0),
        "召回率(恶性)": recall_score(y_test, y_pred, pos_label=0),
        "F1": f1_score(y_test, y_pred, pos_label=0),
        "ROC-AUC": roc_auc_score(y_test, y_prob),
        "TP": tp,
        "FN": fn,
        "FP": fp,
        "TN": tn,
    })

df_metrics = pd.DataFrame(metrics)
print("\n测试集结果:")
print(df_metrics.to_string(index=False))

# ------------------------------------------------------------------
# 4. 可视化：混淆矩阵 + ROC 曲线
# ------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 混淆矩阵：以 RBF 为例（召回率最高）
best_name = df_metrics.loc[df_metrics["召回率(恶性)"].idxmax(), "核函数"]
best_model = results[best_name]["model"]
ConfusionMatrixDisplay.from_estimator(
    best_model, X_test_s, y_test,
    display_labels=["恶性", "良性"],
    cmap="Blues", ax=axes[0]
)
axes[0].set_title(f"Confusion Matrix — {best_name} SVM")

# ROC 曲线
for name, res in results.items():
    model = res["model"]
    y_prob = model.predict_proba(X_test_s)[:, 0]
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    axes[1].plot(fpr, tpr, label=f"{name} (AUC={roc_auc:.3f})")

axes[1].plot([0, 1], [0, 1], "k--", lw=1)
axes[1].set_xlabel("False Positive Rate")
axes[1].set_ylabel("True Positive Rate")
axes[1].set_title("ROC Curves — Four Kernels")
axes[1].legend(loc="lower right")

plt.tight_layout()
plt.savefig("model_evaluation.png", dpi=150, bbox_inches="tight")
print("\n已保存: model_evaluation.png")

# ------------------------------------------------------------------
# 5. 特征重要性
# ------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Linear SVM 权重绝对值
linear_model = results["Linear"]["model"]
weights = np.abs(linear_model.coef_[0])
idx = np.argsort(weights)[::-1][:10]
axes[0].barh(range(10), weights[idx], color="#147A52")
axes[0].set_yticks(range(10))
axes[0].set_yticklabels([feature_names[i] for i in idx])
axes[0].invert_yaxis()
axes[0].set_xlabel("|w|")
axes[0].set_title("Linear SVM Feature Weights (Top 10)")

# RBF 置换重要性
perm = permutation_importance(
    best_model, X_test_s, y_test,
    scoring=scorer, n_repeats=30, random_state=RANDOM_STATE, n_jobs=-1
)
idx_perm = np.argsort(perm.importances_mean)[::-1][:10]
axes[1].barh(
    range(10),
    perm.importances_mean[idx_perm],
    xerr=perm.importances_std[idx_perm],
    color="#c9a24b"
)
axes[1].set_yticks(range(10))
axes[1].set_yticklabels([feature_names[i] for i in idx_perm])
axes[1].invert_yaxis()
axes[1].set_xlabel("Permutation Importance (Δ recall)")
axes[1].set_title(f"Permutation Importance — {best_name} SVM")

plt.tight_layout()
plt.savefig("feature_importance.png", dpi=150, bbox_inches="tight")
print("已保存: feature_importance.png")

# ------------------------------------------------------------------
# 6. PCA 投影 + 决策边界（Linear）
# ------------------------------------------------------------------
pca = PCA(n_components=2, random_state=RANDOM_STATE)
X_train_pca = pca.fit_transform(X_train_s)
X_test_pca = pca.transform(X_test_s)

# 在 PCA 空间训练一个 Linear SVM 用于可视化边界
svm_pca = SVC(kernel="linear", C=1, class_weight="balanced", random_state=RANDOM_STATE)
svm_pca.fit(X_train_pca, y_train)

xx, yy = np.meshgrid(
    np.linspace(X_test_pca[:, 0].min() - 1, X_test_pca[:, 0].max() + 1, 200),
    np.linspace(X_test_pca[:, 1].min() - 1, X_test_pca[:, 1].max() + 1, 200),
)
Z = svm_pca.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(9, 7))
plt.contourf(xx, yy, Z, levels=[-1, 0, 1], alpha=0.2, colors=["#147A52", "#c9a24b", "#147A52"])
plt.contour(xx, yy, Z, levels=[-1, 0, 1], colors="k", linestyles=["--", "-", "--"], linewidths=1)
plt.scatter(X_test_pca[y_test == 0, 0], X_test_pca[y_test == 0, 1],
            c="#c9a24b", label="恶性", edgecolors="k", s=50)
plt.scatter(X_test_pca[y_test == 1, 0], X_test_pca[y_test == 1, 1],
            c="#147A52", label="良性", edgecolors="k", s=50)
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)")
plt.title("PCA Projection with Linear SVM Decision Boundary")
plt.legend()
plt.tight_layout()
plt.savefig("pca_boundary.png", dpi=150, bbox_inches="tight")
print("已保存: pca_boundary.png")

# ------------------------------------------------------------------
# 7. EDA 图表
# ------------------------------------------------------------------
fig, axes = plt.subplots(2, 3, figsize=(14, 9))
axes = axes.ravel()

plot_features = ["mean area", "mean concavity", "mean texture",
                 "worst area", "worst concavity", "worst texture"]
for i, feat in enumerate(plot_features):
    idx = list(feature_names).index(feat)
    sns.histplot(X[y == 0, idx], color="#c9a24b", kde=True, label="恶性", ax=axes[i], alpha=0.6)
    sns.histplot(X[y == 1, idx], color="#147A52", kde=True, label="良性", ax=axes[i], alpha=0.6)
    axes[i].set_title(feat)
    axes[i].legend()

plt.suptitle("Feature Distributions by Diagnosis", y=1.02)
plt.tight_layout()
plt.savefig("eda_distribution.png", dpi=150, bbox_inches="tight")
print("已保存: eda_distribution.png")

# 相关热力图（mean 组）
mean_cols = [i for i, n in enumerate(feature_names) if n.startswith("mean ")]
mean_names = [feature_names[i] for i in mean_cols]
mean_df = pd.DataFrame(X[:, mean_cols], columns=mean_names)

plt.figure(figsize=(10, 8))
sns.heatmap(mean_df.corr(), annot=True, fmt=".2f", cmap="RdBu_r", center=0,
            square=True, cbar_kws={"shrink": 0.8})
plt.title("Pearson Correlation — Mean Feature Group")
plt.tight_layout()
plt.savefig("eda_correlation.png", dpi=150, bbox_inches="tight")
print("已保存: eda_correlation.png")

print("\n全部完成。核心结果:")
print(df_metrics[["核函数", "准确率", "召回率(恶性)", "F1", "ROC-AUC"]].to_string(index=False))
