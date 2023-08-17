from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
def blogs(request):
    return render(request,'blogs/blogs.html' )



from blogs.forms import teacherRegistration
def showforms(request):
    if request.method =='POST':
        fb = teacherRegistration(request.POST)
        if fb.is_valid():
            print(fb.cleaned_data['password'])
            print(fb.cleaned_data['repassword'])
    else:
        fb = teacherRegistration()
        print('this is get statement')
    fb.order_fields(field_order=  ['email', 'first_name', 'last_name'])
    return render (request, 'blogs/forms.html', {'forms': fb})