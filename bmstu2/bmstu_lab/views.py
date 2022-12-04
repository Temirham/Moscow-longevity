from django.shortcuts import render
from django.shortcuts import render
# Create your views here.
from datetime import date


def index(request):
    return render(request, 'index.html',
                  {'current_date': date.today()})

def about(request):
    return render(request, 'about.html')


def GetOrders(request):
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'orders': [
            {'title': 'Библиотеки', 'id': 1},
            {'title': 'Ярмарки', 'id': 2},
            {'title': 'Бассейны', 'id': 3},
        ]
    }})


def GetOrder(request, id):
    return render(request, 'order.html', {'data': {
        'current_date': date.today(),
        'id': id
    }})


def sendText(request):
    input_text = request.POST['text']
    return render(request, 'orders.html', {'data': {
        'current_date': date.today(),
        'orders': [
            {'title': 'Библиотеки', 'id': 1},
            {'title': 'Ярмарки', 'id': 2},
            {'title': 'Бассейны', 'id': 3},
        ],
    'input_text' : int(input_text)}})
from django.shortcuts import render

# Create your views here.
