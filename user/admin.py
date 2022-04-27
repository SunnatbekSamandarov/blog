from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fields = ['Name','Email','Subject','Message']

admin.site.register(Post,PostAdmin)
