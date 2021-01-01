from django.shortcuts import render

def main_vew(request):
    return render(request, 'main.html')
