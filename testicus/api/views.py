from rest_framework import viewsets

from exams.models import Exam, User, Question, Answer
from .serializers import (ExamSerializer,
                          UserSerializer,
                          QuestionSerializer,
                          AnswerSerializer)


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        exam_id = self.kwargs.get('test_id')
        new_querryset = Question.objects.filter(exam=exam_id)
        return new_querryset

    def perform_create(self, serializer):
        exam = Exam.objects.get(id=self.kwargs.get("test_id"))
        serializer.save(exam=exam)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        new_querryset = Answer.objects.filter(question=question_id)
        return new_querryset

    def perform_create(self, serializer):
        question = Question.objects.get(id=self.kwargs.get("question_id"))
        serializer.save(question=question)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
