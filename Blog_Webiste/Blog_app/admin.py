from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Comment_Reply)