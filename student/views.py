from django.shortcuts import render
from .forms import StudForm,SForm
from .models import stud
# Create your views here.
def show(request):
    return render(request,"home.html")

def register(request):
    title="Student Registration"
    form= StudForm(request.POST or None)

    if form.is_valid():
        name= form.cleaned_data['s_name']
        clas= form.cleaned_data['s_class']
        addr= form.cleaned_data['s_addr']
        school= form.cleaned_data['s_school']
        mail= form.cleaned_data['s_email']
        email= stud.objects.filter(s_email=mail)
        if len(email)>0:
             return render(request,'a.html',{"title":"Student Already Exists.Try with other E-Mail"})
        else:
            p=stud(s_name=name,s_class=clas,s_addr=addr,s_school=school,s_email=mail)
            p.save()
            return render(request,'a.html',{"title":"Registered Successfully"})

    context={
        "title":title,
        "form":form,
    }

    return render(request,'register.html',context)

def existing(request):
    title="All Registered Students"
    queryset= stud.objects.all()

    context={
        "title":title,
        "queryset":queryset,
    }
    return render(request,'existingstud.html',context)
def search(request):
    title="Search Student"
    form=SForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data['s_name']
        queryset= stud.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'a.html',{'title':'Student Details Not Found.. Pleae Enter Correct Data'})
        context={
            'title':title,
            'queryset':queryset,
        }
        return render(request,'existingstud.html',context)
    context={
        'title':title,
        'form':form,

    }
    return render(request,'search.html',context)


def dropout(request):
    title="Drop Out"
    form=SForm(request.POST or None)
    if form.is_valid():
        name= form.cleaned_data['s_name']
        queryset= stud.objects.filter(s_name=name)
        if len(queryset)==0:
            return render(request,'a.html',{'title':'Student Details Not Found.. Pleae Enter Correct Data'})
        else:
            queryset= stud.objects.filter(s_name=name).delete()
        return render(request,'a.html',{'title':"Student removed from your Database"})
    context={
        'title':title,
        'form':form,

    }
    return render(request,'search.html',context)
