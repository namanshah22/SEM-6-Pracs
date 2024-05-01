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

def hire_assistant_randomized(n):
    # Generating random list of interview scores
    interview_scores = [random.random() for _ in range(n)]
    best_score = 0
    hired = None

    # Shuffling the list of scores
    random.shuffle(interview_scores)

    # Hiring decision process
    for i, score in enumerate(interview_scores):
        if score > best_score:
            best_score = score
            hired = i
            print(f"Interview {i+1}: Hire candidate {i+1} (CGPA: {candidates[i+1]['cgpa']}, Experience: {candidates[i+1]['experience']}, Role: {candidates[i+1]['role']})")
        else:
            print(f"Interview {i+1}: Reject candidate {i+1} (CGPA: {candidates[i+1]['cgpa']}, Experience: {candidates[i+1]['experience']}, Role: {candidates[i+1]['role']})")

    print(f"\nBest candidate found at interview {hired+1} with score {best_score} (CGPA: {candidates[hired+1]['cgpa']}, Experience: {candidates[hired+1]['experience']}, Role: {candidates[hired+1]['role']})")

# Number of candidates to interview
num_candidates = 15

print("Randomized Hiring Process:")
hire_assistant_randomized(num_candidates)
