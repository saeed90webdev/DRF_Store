from django.shortcuts import render

def show_data(request):
    return render(request, 'hello.html')
