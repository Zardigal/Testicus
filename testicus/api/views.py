from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from exams.models import Exam, User, Question, Answer
from .serializers import (ExamSerializer,
                          CustomUserSerializer,
                          QuestionSerializer,
                          AnswerSerializer,
                          SolutionSerializer)
from .permissions import (IsAdminAuthorOrReadOnly,
                          AnswerQuestionPermission,
                          IsAdminUserOrReadOnly)
from .core import get_percent
from .mixins import ListRetrieveUpdateDestroyMixin


@api_view(['POST'])
def exam_solution(request, id):
    serializer = SolutionSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    exam = get_object_or_404(Exam, id=id)
    questions = Question.objects.filter(exam=exam)
    question_quantity = len(questions)
    correct_answ_for_quest = {}
    correct_solutions = 0
    solutions = request.data.get('solutions')

    if len(solutions) != question_quantity:
        raise serializers.ValidationError('Необходимо ответить на все вопросы')

    for question in questions:
        correct_answer = Answer.objects.get(question=question, correct=True)
        correct_answ_for_quest[question.id] = correct_answer.id

    for solution in solutions:
        if correct_answ_for_quest[solution['question_id']] == solution['answer_id']:
            correct_solutions += 1

    try:
        percent = get_percent(correct_solutions, question_quantity)
    except ZeroDivisionError:
        percent = 0

    return Response(data={'percent': percent}, status=status.HTTP_200_OK)


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = (IsAdminAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    permission_classes = (AnswerQuestionPermission,)

    def get_queryset(self):
        exam_id = self.kwargs.get('test_id')
        new_querryset = Question.objects.filter(exam=exam_id)
        return new_querryset

    def perform_create(self, serializer):
        exam = Exam.objects.get(id=self.kwargs.get("test_id"))
        serializer.save(exam=exam, author=self.request.user)


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    permission_classes = (AnswerQuestionPermission,)

    def get_queryset(self):
        question_id = self.kwargs.get('question_id')
        new_querryset = Answer.objects.filter(question=question_id)
        return new_querryset

    def perform_create(self, serializer):
        question = Question.objects.get(id=self.kwargs.get("question_id"))
        serializer.save(question=question, author=self.request.user)


class UserViewSet(ListRetrieveUpdateDestroyMixin):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
