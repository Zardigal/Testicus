import csv

from django.core.management.base import BaseCommand

from exams.models import (Exam,
                          Question,
                          Answer,
                          User)


def import_exam():
    with open('static/data/exams.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Exam.objects.create(
                id=row['id'],
                title=row['title'],
                description=row['description'],
                author_id=row['author_id'],
            )


def import_question():
    with open('static/data/questions.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Question.objects.create(
                id=row['id'],
                text=row['text'],
                exam_id=row['exam_id'],
                author_id=row['author_id'],
            )


def import_answer():
    with open('static/data/answers.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            Answer.objects.create(
                id=row['id'],
                text=row['text'],
                correct=row['correct'],
                question_id=row['question_id'],
                author_id=row['author_id'],
            )


def import_user():
    with open('static/data/users.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            User.objects.create(
                id=row['id'],
                username=row['username'],
                password=row['password'],
            )


class Command(BaseCommand):
    help = 'Import data from csv file.'

    def handle(self, *args, **options):
        import_user()
        import_exam()
        import_question()
        import_answer()
        self.stdout.write(self.style.SUCCESS('Data imported from csv.'))
