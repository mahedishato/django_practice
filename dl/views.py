from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def deep_learning(request):
    he= 'welcome mahedi hasan '
    arr={'header':he.upper}
    return render(request,"dl/deep.html", arr )

def sub(request):
    return HttpResponse("<h1>2nd teb<h1> ")

class sub_line(View):
    def get(self, request):
        return render(request, 'dl/sub.html' )



