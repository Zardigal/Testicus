from django.urls import path

from .views import (homepage,
                    test_detail,
                    test_solution,
                    about)

app_name = 'frontend'

urlpatterns = [
    path('tests/<int:id>/solution/', test_solution, name='test_solution'),
    path('tests/<int:id>/', test_detail, name='test_detail'),
    path('about/', about, name='about'),
    path('', homepage, name='index'),
]
