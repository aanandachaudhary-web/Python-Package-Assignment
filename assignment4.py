from tqdm import tqdm
import time

for i in tqdm(range(20), desc="Completing study tasks"):
    time.sleep(0.1)

print("All 20 study tasks completed!")