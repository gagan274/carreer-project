import csv
import random

# Define the grades and subjects
grades = ['8th', '9th', '10th']
subjects = ['Science', 'Social', 'Maths']

# Generate predictions based on marks
def predict_stream(science, social, maths):
    if science > 80 and social > 80 and maths > 80:
        return "Science"
    elif science < 50 and social < 50 and maths < 50:
        return "Arts"
    elif science > social and science > maths:
        return "Strongly Science"
    elif maths > science and social > science:
        return "Strongly Commerce"
    elif social > science and social > maths:
        return "Commerce"
    else:
        return "Arts"

# Generate random student data
num_students = 10000
student_data = []

for _ in range(num_students):
    science_marks_8th = random.randint(35, 100)  # Ensure a passing range of marks
    social_marks_8th = random.randint(35, 100)
    maths_marks_8th = random.randint(35, 100)

    science_marks_9th = random.randint(35, 100)
    social_marks_9th = random.randint(35, 100)
    maths_marks_9th = random.randint(35, 100)

    science_marks_10th = random.randint(35, 100)
    social_marks_10th = random.randint(35, 100)
    maths_marks_10th = random.randint(35, 100)

    quiz_marks_science = random.randint(5, 20)
    quiz_marks_social = random.randint(5, 20)
    quiz_marks_maths = random.randint(5, 20)

    prediction_10th = predict_stream(science_marks_10th, social_marks_10th, maths_marks_10th)

    student_data.append({
        "Science_8th": science_marks_8th,
        "Social_8th": social_marks_8th,
        "Maths_8th": maths_marks_8th,
        "Science_9th": science_marks_9th,
        "Social_9th": social_marks_9th,
        "Maths_9th": maths_marks_9th,
        "Science_10th": science_marks_10th,
        "Social_10th": social_marks_10th,
        "Maths_10th": maths_marks_10th,
        "Quiz_Science": quiz_marks_science,
        "Quiz_Social": quiz_marks_social,
        "Quiz_Maths": quiz_marks_maths,
        "Prediction": prediction_10th
    })

# Write to CSV file
csv_file = "student_marks_predictions.csv"
fieldnames = [
    "Science_8th", "Social_8th", "Maths_8th",
    "Science_9th", "Social_9th", "Maths_9th",
    "Science_10th", "Social_10th", "Maths_10th",
    "Quiz_Science", "Quiz_Social", "Quiz_Maths",
    "Prediction"
]

with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(student_data)

print(f"CSV file '{csv_file}' has been generated with student marks and predictions.")
