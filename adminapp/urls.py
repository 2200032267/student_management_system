from django.urls import path
from . import views
urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome"),

    path("adminlogout",views.logout,name="adminlogout"),
    path("checkadminlogin",views.checkadminlogin,name="checkadminlogin"),

    path("adminchangepwd", views.adminchangepwd, name="adminchangepwd"),
    path("adminupdatepwd", views.adminupdatepwd, name="adminupdatepwd"),


    path("viewstudents",views.viewstudents,name="viewstudents"),

    path("viewfaculty",views.viewfaculty,name="viewfaculty"),
    path("viewcourses",views.viewcourses,name="viewcourses"),
    path("admincourse",views.admincourse,name="admincourse"),
    path("admincourse", views.admincourse, name="admincourse"),
    path("addcourses", views.addcourses, name="addcourses"),
    path("insertcourse", views.insertcourse, name="insertcourse"),
    path("deletecourse", views.deletecourse, name="deletecourse"),
    path("coursedeletion/<int:courseid>", views.coursedeletion, name="coursedeletion"),
    path("updatecourse", views.updatecourse, name="updatecourse"),
    path("courseupdation/<int:courseid>", views.courseupdation, name="courseupdation"),
    path("courseupdated", views.courseupdated, name="courseupdated"),
    path("updatestudent", views.updatestudent, name="updatestudent"),
    path("studentupdation/<int:studentid>", views.studentupdation, name="studentupdation"),

    path("adminstudent",views.adminstudent,name="adminstudent"),
    path("adminfaculty",views.adminfaculty,name="adminfaculty"),
    path("adminfaculty", views.adminfaculty, name="adminfaculty"),
    path("facultylogin", views.facultylogin, name="facultylogin"),
    path("studentlogin", views.studentlogin, name="studentlogin"),

    path("addfaculty/", views.addfaculty, name="addfaculty"),
    path("deletefaculty", views.deletefaculty, name="deletefaculty"),
    path("facultydeletion/<int:facultyid>", views.facultydeletion, name="facultydeletion"),
    path("addstudent/", views.addstudent, name="addstudent"),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("studentdeletion/<int:studentid>", views.studentdeletion, name="studentdeletion"),
    path("facultycoursemapping", views.facultycoursemapping, name="facultycoursemapping"),

]
