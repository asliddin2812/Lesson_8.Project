from django.urls import path
from .views import QuestionListView, UserAnswerCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name='question-list'),
    path('answers/', UserAnswerCreateView.as_view(), name='user-answer-create'),
]
