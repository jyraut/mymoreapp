from django.shortcuts import redirect, render
from .models import *
from secondapp.form import *

def index(request):
    data=student.objects.all()
    return render(request,'f1.html',{'data':data})


# To delete record
def del_record(request,d):
    s1=student.objects.get(id=d)
    s1.delete()
    return redirect('app1:firstpage')

#to edit data
def edit_record(request,d):
    s1 = student.objects.get(id=d)
    if request.method=='POST':
        #to submit the data and display
        form=student_form(request.POST,instance=s1)
        if form.is_valid():
            form.save()
            return redirect('app1:firstpage')
    else:
        form = student_form(instance=s1)
    

    return render(request,'edit.html',{'form':form})