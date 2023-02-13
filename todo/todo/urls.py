"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf.urls import url
from django.urls import include, re_path, path
from django.contrib import admin
from todolist.views import (
    redirect_view,
    CatView,
    CatAddView,
    ToDoAddView,
    TodoFilterView,
    ToDoDetailView,
    ToDoUpdateView,
    ToDoDeleteView,
)


urlpatterns = [
    re_path(r"$^", redirect_view),
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^test_cat/", CatView.as_view()),
    re_path(r"^test_cat_add/", CatAddView.as_view()),
    re_path(r"^test_todo/", TodoFilterView.as_view()),  
    re_path(r"^test_todo_add/", ToDoAddView.as_view()),
    path("test_todo_update/<int:pk>/", ToDoUpdateView.as_view(), name="todo_edit"),
    path("test_todo_detail/<int:pk>/", ToDoDetailView.as_view(), name="todo_detail"),
    path("test_todo_delete/<int:pk>/", ToDoDeleteView.as_view(), name="todo_delete"),
]
