from rest_framework import routers

from django.urls import include, path

from .views import (ExamsViewSet,
                    UserViewSet,
                    QuestionViewSet,
                    AnswerViewSet,
                    exam_solution)


router_v1 = routers.DefaultRouter()
router_v1.register(r'tests', ExamsViewSet)
router_v1.register(r'^tests/(?P<test_id>\d+)/questions',
                   QuestionViewSet, basename='question')
# router_v1.register(r'^tests/(?P<test_id>\d+)/solution',
#                    SolutionViewSet, basename='solution')
router_v1.register(
    r'^tests/(?P<test_id>\d+)/questions/(?P<question_id>\d+)/answers',
    AnswerViewSet,
    basename='answer')
router_v1.register(r'users', UserViewSet)


urlpatterns = [
    path(route='tests/<int:id>/solution', view=exam_solution),
    path('', include(router_v1.urls))
]
