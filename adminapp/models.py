from django.db import models
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100,blank=False,unique=True)
    password = models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    department_choices = (("CSE(R)","CSE(REGULAR)"),("CSE(H)","CSE(HONOURS)"),("CSIT","CS&IT") )

    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    program_choices = (("BTECH", "BTECH"), ("MTECH", "MTECH"))
    program = models.CharField(max_length=50, blank=False, choices=program_choices)
    academic_choices = (("2023-24","2023-24"),("2022-23","2022-23"))

    academicyear = models.CharField(max_length=20, blank=False,choices=academic_choices)
    semester_choices = (("ODD","ODD"),("EVEN","EVEN"))

    semester = models.CharField(max_length=10, blank=False,choices=semester_choices)
    year = models.IntegerField(blank=False)
    coursecode = models.CharField(max_length=20, blank=False)
    coursetitle = models.CharField(max_length=100, blank=False)
    ltps = models.CharField(max_length=10,blank=False)
    credits = models.FloatField(blank=False)

    class Meta:
        db_table = "course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
        id = models.AutoField(primary_key=True)
        Studentid = models.BigIntegerField(blank=False,unique=True)
        fullname = models.CharField(max_length=20, blank=False)
        gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"),("OTHERS", "OTHERS"))

        gender = models.CharField(max_length=20, blank=False,choices=gender_choices)
        department_choices = (("CSE(R)", "CSE(REGULAR)"), ("CSE(H)", "CSE(HONOURS)"), ("CSIT", "CS&IT"))
        department = models.CharField(max_length=50,blank=False,choices=department_choices)
        program_choices = (("BTECH", "BTECH"), ("MTECH", "MTECH"))
        program = models.CharField(max_length=50, blank=False,choices=program_choices)
        semester_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))

        semester = models.CharField(max_length=10, blank=False,choices=semester_choices)
        year = models.IntegerField(blank=False)
        password = models.CharField(max_length=100,blank=False,default="klu123")
        email = models.CharField(max_length=100,blank=False,unique=True)
        contact = models.CharField(max_length=20,blank=False,unique=True)

        class Meta:
            db_table = "student_table"

        def __str__(self):
             return str(self.Studentid)

class Faculty(models.Model):
         id = models.AutoField(primary_key=True)
         facultyid = models.BigIntegerField(blank=False, unique=True)
         fullname = models.CharField(max_length=20, blank=False)
         gender_choices = (("MALE", "MALE"), ("FEMALE", "FEMALE"), ("OTHERS", "OTHERS"))

         gender = models.CharField(max_length=20, blank=False,choices=gender_choices)
         department_choices = (("CSE(R)", "CSE(REGULAR)"), ("CSE(H)", "CSE(HONOURS)"), ("CSIT", "CS&IT"))

         department = models.CharField(max_length=50, blank=False,choices=department_choices)
         qualification_choices = (("MTECH", "MTECH"), ("PHD", "PHD"))

         qualification = models.CharField(max_length=50, blank=False,choices=qualification_choices)
         designation_choices = (("professor", "professor"), ("asstprofessor", "asstprofessor"))

         designation = models.CharField(max_length=50, blank=False,choices=designation_choices)
         password = models.CharField(max_length=100, blank=False, default="klu123")
         email = models.CharField(max_length=100, blank=False, unique=True)
         contact = models.CharField(max_length=20, blank=False, unique=True)

         class Meta:
            db_table = "faculty_table"

         def __str__(self):
              return str(self.facultyid)
         def __str__(self):
             return str(self.facultyid)

class FacultyCourseMapping(models.Model):
    mappingid=models.AutoField(primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    component_choices = (("L","Lecture"),("T","Tutorial"),("P","Pratical"),("S","Skill"))
    component = models.CharField(max_length=10,blank=False,choices=component_choices)

    type = models.BooleanField(blank=False,verbose_name="Faculty type")
    section = models.IntegerField(blank=False)

    class Meta:
        db_table="FacultyCourseMapping_table"

    def __str__(self):
        return f"{self.course.coursetitle}--{self.faculty.fullname}"



