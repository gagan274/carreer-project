README – AI-Driven Career Guidance System

![image alt](https://github.com/gagan274/carreer-project/blob/main/Screenshot%202025-12-02%20104829.png?raw=true)

1. Overview
- A web-based AI system that helps students choose the right academic stream after Grade 10.
- Uses academic marks, aptitude tests, and interest assessments for predictions.
- Powered by a Decision Tree algorithm with 92% accuracy.

2. Key Features
 1. AI-based stream recommendation
 2. Interactive aptitude & interest quizzes
 3. One-on-one counselling session booking
 4. Webinars & career awareness sessions
 5. Resource library for career information
 6. Secure login and user profiles
 7. Admin dashboard for counsellors

3. Tech Stack
 - Frontend: React.js
 - Backend: Django REST Framework
 - Database: MongoDB
 - Deployment: AWS
 - UI: Tailwind CSS or Material UI

4. AI Model
 1. Decision Tree Classifier
 2. Inputs used:
   - Academic records
   - Aptitude scores
   - Interest test results
 3. Outputs:
   - Recommended stream (Science / Commerce / Arts)
   - Explanation of prediction

5. Installation Steps
 1. Clone the repository
  git clone https://github.com/yourusername/career-guidance-system.git
 2. Install frontend
  cd frontend
  npm install
  npm start
 3. Install backend
  cd backend
  pip install -r requirements.txt
  python manage.py runserver
 4. Set up environment variables (.env)
 
 6. Environment Configuration
  Backend .env:
  MONGO_URI=your_mongodb_connection_string
  SECRET_KEY=your_django_secret_key

Frontend .env:
  REACT_APP_API_URL=http://localhost:8000

7. How to Use
  1. Student signs up and logs in
  2. Completes aptitude & interest assessments
  3. System processes data using Decision Tree
  4. Student receives predicted academic stream
  5. Student explores resources, books counselling, or attends webinars

8. Project Folder Structure
project/
├── frontend/
├── backend/
├── model/
└── README.md

9. Future Improvements
1. Chatbot for career guidance using NLP
2. Support for regional languages
3. Integration of advanced ML models (Random Forest, XGBoost)
4. Real-time analytics for schools

