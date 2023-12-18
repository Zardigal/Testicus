from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Exam(models.Model):
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='название')
    description = models.TextField(verbose_name='описание')
    image = models.ImageField(
        upload_to='exams/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='exams',
        verbose_name='автор'
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'тесты'


class Question(models.Model):
    text = models.TextField(verbose_name='текст')
    image = models.ImageField(
        upload_to='questions/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )
    exam = models.ForeignKey(
        Exam,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='тест'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name='автор'
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'


class Answer(models.Model):
    text = models.TextField(verbose_name='текст')
    correct = models.BooleanField(
        default=False,
        verbose_name='правильный ответ')
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='описание')
    image = models.ImageField(
        upload_to='answers/',
        null=True,
        blank=True,
        verbose_name='изображение'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='вопрос'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name='автор'
    )

    def __str__(self) -> str:
        return self.text

    class Meta:
        verbose_name = 'ответ'
        verbose_name_plural = 'ответы'
