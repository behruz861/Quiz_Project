from django.urls import path
from .views import *

urlpatterns = [
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('add_question/', AddQuestionView.as_view(), name='add_question.html'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password')
]