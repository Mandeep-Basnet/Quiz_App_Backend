from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from .serializers import *
from django.http import JsonResponse, HttpResponseNotFound
from rest_framework.permissions import IsAuthenticated
from .models import Question
from rest_framework.response import Response 

# Create your views here.

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Question created successfully!", "status": HTTP_201_CREATED})
    return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getQuestions(request):
    questions = Question.objects.all()[:20]
    serializer = QuestionSerializer(instance=questions, many=True)
    return Response(serializer.data, status= HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_question(request, id):
    try:
        question = Question.objects.get(id=id)
        serializer = QuestionSerializer(instance=question)
        return Response(serializer.data, status=HTTP_200_OK)
    except Question.DoesNotExist:
        return JsonResponse({"message": "Question not found"}, status=HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_questions_by_level(request, level):
    if level not in ['easy', 'medium', 'hard', 'random']:
        return JsonResponse({"message": "Invalid difficulty level"}, status=HTTP_400_BAD_REQUEST)
    
    if level == 'random':
        questions = Question.objects.all()[:20]
    else:
        questions = Question.objects.filter(level=level)[:20]

    serializer = QuestionSerializer(instance=questions, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_questions_by_category(request, category):
    if category not in ['Geography', 'Astronomy', 'Literature','Chemistry', 'Physics', 'Science','Computer','Math', 'Art', 'Technology', 'Cuisine','Economics', 'random']:
        return JsonResponse({"message": "Invalid difficulty category"}, status=HTTP_400_BAD_REQUEST)
    
    if category == 'random':
        questions = Question.objects.all()[:20]
    else:
        questions = Question.objects.filter(category=category)[:20]

    serializer = QuestionSerializer(instance=questions, many=True)
    return Response(serializer.data, status=HTTP_200_OK)  

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createQuizAttempt(request):
    serializer = QuizAttemptSerializer(data=request.data,context={'request':request})
    if serializer.is_valid():
        serializer.save()
        return Response (serializer.data, status=HTTP_200_OK) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)