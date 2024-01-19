from django.contrib import admin
from .models import Student
from .models import Teacher

# within this folder there is a file name models from that models file 
# import module name

# Register your student model here so that the model can be seen in 
# admin site 
admin.site.register([Student])
admin.site.register([Teacher])