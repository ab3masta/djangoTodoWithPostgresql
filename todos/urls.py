from django.urls import path, include
from .views import list_todo_items, insert_todo_item, delete_todo_item
urlpatterns = [
    path('', list_todo_items),
    path('insert_todo/', insert_todo_item, name='insert_todo_item'),
    path('delete_todo/<int:todo_id>/', delete_todo_item, name='delete_todo_item'),

]
