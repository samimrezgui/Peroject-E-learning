from django.contrib import admin

# Register your models here.
 
from .models import Student
from .models import Teacher
from .models import Exercise
from .models import individual_Assignment
from .models import Cours
from .models import Group
from .models import EnrollmentP
from .models import Test
from .models import Group_Assignment



 
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Exercise)
admin.site.register(individual_Assignment)
admin.site.register(Cours)
admin.site.register(Group)
admin.site.register(Enrollment)
admin.site.register(Test)
admin.site.register(Group_Assignment)
 