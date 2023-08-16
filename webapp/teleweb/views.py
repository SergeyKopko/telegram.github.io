from django.shortcuts import render

# Create your views here.


def main_window(request):
    return render(request, 'teleweb/index.html')