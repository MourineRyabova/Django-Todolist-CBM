from django.contrib import admin
from todolist.models import Category, TodoList
from rangefilter.filters import DateRangeFilter


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(TodoList)
class TodolistAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "content",
        "created",
        "due_date",
        "category_name",
        "category_id",
    ]

    def category_name(self, obj):
        """Вычисляемое значение для только-читаемого поля."""
        return obj.category.name

    readonly_fields = [
        "category_name",
    ]
    list_filter = [
        ("created", DateRangeFilter),
        ("due_date", DateRangeFilter),
    ]  # фильтры в правой части экрана
    search_fields = ["title", "content"]
