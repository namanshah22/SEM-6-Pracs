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

# Define hiring and firing costs
hiring_cost = 1000  # Cost per hired candidate
firing_cost = 500   # Cost per fired candidate

# Calculate score for each candidate based on weightage
def calculate_score(candidate_id, candidate_data):
    return (cgpa_weightage * candidate_data['cgpa']) + (experience_weightage * candidate_data['experience']) + (rank_weightage / candidate_rankings[candidate_id])

# Hiring process
def hiring_process():
    selected_candidates = []
    for candidate_id, candidate_data in candidates.items():
        score = calculate_score(candidate_id, candidate_data)
        selected_candidates.append((candidate_id, score))
    selected_candidates.sort(key=lambda x: x[1], reverse=True)
    return selected_candidates[:len(candidates) // 3]  # Select top candidates for each role

# Firing process (replace the least qualified candidate with a new hire)
def firing_process(hired_candidates):
    least_qualified = min(hired_candidates, key=lambda x: x[1])
    hired_candidates.remove(least_qualified)
    return hired_candidates

# Interview sequence
def interview_sequence():
    sequence = []
    for _ in range(len(candidates) // 3):
        sequence.extend(['analyst', 'marketing', 'experience'])
    return sequence

# Main function
def main():
    # Interview sequence
    sequence = interview_sequence()
    
    # Hiring process
    hired_candidates = []
    for role in sequence:
        candidates_for_role = [(cid, cdata) for cid, cdata in candidates.items() if cdata['role'] == role]
        candidates_for_role.sort(key=lambda x: calculate_score(x[0], x[1]), reverse=True)
        hired_candidates.append(candidates_for_role[0])
    
    # Display hired candidates
    print("Hired Candidates:")
    for candidate_id, candidate_data in hired_candidates:
        print(f"Role: {candidate_data['role']}, CGPA: {candidate_data['cgpa']}, Experience: {candidate_data['experience']}")
    
    # Calculate hiring and firing costs
    hiring_costs = len(hired_candidates) * hiring_cost
    firing_costs = firing_cost * (len(candidates) // 3)
    
    print(f"\nTotal Hiring Cost: ${hiring_costs}")
    print(f"Total Firing Cost: ${firing_costs}")

# Execute main function
if __name__ == "__main__":
    main()

