from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course
from facultyapp.models import CourseContent


# Create your views here.
def studenthome(request):
    studentid = request.session["studentid"]
    student=Student.objects.get(studentid=studentid)
    print(student)

    return render(request,"studenthome.html",{"studentid":studentid,"student":student})

def checkstudentlogin(request):
    studentid = request.POST["studentid"]
    pwd = request.POST["pwd"]

    flag=Student.objects.filter(Q(Studentid=studentid)&Q(password=pwd))
    print(flag)

    if flag:
        print("login success")
        request.session["studentid"]=studentid

        student = Student.objects.get(Studentid=studentid)
        print(student)


        return render(request,"studenthome.html",{"studentid":studentid,"student":student})
    else:
        msg="login failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("login failed")

def studentchangepwd(request):
    studentid=request.session["studentid"]

    return render(request,"studentchangepwd.html",{"studentid":studentid})
def studentupdatepwd(request):
    studentid=request.session["studentid"]
    print(studentid)
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(studentid,opwd,npwd)


    flag=Student.objects.filter(Q(studentid=studentid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Student.objects.filter(studentid=studentid).update(password=npwd)
        print("updated...")
        msg="password updated succesfully"
    else:
        print("old pwd is incorrect")
        msg=" old password is invalid"


    return render(request,"studentchangepwd.html",{"studentid": studentid,"message":msg})

def studentcourses(request):
    studentid = request.session["studentid"]
    return render(request,"studentcourses.html",{"studentid":studentid})

def displaystudentcourses(request):
    studentid=request.session["studentid"]
    academicyear=request.POST["academicyear"]
    semester=request.POST["semester"]
    courses=Course.objects.filter(Q(academicyear=academicyear)&Q(semester=semester))
    return render(request,"displaystudentcourses.html",{"courses":courses,"studentid":studentid})

def studentcoursecontent(request):
    studentid=request.session["studentid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"studentid":studentid,"coursecontent":content})




