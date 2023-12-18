from django.shortcuts import render


def homepage(request):
    template = 'testicum/index.html'
    return render(request, template)


def test_detail(request, id):
    template = 'testicum/detail.html'
    return render(request, template)


def test_solution(request, id):
    template = 'testicum/solution.html'
    return render(request, template)


def about(request):
    template = 'about.html'
    return render(request, template)
