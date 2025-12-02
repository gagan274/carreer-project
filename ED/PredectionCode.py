
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

from Sendmail import *

def ModelPredection(Data, quizMarks, email):

    # Load the data from san existing CSV file
    data = pd.read_csv("student_marks_predictions.csv")

    # Split the data into features and target
    X = data.drop(columns=["Prediction"])
    y = data["Prediction"]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Decision Tree Classifier
    decision_tree = DecisionTreeClassifier(random_state=42)
    decision_tree.fit(X_train, y_train)
    dt_predictions = decision_tree.predict(X_test)
    dt_accuracy = accuracy_score(y_test, dt_predictions)
    print(f"Decision Tree Accuracy: {dt_accuracy:.2f}")

    # Random Forest Classifier
    random_forest = RandomForestClassifier(random_state=42)
    random_forest.fit(X_train, y_train)
    rf_predictions = random_forest.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_predictions)
    print(f"Random Forest Accuracy: {rf_accuracy:.2f}")

    print("Data: ", Data)

    # Prompt user for new data
    print("Enter the marks for a new student:")
    science_marks_8th = Data["8"]["Science"]
    social_marks_8th = Data["8"]["Social"]
    maths_marks_8th = Data["8"]["Math"]
    science_marks_9th = Data["9"]["Science"]
    social_marks_9th = Data["9"]["Social"]
    maths_marks_9th = Data["9"]["Math"]
    science_marks_10th = Data["10"]["Science"]
    social_marks_10th = Data["10"]["Social"]
    maths_marks_10th = Data["10"]["Math"]
    quiz_marks_science = quizMarks["Science"]
    quiz_marks_social = quizMarks["Arts"]
    quiz_marks_maths = quizMarks["Commerce"]

    # Prepare the input data
    new_data = pd.DataFrame({
        "Science_8th": [science_marks_8th],
        "Social_8th": [social_marks_8th],
        "Maths_8th": [maths_marks_8th],
        "Science_9th": [science_marks_9th],
        "Social_9th": [social_marks_9th],
        "Maths_9th": [maths_marks_9th],
        "Science_10th": [science_marks_10th],
        "Social_10th": [social_marks_10th],
        "Maths_10th": [maths_marks_10th],
        "Quiz_Science": [quiz_marks_science],
        "Quiz_Social": [quiz_marks_social],
        "Quiz_Maths": [quiz_marks_maths]
    })

    # Make predictions
    decision_tree_prediction = decision_tree.predict(new_data)
    random_forest_prediction = random_forest.predict(new_data)

    print(f"Decision Tree Prediction: {decision_tree_prediction[0]}")
    print(f"Random Forest Prediction: {random_forest_prediction[0]}")

    # Display prediction accuracy
    print(f"Decision Tree Prediction Accuracy: {dt_accuracy:.2f}")
    print(f"Random Forest Prediction Accuracy: {rf_accuracy:.2f}")

    if decision_tree_prediction[0] == "Science" or decision_tree_prediction[0] == "Strongly Science":
        message = f'Dear User \r\n Your Predection result is Science \r\n\n Best Regards,\r\n EFFECTIVE CARRER BUILDING USING ML ALGORITHM'
    elif decision_tree_prediction[0] == "Commerce" or decision_tree_prediction[0] == "Strongly Commerce":
        message = f'Dear User \r\n Your Predection result is Commerce \r\n\n Best Regards,\r\n EFFECTIVE CARRER BUILDING USING ML ALGORITHM'
    elif decision_tree_prediction[0] == "Arts":
        message = f'Dear User \r\n Your Predection result is Arts \r\n\n Best Regards,\r\n EFFECTIVE CARRER BUILDING USING ML ALGORITHM'
    Subject = "Predection result for the carrer Options"
    ReceiverEmail = email
    send_email([ReceiverEmail], Subject, message)
    return {"accuracy":dt_accuracy, "predection":decision_tree_prediction[0]}
