from django.shortcuts import get_object_or_404
from rest_framework import permissions
from exams.models import Exam
from .core import get_object_id_from_url


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


class AnswerQuestionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        test_id = get_object_id_from_url(
            path=request.path,
            text_before='tests/',
            text_after='/questions')
        test = get_object_or_404(Exam, id=test_id)

        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or request.user == test.author
        )


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
            or obj == request.user
        )
