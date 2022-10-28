from django.shortcuts import render,redirect
from secondapp.form import student_form

def page2(request):
    if request.method=='POST':
        #to submit the data and display
        form=student_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app1:firstpage')
    else:
        form = student_form()
    

    return render(request,'home.html',{'form':form})
# Create your views here.
