import random

candidates = {
    1: {'cgpa': 9.5, 'experience': 1, 'role': 'analyst'},
    2: {'cgpa': 9.1, 'experience': 0, 'role': 'analyst'},
    3: {'cgpa': 9.8, 'experience': 2, 'role': 'analyst'},
    4: {'cgpa': 8.7, 'experience': 1, 'role': 'marketing'},
    5: {'cgpa': 7.9, 'experience': 1, 'role': 'marketing'},
    6: {'cgpa': 8.5, 'experience': 0, 'role': 'marketing'},
    7: {'cgpa': 7.6, 'experience': 3, 'role': 'experience'},
    8: {'cgpa': 6.9, 'experience': 2, 'role': 'experience'},
    9: {'cgpa': 6.8, 'experience': 0, 'role': 'experience'},
    10: {'cgpa': 5.5, 'experience': 1, 'role': 'analyst'},
    11: {'cgpa': 5.9, 'experience': 2, 'role': 'analyst'},
    12: {'cgpa': 6.2, 'experience': 0, 'role': 'analyst'},
    13: {'cgpa': 5.8, 'experience': 1, 'role': 'marketing'},
    14: {'cgpa': 6.1, 'experience': 0, 'role': 'marketing'},
    15: {'cgpa': 4.9, 'experience': 3, 'role': 'marketing'},
}

cgpa_weightage = 0.5
experience_weightage = 0.4
rank_weightage = 0.3

interviewed_candidates = []
hired_candidates = []

candidates_copy = candidates.copy()

for i in range(len(candidates)):
    selected_candidate = random.choice(list(candidates_copy.values()))
    interviewed_candidates.append(selected_candidate)
    del candidates_copy[list(candidates_copy.keys())[list(candidates_copy.values()).index(selected_candidate)]]

num_to_hire = random.randint(1, len(interviewed_candidates))

interviewed_candidates_copy = interviewed_candidates.copy()

for _ in range(num_to_hire):
    max_score = -1
    best_candidate = None

    for candidate in interviewed_candidates_copy:
        cgpa, experience, role = candidate['cgpa'], candidate['experience'], candidate['role']
        score = (rank_weightage * random.random()) + (experience_weightage * experience) + (cgpa_weightage * cgpa)
        
        if score > max_score:
            max_score = score
            best_candidate = candidate

    hired_candidates.append(best_candidate)
    interviewed_candidates_copy.remove(best_candidate)

firing_cost = len(hired_candidates) - 1

print("Interviewed candidates:")
for candidate in interviewed_candidates:
    print(f"CGPA: {candidate['cgpa']}, Experience: {candidate['experience']}, Role: {candidate['role']}")

print("\nHired candidates:")
for candidate in hired_candidates:
    print(f"CGPA: {candidate['cgpa']}, Experience: {candidate['experience']}, Role: {candidate['role']}")

print("\nNumber of candidates hired:", len(hired_candidates))
print("Firing cost:", firing_cost)
