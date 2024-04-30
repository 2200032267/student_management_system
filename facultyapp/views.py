from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Faculty,FacultyCourseMapping,Course


def facultyhome(request):
    facultyid = request.session["facultyid"]
    return render(request,"facultyhome.html",{"facultyid":facultyid})

def checkfacultylogin(request):
    facultyid = request.POST["facultyid"]
    pwd = request.POST["pwd"]

    flag=Faculty.objects.filter(Q(facultyid=facultyid)&Q(password=pwd))
    print(flag)

    if flag:
        print("login success")
        request.session["facultyid"]=facultyid
        return render(request,"facultyhome.html",{"facultytid":facultyid})
    else:
        msg="login failed"
        return render(request,"facultylogin.html",{"message":msg})
        #return HttpResponse("login failed")
def facultycourses(request):
    facultyid = request.session["facultyid"]


    mappingcourses=FacultyCourseMapping.objects.all()
    facultymappingcourses=[]
    for course in mappingcourses:
        #print(course.faculty.facultyid)
        if(course.faculty.facultyid==int(facultyid)):
            facultymappingcourses.append(course)
    print(facultymappingcourses)
    dir(facultymappingcourses)
    count=len(facultymappingcourses)

    return render(request,"facultycourses.html",{"facultyid":facultyid,"facultymappingcourses":facultymappingcourses,"count":count})

def facultychangepwd(request):
    facultyid=request.session["facultyid"]

    return render(request,"facultychangepwd.html",{"facultyid":facultyid})
def facultyupdatepwd(request):
    facultyid=request.session["facultyid"]
    print(facultyid)
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(facultyid,opwd,npwd)


    flag=Faculty.objects.filter(Q(facultyid=facultyid)&Q(password=opwd))
    if flag:
        print("old pwd is correct")
        Faculty.objects.filter(facultyid=facultyid).update(password=npwd)
        print("updated...")
        msg="password updated succesfully"
    else:
        print("old pwd is incorrect")
        msg=" old password is invalid"


    return render(request,"facultychangepwd.html",{"facultyid": facultyid,"message":msg})

