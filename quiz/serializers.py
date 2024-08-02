from rest_framework import serializers
from .models import *


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option', 'isCorrect']
        required = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'question', 'category', 'level', 'options']
        required = ['question', 'category', 'level', 'options']

    def create(self, validated_data):
        options = validated_data.pop('options')
        question = Question.objects.create(**validated_data)

        for option in options:
            Option.objects.create(questionId=question, **option)

        return question

class QuestionAttemptSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = QuestionAttempt
        fields = ['id', 'question', 'isCorrect']

class QuizAttemptSerializer(serializers.ModelSerializer):
    questionsAttempt = QuestionAttemptSerializer(many = True, read_only=True)

    class Meta:
        model = QuizAttempt
        fields = ['id','attemptedDate', 'questionsAttempt', 'totalScore']       

    def create(self, validated_data):
        user = self.context['request'].user
        quiz_attempt = QuizAttempt.objects.create(user=user)

        questions = list(Question.objects.all().order_by('?')[:20])

        for question in questions:
            QuestionAttempt.objects.create(question=question,questionAttempt=quiz_attempt)

        return quiz_attempt    