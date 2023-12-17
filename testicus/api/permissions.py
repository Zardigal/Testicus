from django.shortcuts import get_object_or_404
from rest_framework import permissions
from exams.models import Exam


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or obj.author == request.user
        )


class QuestionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        str_path = str(request.path)
        text_before = 'tests/'
        text_after = '/questions'
        start_index_id = str_path.find(text_before) + len(text_before)
        end_index_id = str_path.find(text_after)
        test_id = int(str_path[start_index_id:end_index_id])
        test = get_object_or_404(Exam, id=test_id)

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user == test.author
        )
