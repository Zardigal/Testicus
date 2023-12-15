from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Exam(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(
        upload_to='exams/', null=True, blank=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='exams'
    )

    def __str__(self) -> str:
        return self.title


class Question(models.Model):
    text = models.TextField()
    image = models.ImageField(
        upload_to='questions/', null=True, blank=True
    )
    exam = models.ForeignKey(
        Exam, on_delete=models.CASCADE, related_name='questions'
    )

    def __str__(self) -> str:
        return self.text


class Answer(models.Model):
    text = models.TextField()
    correct = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='answers/', null=True, blank=True
    )
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answers'
    )

    def __str__(self) -> str:
        return self.text
