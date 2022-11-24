from django.shortcuts import render

# Create your views here.


def if_condition(request):
    dict = {'a': 1000, 'b': 2000, 'c': 300, 'd': 400}
    return render(request, 'if_condition.html', context=dict)
