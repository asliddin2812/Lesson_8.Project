from rest_framework import serializers
from .models import Question, ImageOption, UserAnswer

class ImageOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOption
        fields = ['id', 'image', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = ImageOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'number', 'text', 'options']

class UserAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id', 'user_id', 'question', 'selected_option', 'timestamp']
