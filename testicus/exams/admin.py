from django.contrib import admin
from .models import Exam, Question, Answer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'author')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    inlines = [QuestionInline]


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'exam')
    list_display_links = ('id', 'text')
    list_filter = ('exam',)
    search_fields = ('id', 'text')
    inlines = [AnswerInline]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'text',
                    'correct',
                    'description',
                    'question')
    list_display_links = ('id', 'text')
    list_filter = ('question',)
    search_fields = ('id', 'text', 'question')
