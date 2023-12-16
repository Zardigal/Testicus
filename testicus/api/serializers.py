from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from exams.models import Exam, User, Question, Answer
from .core import Base64ImageField


class SolutionFieldSerializer(serializers.Serializer):
    question_id = serializers.IntegerField()
    answer_id = serializers.IntegerField()


class SolutionSerializer(serializers.Serializer):
    solutions = SolutionFieldSerializer(many=True, required=True)


class AnswerSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Answer
        fields = (
            'id',
            'question',
            'text',
            'correct',
            'description',
            'image'
        )
        read_only_fields = ('question',)


class QuestionSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False, allow_null=True)
    answers = AnswerSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = Question
        fields = (
            'id',
            'exam',
            'text',
            'image',
            'answers'
        )
        read_only_fields = ('exam',)


class ExamSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True,
                              default=serializers.CurrentUserDefault())
    image = Base64ImageField(required=False, allow_null=True)

    class Meta:
        model = Exam
        fields = (
            'id',
            'title',
            'description',
            'image',
            'author'
        )


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'exams')
