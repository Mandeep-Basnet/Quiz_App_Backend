from django.urls import path
from .views import create_question,getQuestions,get_question,get_questions_by_level,get_questions_by_category,createQuizAttempt

urlpatterns = [
  path('quizAttempt/create/',createQuizAttempt, name='create-quiz-attempt'),
  path('questions/category/<str:category>/', get_questions_by_category, name='get_questions_by_category'),
    path('questions/level/<str:level>/', get_questions_by_level, name='get_questions_by_level'),
    path('question/<int:id>',get_question,name='get_question_by_id'),
    path('questions/', getQuestions, name='get_question'),
    path('question/create/', create_question, name='create-question')
]
