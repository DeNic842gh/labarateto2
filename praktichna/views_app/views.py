from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'title': 'Головна сторінка'})

def view1(request):
    return render(request, 'view.html', {'title': 'Сторінка 1'})

def view2(request):
    return render(request, 'view.html', {'title': 'Сторінка 2'})

def view3(request):
    return render(request, 'view.html', {'title': 'Сторінка 3'})

def view4(request):
    return render(request, 'view.html', {'title': 'Сторінка 4'})

def view5(request):
    return render(request, 'view.html', {'title': 'Сторінка 5'})