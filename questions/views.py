from rest_framework import generics
from .models import Question, UserAnswer
from .serializers import QuestionSerializer, UserAnswerSerializer

class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all().order_by('number')
    serializer_class = QuestionSerializer

class UserAnswerCreateView(generics.CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
