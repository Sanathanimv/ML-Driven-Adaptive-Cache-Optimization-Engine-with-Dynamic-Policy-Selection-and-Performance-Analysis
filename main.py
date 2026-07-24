# ==========================================
# PHASE 6
# DATASET GENERATION IMPROVEMENT
# main.py
# ==========================================
# PHASE 7.1
# DECISION TREE TRAINING
# ==========================================
#Phase 7.2
#MODEL COMPARISON
# ==========================================
# PHASE 7
# MACHINE LEARNING MODEL TRAINING
# DECISION TREE + RANDOM FOREST
# ==========================================
# ==========================================
# PHASE 8
# MODEL EVALUATION
# ==========================================

from ml.evaluate_model import evaluate_model


print("========================================")
print(" AI CACHE PROJECT")
print(" PHASE 8 - MODEL EVALUATION")
print("========================================")


# Evaluate the best ML model
accuracy = evaluate_model()


print("\n========================================")
print(" PHASE 8 COMPLETED")
print(f" FINAL MODEL ACCURACY : {accuracy * 100:.2f}%")
print("========================================")
