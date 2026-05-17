from django.contrib import admin
from .models import ContactMessage, Course, Statistic

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'course_type', 'is_active', 'order']
    list_editable = ['is_active', 'order']

@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['number', 'label', 'order']
    list_editable = ['order']
