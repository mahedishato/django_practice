from django.shortcuts import render
from django.http import HttpResponse
from demo.models import teaccher

# Create your views here.


def machine(request):
    return HttpResponse('<h1>mahedi hasan rasel<h1>')


def deep(request):
    gaan =['mahedi ', 'hasan', 'rasel']

    variable = {'c':gaan,
                'facebook':'facebook.com/',
                'insta':'instagram.com',
                'linkedin':'linkedin.com'}
    return render(request, 'demo/index.html', variable)

def review(request):
    ami = 'mahedi hasan rasel'
    variable = {'what': 'Mahedi Hasan', 
                'me': ami,
                'name': 'shota',
                'picture': 'data:image/jpeg;base64,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'}
    return render(request, 'demo/review.html', variable)

def news(request):
    return render(request, 'demo/news.html')

def nai(request):
    return render(request, 'demo/demo.html')




def teacher_info(request):
    teacher_ = teaccher.objects.all()
    return render (request , 'demo/teacher.html' , {'thr': teacher_})
    


from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.method=='POST':
        fo= UserCreationForm(request.POST)
        if fo.is_valid():
            fo.save()
    else:
        fo= UserCreationForm()
    return render(request, 'demo/registrate.html', {'form': fo})