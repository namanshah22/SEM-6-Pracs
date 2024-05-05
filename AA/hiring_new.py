candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates: ", candidates)
interviewed_candidates = []
hired_candidates = []
# Interview candidates in order
for candidate in candidates:
    interviewed_candidates.append(candidate)
    # Hire the best candidate so far
    if not hired_candidates or candidate > max(hired_candidates):
        hired_candidates.append(candidate)
# Calculate firing cost
firing_cost = len(hired_candidates) - 1  # Since the last candidate is the best
print("Normal way : ")
print("Interviewed candidates:", interviewed_candidates)
print("Hired candidates:", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)
import random

candidates = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Candidates: ", candidates)
interviewed_candidates = []
hired_candidates = []
print("\nRandomized Approach")
# Randomly select and interview candidates
for i in range(len(candidates)):
    selected_candidate = random.choice(candidates)
    interviewed_candidates.append(selected_candidate)
    candidates.remove(selected_candidate)
# Hire the best candidate so far
max = -1
for i in range(len(interviewed_candidates)):
    if interviewed_candidates[i] > max:
        max = interviewed_candidates[i]
        hired_candidates.append(interviewed_candidates[i])
# Calculate firing cost
firing_cost = len(hired_candidates) - 1  # Since the last candidate is the best
print("Interviewed candidates in randomized order:", interviewed_candidates)
print("Hired candidates:", hired_candidates)
print("Number of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)