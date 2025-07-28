import pandas as pd
from sklearn.metrics import accuracy_score, f1_score, classification_report

df = pd.read_csv("climate_test_with_lst_assessed.csv")

df = df.dropna(subset=["Predicted Fallacy"])

y_true = df["logical_fallacies"].str.strip().tolist()
y_pred = df["Predicted Fallacy"].str.strip().tolist()

acc = accuracy_score(y_true, y_pred)
print(f"Accuracy: {acc:.3f}")

labels = [
    "ad hominem",
    "ad populum",
    "appeal to emotion",
    "circular reasoning",
    "deductive fallacy",
    "fallacy of credibility",
    "fallacy of extension",
    "fallacy of relevance",
    "false causality",
    "false dilemma",
    "faulty generalization",
    "intentional fallacy",
]

f1s = f1_score(y_true, y_pred, labels=labels, average=None, zero_division=0)
for lbl, f in zip(labels, f1s):
    print(f"{lbl:25s} F1 = {f:.3f}")

print("\nFull report:\n")
print(classification_report(
    y_true,
    y_pred,
    labels=labels,
    target_names=labels,
    zero_division=0
))
