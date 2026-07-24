#phase1
#phase 2 updated
#phase 4 updated
#phase 5 updated
#phase 6 updated(data generation)
# DATASET GENERATION IMPROVEMENT

# PHASE 7
# MACHINE LEARNING MODEL TRAINING
# DECISION TREE + RANDOM FOREST

#( PHASE 7.1
# DECISION TREE TRAINING
#Phase 7.2
#MODEL COMPARISON)

# main.py
# MAIN PROJECT FILE 

import joblib

from ml.train_decision_tree import train_decision_tree
from ml.train_random_forest import train_random_forest


print("========================================")
print(" AI CACHE PROJECT")
print(" PHASE 7 - MACHINE LEARNING")
print("========================================")


# ==========================================
# TRAIN DECISION TREE
# ==========================================

decision_tree_model, dt_accuracy = train_decision_tree()


# ==========================================
# TRAIN RANDOM FOREST
# ==========================================

random_forest_model, rf_accuracy = train_random_forest()


# ==========================================
# COMPARE MODELS
# ==========================================

print("\n========================================")
print(" MODEL COMPARISON")
print("========================================")

print(
    f"Decision Tree Accuracy : "
    f"{dt_accuracy * 100:.2f}%"
)

print(
    f"Random Forest Accuracy : "
    f"{rf_accuracy * 100:.2f}%"
)


# ==========================================
# SELECT BEST MODEL
# ==========================================

if rf_accuracy > dt_accuracy:

    best_model = random_forest_model
    best_model_name = "Random Forest"
    best_accuracy = rf_accuracy

else:

    best_model = decision_tree_model
    best_model_name = "Decision Tree"
    best_accuracy = dt_accuracy


# ==========================================
# SAVE BEST MODEL
# ==========================================

joblib.dump(
    best_model,
    "models/cache_model.pkl"
)


# ==========================================
# FINAL RESULT
# ==========================================

print("\n========================================")
print(" BEST MODEL")
print("========================================")

print("Selected Model :", best_model_name)

print(
    f"Accuracy : {best_accuracy * 100:.2f}%"
)

print("Saved As : models/cache_model.pkl")

print("\n========================================")
print(" PHASE 7 COMPLETED")
print("========================================")
