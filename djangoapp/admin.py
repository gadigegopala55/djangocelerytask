from atexit import register
from django.contrib import admin
from .models import blog, comments, subscribers,useradmin

# Register your models here.
admin.site.register(blog)
admin.site.register(useradmin)
admin.site.register(subscribers)
admin.site.register(comments)