from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Lesson, CourseLesson, Course, Rating


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "is_instructor", "is_staff", "is_active")
    search_fields = ("username", "email", "full_name", "display_name")
    list_filter = ("is_instructor", "is_staff", "is_active")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "instructor", "price", "created_at")
    search_fields = ("title", "description")
    list_filter = ("created_at", "updated_at")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title", "description")


@admin.register(CourseLesson)
class CourseLessonAdmin(admin.ModelAdmin):
    list_display = ("course", "lesson", "order")
    list_filter = ("course",)
    ordering = ("order",)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "rating", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("user__username", "course__title")
