from django.contrib import admin

# Register your models here.
 
from .models import Etudiant
from .models import Teacher
from .models import Exercise
from .models import Membership


 
admin.site.register(Etudiant)
admin.site.register(Teacher)
admin.site.register(Exercise)
admin.site.register(Membership)