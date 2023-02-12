from django.shortcuts import (
    render,
    redirect,
)  # для отображения и редиректа берем необходимые классы
from .models import TodoList, Category  # не забываем наши модели
from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django_filters import FilterSet
from django_filters.views import FilterView


def redirect_view(request):
    return redirect("/test_todo/")  # редирект с главной на категории


class CatView(ListView):
    """Представление для отображения списка категорий.
    
    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview
    """

    model = Category
    context_object_name = "categories"
    template_name = "cat_list.html"


class CatAddView(CreateView):
    model = Category
    fields = ["name"]
    # categories = Category.objects.all()
    context_object_name = "categories"
    template_name = "cat_create.html"
    success_url = "/test_cat/"


class ToDoAddView(CreateView):
    model = TodoList
    fields = ["title", "due_date", "category", "is_done"]
    # context_object_name = 'todos'
    template_name = "todo_create.html"
    success_url = "/test_todo/"


class TodoFilter(FilterSet):
    class Meta:
        model = TodoList
        fields = ["category", "is_done"]


class TodoFilterView(FilterView):
    model = TodoList
    context_object_name = "todo_filter"
    filterset_class = TodoFilter
    fields = ["category", "is_done"]
    template_name = "todo_list.html"


class ToDoDetailView(DetailView):
    model = TodoList
    template_name = "todo_detail.html"
    context_object_name = "todo_detail"


class ToDoUpdateView(UpdateView):
    model = TodoList
    fields = ["is_done", "title", "category", "due_date", "completed"]
    template_name = "todo_update.html"
    context_object_name = "todo_edit"
    success_url = "/test_todo/"


class ToDoDeleteView(DeleteView):
    model = TodoList
    context_object_name = "todo_delete"
    success_url = "/test_todo/"
    template_name = "todo_delete.html"
