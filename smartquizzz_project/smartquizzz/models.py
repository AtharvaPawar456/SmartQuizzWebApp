from django.db import models
from django.contrib.auth.models import User

# class QuizQuestion(models.Model):
#     question = models.TextField()
#     answer = models.CharField(max_length=255)
#     hint = models.TextField()
#     option1 = models.CharField(max_length=255)
#     option2 = models.CharField(max_length=255)
#     option3 = models.CharField(max_length=255)
#     option4 = models.CharField(max_length=255)
#     severity = models.CharField(max_length=10)  # low, medium, high
#     avg_time_to_answer = models.IntegerField()  # in seconds
#     marks = models.IntegerField()

# class UserResponse(models.Model):
#     user_answer = models.CharField(max_length=255)
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)  # assuming you have User model

# class QuizHistory(models.Model):
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     answered_correctly = models.BooleanField()
#     response_time = models.IntegerField()  # in seconds

# class QuizResult(models.Model):
#     question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     user_answer = models.CharField(max_length=255)
#     response_time = models.IntegerField()  # in seconds
#     severity = models.CharField(max_length=10)  # low, medium, high
#     marks_scored = models.IntegerField()


class AdminQuestion(models.Model):
    name = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    date = models.DateField()
    starttime = models.IntegerField()
    runtime = models.IntegerField()
    branch = models.CharField(max_length=10)
    extrainfo = models.TextField()
    maxQuestion = models.IntegerField()

class Question(models.Model):
    admin_question = models.ForeignKey(AdminQuestion, on_delete=models.CASCADE, related_name='questions')
    Question = models.TextField()
    Answer = models.TextField()
    Hint = models.TextField()
    Option1 = models.TextField()
    Option2 = models.TextField()
    Option3 = models.TextField()
    Option4 = models.TextField()
    Severity = models.CharField(max_length=10)
    AvgTimeToAnswer = models.IntegerField()
    Marks = models.IntegerField()


class SmartQuizQuestion(models.Model):
    name = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    date = models.DateField()
    starttime = models.PositiveIntegerField()
    runtime = models.PositiveIntegerField()
    branch = models.CharField(max_length=255)
    extrainfo = models.TextField()
    maxQuestion = models.PositiveIntegerField()
    question = models.TextField()
    answer = models.TextField()
    hint = models.TextField()
    option1 = models.TextField()
    option2 = models.TextField()
    option3 = models.TextField()
    option4 = models.TextField()
    severity = models.CharField(max_length=255)
    avgTimeToAnswer = models.PositiveIntegerField()
    marks = models.PositiveIntegerField()

    def __str__(self):
        return self.name