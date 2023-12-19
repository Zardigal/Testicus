from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from exams.models import Exam, User, Question, Answer
from .core import Base64ImageField


class SolutionFieldSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()


class SolutionSerializer(serializers.Serializer):
    solutions = SolutionFieldSerializer(many=True, required=True)


class AuthorImageSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())
    image = Base64ImageField(required=False, allow_null=True)


class AnswerSerializer(AuthorImageSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('author')
        data.pop('correct')
        data.pop('question')
        data.pop('description')
        return data

    class Meta:
        model = Answer
        fields = (
            'id',
            'question',
            'text',
            'correct',
            'description',
            'image',
            'author'
        )
        read_only_fields = ('question',)


class QuestionSerializer(AuthorImageSerializer):
    answers = AnswerSerializer(many=True, required=False, allow_null=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('author')
        return data

    class Meta:
        model = Question
        fields = (
            'id',
            'exam',
            'text',
            'image',
            'answers',
            'author'
        )
        read_only_fields = ('exam',)


class ExamSerializer(AuthorImageSerializer):

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop('author')
        return data

    class Meta:
        model = Exam
        fields = (
            'id',
            'title',
            'description',
            'image',
            'author'
        )


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'first_name',
                  'last_name'
                  )
