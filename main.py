#phase1
#phase 2 updated
#phase 4 updated
#phase 5 updated
#phase 6 updated(data generation)
# main.py
# MAIN PROJECT FILE 

from ml.dataset_generator import generate_dataset

print("==========================================")
print(" AI CACHE PROJECT - PHASE 6")
print(" DATASET GENERATION")
print("==========================================\n")

# Number of workloads to generate
samples = 300

# Cache size
cache_size = 5

# Generate Dataset
generate_dataset(samples=samples, cache_size=cache_size)

print("\n==========================================")
print("DATASET CREATED SUCCESSFULLY")
print("Location : datasets/dataset.csv")
print("==========================================")
    
