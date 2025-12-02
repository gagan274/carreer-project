README – AI-Driven Career Guidance System

1.Overview

  *  A web-based AI system that helps students choose the right academic stream after Grade 10.

  *  Uses academic marks, aptitude tests, and interest assessments for predictions.

  *  Powered by a Decision Tree algorithm with 92% accuracy.
  *  https://github.com/gagan274/carreer-project/blob/main/Screenshot%202025-12-02%20104829.png?raw=true
  

2. Key Features

  AI-based stream recommendation

  Interactive aptitude & interest quizzes

  One-on-one counselling session booking

  Webinars & career awareness sessions

  Resource library for career information

  Secure login and user profiles

  Admin dashboard for counsellors

  Tech Stack

Frontend: React.js

Backend: Django REST Framework

Database: MongoDB

Deployment: AWS (EC2 / S3 / Lambda options)

UI: Tailwind CSS or Material UI

AI Model

Decision Tree Classifier

Inputs used:

Academic records

Aptitude scores

Interest test results

Outputs:

Recommended stream (Science / Commerce / Arts)

Explanation of prediction

Installation Steps

Clone the repository

git clone https://github.com/yourusername/career-guidance-system.git


Install frontend

cd frontend
npm install
npm start


Install backend

cd backend
pip install -r requirements.txt
python manage.py runserver


Set up environment variables (.env in frontend & backend)

Environment Configuration

Backend .env:

MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_django_secret_key


How to Use

Student signs up and logs in

Completes aptitude & interest assessments

System processes data using Decision Tree

Student receives predicted academic stream

Student explores resources, books counselling, or attends webinars

Project Folder Structure

project/
├── frontend/
├── backend/
├── model/
└── README.md


Future Improvements

Chatbot for career guidance using NLP

Support for regional languages

Integration of advanced ML models (Random Forest, XGBoost)

Real-time analytics for schools

License

This project is released under the MIT License.
