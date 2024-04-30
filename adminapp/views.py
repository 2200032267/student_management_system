from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Admin,Course,Student,Faculty,FacultyCourseMapping
from .forms import AddFacultyForm,AddStudentForm,StudentForm


# Create your views here.
def adminhome(request):
    auname = request.session["auname"]

    return render(request,"adminhome.html",{"adminuname":auname})

# Create your views here.


def logout(request):
    return render(request,"login.html")

def checkadminlogin(request):
    adminuname = request.POST["uname"]
    adminpwd = request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        print("login success")
        request.session["auname"]=adminuname
        return render(request,"adminhome.html",{"adminuname":adminuname})
    else:
        msg="login failed"
        return render(request,"login.html",{"message":msg})
        #return HttpResponse("login failed")




def viewstudents(request):
    student = Student.objects.all()
    count = Student.objects.count()
    auname = request.session["auname"]

    return render(request, "viewstudents.html", {"studentsdata": student, "count": count,"adminuname":auname})


def viewfaculty(request):
    auname = request.session["auname"]

    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request,"viewfaculty.html",{"facultydata":faculty,"count":count,"adminuname":auname})

def viewcourses(request):
    auname = request.session["auname"]

    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"viewcourses.html",{"coursesdata":courses,"count":count,"adminuname":auname})

def adminstudent(request):
    auname=request.session["auname"]
    return render(request,"adminstudent.html",{"adminuname":auname})

def admincourse(request):
    auname=request.session["auname"]

    return render(request,"admincourse.html",{"adminuname":auname})

def adminfaculty(request):
    auname=request.session["auname"]

    return render(request,"adminfaculty.html",{"adminuname":auname})

def addcourses(request):
    auname=request.session["auname"]

    return render(request,"addcourses.html",{"adminuname":auname})
def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()

    return render(request, "updatecourse.html", {"adminuname": auname,"courses":courses,"count":count})

def courseupdation(request,courseid):
    auname = request.session["auname"]

    return render(request,"courseupdation.html",{"courseid":courseid,"adminuname": auname})
def courseupdated(request):
    auname = request.session["auname"]

    courseid=request.POST["courseid"]


    ltps=request.POST["ltps"]

    credits=request.POST["credits"]
    Course.objects.filter(id=courseid).update(ltps=ltps,credits=credits)
    msg="course updated successfully"
    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname})

def insertcourse(request):
    auname = request.session["auname"]

    if request.method=="POST":
        dept=request.POST["dept"]
        program=request.POST["program"]
        academicYear =request.POST["academicYear"]
        semester=request.POST["semester"]
        year=request.POST["year"]
        coursecode=request.POST["coursecode"]
        CourseTitle=request.POST["CourseTitle"]
        ltps=request.POST["ltps"]
        credits=request.POST["credits"]

        course =  Course(department=dept,program=program,academicyear=academicYear,semester=semester,year=year,coursecode=coursecode,coursetitle=CourseTitle,ltps=ltps,credits=credits)
        Course.save(course)
        message = "course added succesfully"

        return render(request,"addcourses.html",{"msg":message,"adminuname":auname})

def updatestudent(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    auname = request.session["auname"]

    return render(request, "updatestudent.html", {"coursesdata": courses, "count": count, "adminuname": auname})

def studentupdation(request,studentid):
    auname = request.session["auname"]


    student=get_object_or_404(Student,pk=studentid)
    if request.method =="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.saved()
            return HttpResponse("student updated succesfully")
        else:
            return HttpResponse("student updation failed")
    else:
        form=StudentForm(instance=student)
    return render(request,"studentupdated.html",{"from":form,"adminuname":auname})




def deletecourse(request):
        courses = Course.objects.all()
        count = Course.objects.count()
        auname = request.session["auname"]

        return render(request, "deletecourse.html", {"coursesdata": courses, "count": count,"adminuname":auname})

def coursedeletion(request,courseid):
        Course.objects.filter(id=courseid).delete()

        #return HttpResponse("course deleted successfully")
        return redirect("deletecourse")

def addfaculty(request):
    auname=request.session["auname"]

    form = AddFacultyForm()
    if request.method == "POST":
        form1 = AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            message= "faculty added succesfully"
            #return HttpResponse("faculty added succesfully")

            return render(request,"addfaculty.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message="failed to add faculty data"
            return render(request,"addfaculty.html",{"msg":message,"form":form,"adminuname":auname})




    return render(request,"addfaculty.html",{"form":form,"adminuname":auname})

def deletefaculty(request):
    auname = request.session["auname"]

    faculty = Faculty.objects.all()
    count = Faculty.objects.count()

    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count,"adminuname":auname})


def facultydeletion(request, facultyid):

    Faculty.objects.filter(id=facultyid).delete()

    # return HttpResponse("course deleted successfully")
    return redirect("deletefaculty")

def addstudent(request):
    auname=request.session["auname"]

    form = AddStudentForm()
    if request.method == "POST":
        form1 = AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            message= "student added succesfully"
            #return HttpResponse("faculty added succesfully")
            return render(request,"addstudent.html",{"msg":message,"form":form,"adminuname":auname})
        else:
            message="failed to add student data"
            return render(request,"addstudent.html",{"msg":message,"form":form,"adminuname":auname})




    return render(request,"addstudent.html",{"form":form,"adminuname":auname})

def deletestudent(request):
    auname=request.session["auname"]

    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentsdata":student, "count": count,"adminuname":auname})


def studentdeletion(request, studentid):
    Student.objects.filter(id=studentid).delete()

    # return HttpResponse("course deleted successfully")
    return redirect("deletestudent")

def facultycoursemapping(request):
    facultymappingcourses= FacultyCourseMapping.objects.all()
    print(facultymappingcourses)
    auname=request.session["auname"]

    return render(request,"facultycoursemapping.html",{"adminuname":auname,"facultymappingcourses":facultymappingcourses})
def adminchangepwd(request):
    auname=request.session["auname"]

    return render(request,"adminchangepwd.html",{"adminuname":auname})

def facultylogin(request):
    return render(request,"facultylogin.html")

def studentlogin(request):
    return render(request,"studentlogin.html")

def adminupdatepwd(request):
    auname=request.session["uname"]
    print(auname)
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(auname,opwd,npwd)


    flag=Admin.objects.filter(Q(username=auname)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Admin.objects.filter(username=auname).update(password=npwd)
        print("updated...")
        msg="password updated succesfully"
    else:
        print("old pwd is incorrect")
        msg=" old password is invalid"


    return render(request,"adminchangepwd.html",{"adminuname": auname,"message":msg})

