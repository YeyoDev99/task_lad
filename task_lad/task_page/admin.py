from django.contrib import admin
from .models import User, Task
from django.contrib.admin import ModelAdmin, StackedInline


class TaskAdmin(ModelAdmin):
    list_display = ('title', 'completion_validation', 'delay_validation')
    list_filter = ['created', 'updated', 'deadline', 'completed']
    search_fields = ['title']


admin.site.register(User)
admin.site.register(Task, TaskAdmin)