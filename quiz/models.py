from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Question(models.Model):
    question = models.TextField()
    category = models.TextField()
    level = models.TextField()


class Option(models.Model):
    option = models.TextField()
    isCorrect = models.BooleanField()
    questionId = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="options")
    
class QuizAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    attemptedDate = models.DateTimeField(auto_now_add=True)
    totalScore = models.IntegerField(default=0)

class QuestionAttempt(models.Model):
    questionAttempt = models.ForeignKey(QuizAttempt, on_delete=models.CASCADE,related_name='questionsAttempt')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selectedOption = models.ForeignKey(Option, blank=True, null=True , on_delete=models.CASCADE)
    isCorrect = models.BooleanField(default=False)