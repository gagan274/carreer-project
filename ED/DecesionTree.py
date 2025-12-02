import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from Sendmail import *
from pymongo import MongoClient
 
def recommend_stream(email):
    client = MongoClient('mongodb+srv://Developer:Admin1234@cluster0.ch7yz.mongodb.net/?retryWrites=true&w=majority&tls=true')
 
    db = client['project']
    collection_marks = db['marks']
    collection_quiz = db['quiz']
    document_marks = collection_marks.find_one({"email":email}, {'_id': 0})
    document_quiz = collection_quiz.find_one({"email":email}, {'_id': 0})
    data = {
        'quiz1': document_quiz['Commerce'],
        'quiz2': document_quiz['Arts'],
        'quiz3': document_quiz['Science'],
        'marks': {k: {subject: 100 for subject in ['maths', 'science', 'social']} for k in document_marks if k != 'email'}
    }
 
    print("Data : ",data)
 
    if 'quiz1' not in data or 'quiz2' not in data or 'quiz3' not in data:
        print("Need Quiz Marks")
        return (False, "Need Quiz Marks")
    # Check if marks are present and contain keys from 1 to 10
    if 'marks' not in data:
        print("Needed Acedemic Marks")
        return (False, "Needed Acedemic Marks")
    for i in range(1, 11):
        if str(i) not in data['marks']:
            print("Need to enter Acedemic marks")
            return (False, "Needed Acedemic Marks")
 
    print(True)
 
    # Prepare the data for DataFrame
    quiz1 = [data["quiz1"]] * len(data["marks"])
    quiz2 = [data["quiz2"]] * len(data["marks"])
    quiz3 = [data["quiz3"]] * len(data["marks"])
    marks = data["marks"]
 
    # Create a DataFrame
    df = pd.DataFrame(marks).T
    df["quiz1"] = quiz1
    df["quiz2"] = quiz2
    df["quiz3"] = quiz3
 
    # Define the target variable (stream)
    # For simplicity: Science if science > maths and science > social; Arts if social > maths and social > science; else Commerce
    def recommend_stream(row):
        if row['science'] >= row['maths'] and row['science'] >= row['social']:
            return 'Science'
        elif row['social'] >= row['maths'] and row['social'] >= row['science']:
            return 'Arts'
        else:
            return 'Commerce'
 
    df['stream'] = df.apply(recommend_stream, axis=1)
 
    # Features and target variable
    features = ['quiz1', 'quiz2', 'quiz3','maths', 'science', 'social']
    X = df[features]
    y = df['stream']
 
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
 
    # Create a Decision Tree Classifier
    clf = DecisionTreeClassifier()
 
    # Train the classifier
    clf = clf.fit(X_train,y_train)
 
    # Predict the response for test dataset
    y_pred = clf.predict(X_test)
 
    # Model Accuracy
    accuracy = metrics.accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
 
    # Example prediction for a new student
    new_student = pd.DataFrame({
        'quiz1': [data['quiz1']],
        'quiz2': [data['quiz2']],
        'quiz3': [data['quiz3']],
        'maths': [40],
        'science': [50],
        'social': [30]
    })
 
    predicted_stream = clf.predict(new_student)
    print(f"Recommended stream for the new student: {predicted_stream[0]}")
 
    # Save the DataFrame to a CSV file for reference
    df.to_csv('student_data.csv', index=False)
    print("Supporting data saved to student_data.csv")
    if predicted_stream[0] == "Commerce":
        receiver_email = ["vishwas.chandrappa@gmail.com","abhishekshetty.1222@gmail.com","dhanumysr14@gmail.com","gagannayaka.2003@gmail.com"]
        subject = "Predection result for the carrer Options"
        body = """
        <p>Dear User,</p>
        <p>Your predicted result is Commerce .</p>
        <p>Best regards,<br>
        <p>EFFECTIVE CARRER BULDING USING ML ALGORITHM .</p>
        """
        
    elif predicted_stream[0] == "Science":
        receiver_email = ["vishwas.chandrappa@gmail.com","abhishekshetty.1222@gmail.com","dhanumysr14@gmail.com","gagannayaka.2003@gmail.com"]
        subject = "Predection result for the carrer Options"
        body = """
        <p>Dear User,</p>
        <p>Your predicted result is Science .</p>
        <p>Best regards,<br>
        <p>EFFECTIVE CARRER BULDING USING ML ALGORITHM .</p>
        """
        
    else:
        receiver_email = ["vishwas.chandrappa@gmail.com","abhishekshetty.1222@gmail.com","dhanumysr14@gmail.com","gagannayaka.2003@gmail.com"]
        subject = "Predection result for the carrer Options"
        body = """
        <p>Dear User,</p>
        <p>Your predicted result is Arts .</p>
        <p>Best regards,<br>
        <p>EFFECTIVE CARRER BULDING USING ML ALGORITHM .</p>
        """
        
        
    send_email(receiver_email, subject, body)
    return (True, accuracy, predicted_stream[0])
