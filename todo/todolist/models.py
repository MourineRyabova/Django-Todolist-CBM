from django.db import models
from datetime import datetime
from datetime import date
from django.urls import reverse

class Category(models.Model):  # Таблица категория которая наследует models.Model
    name = models.CharField(
        max_length=100
    )  # varchar.Нам потребуется только имя категории

    class Meta:
        verbose_name = "Category"  # человекочитаемое имя объекта
        verbose_name_plural = (
            "Categories"  # человекочитаемое множественное имя для Категорий
        )

    def rename(self, new):
        return new

    def __str__(self):
        return self.name  # __str__ применяется для отображения объекта в интерфейсе


class TodoList(models.Model):
    is_done = models.BooleanField(default=False, help_text="Выполнено ли дело")
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)  # текстовое поле
    created = models.DateField(auto_now_add=True)  # дата создания
    due_date = models.DateField(editable=True, default=date.today, help_text="Плановое время завершения задачи")  # до какой даты нужно было сделать дело
    completed = models.DateTimeField(null=True, blank=True, default=False, help_text="Фактическое время завершения задачи")
    category = models.ForeignKey(Category, default="general", on_delete=models.PROTECT)  # foreignkey для таблицы категори
    
    # def get_absolute_url(self): # Тут мы создали новый метод
    #       return reverse('todo_detail', args=[int(self.id)])
          #return reverse('todo_detail', kwargs={"pk": int(self.pk)})
    def save(self, *args, **kwargs) -> None:
        if self.is_done:
            self.completed = datetime.now()
            return super().save(*args, **kwargs)
        else:
            self.completed = None
            return super().save(*args, **kwargs)
    def completed_text(self):
        if self.is_done:
            return "Задача выполнена"
        else:
            return "Задача не выполнена"
          
    class Meta:  # используем вспомогательный класс мета для сортировки наших дел
        #ordering = ["-created"]  # сортировка дел по времени их создания
        ordering = ["due_date"]
    def __str__(self):
        return self.title
