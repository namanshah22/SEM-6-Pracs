import random
# Define attributes for 15 candidates
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

# Generate random rankings for each candidate
candidate_rankings = {i: random.randint(1, 15) for i in range(1, 16)}

# Define weightage for CGPA, experience, and rank
cgpa_weightage = 0.4
experience_weightage = 0.4
rank_weightage = 0.2

# Calculate score for each candidate based on weightage
def calculate_score(candidate):
    return (cgpa_weightage * candidate['cgpa']) + (experience_weightage * candidate['experience']) + (rank_weightage / candidate_rankings[candidate_id])

# Interview candidates for the analyst role first
selected_analyst = []
used_ranks = set()  # To keep track of used ranks
for candidate_id, candidate_data in candidates.items():
    if len(selected_analyst) < len(candidates) // 3 and candidate_data['role'] == 'analyst':
        rank = candidate_rankings[candidate_id]
        while rank in used_ranks:  # Ensure rank is not repeated
            rank = random.randint(1, 15)
        selected_analyst.append((candidate_id, candidate_data, calculate_score(candidate_data)))
        used_ranks.add(rank)

# Sort selected analyst candidates based on their scores
selected_analyst.sort(key=lambda x: x[2], reverse=True)

# Display selected candidates for the analyst role
print("Selected candidates for Analyst role:")
for candidate_id, candidate_data, score in selected_analyst:
    print(f"Candidate: {candidate_id}, CGPA: {candidate_data['cgpa']}, Experience: {candidate_data['experience']}, Rank: {candidate_rankings[candidate_id]}, Score: {score}")

# Filter out selected analyst candidates
selected_candidates = [candidate for candidate in candidates.items() if candidate[0] not in [c[0] for c in selected_analyst]]

# Interview candidates for other roles
selected_marketing = [candidate for candidate in selected_candidates if candidate[1]['role'] == 'marketing'][:len(candidates) // 3]
selected_experience = [candidate for candidate in selected_candidates if candidate[1]['role'] == 'experience'][:len(candidates) // 3]

# Display selected candidates for other roles
print("\nSelected candidates for Marketing role:")
for candidate_id, candidate_data in selected_marketing:
    print(f"Candidate: {candidate_id}, CGPA: {candidate_data['cgpa']}, Experience: {candidate_data['experience']}, Rank: {candidate_rankings[candidate_id]}")

print("\nSelected candidates for Experience role:")
for candidate_id, candidate_data in selected_experience:
    print(f"Candidate: {candidate_id}, CGPA: {candidate_data['cgpa']}, Experience: {candidate_data['experience']}, Rank: {candidate_rankings[candidate_id]}")