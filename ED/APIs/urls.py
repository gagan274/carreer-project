from APIs import views
from django.urls import path

urlpatterns = [
    path('login/', views.loginApi),
    path('register/',views.registerApi),
    path('requestotp/',views.ForgetPasswordRequestApi),
    path('validateotp/',views.ForgetPasswordValidateApi),
    path('quizmarks/',views.QuizMarks),
    path('webinars/',views.webinars),
    path('counselling/',views.counselling),
    path('schoolmarks/',views.SchoolMarks),
    path('decesiontree/',views.DecesionTree)
]