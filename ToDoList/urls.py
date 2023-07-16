from django.urls import path
from .views import task, detail, create, edit, delete

urlpatterns = [
    path("", task, name='task'),
    path('task/<int:id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('edit/<int:id>/', edit, name='edit'),
    path('delete/<int:id>/', delete, name='delete'),
]
