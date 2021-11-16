from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    path('delete/<task_id>', delete, name='delete'),
    path('task/<task_id>', task, name='task'),
    path('edit/<task_id>', edit, name='edit'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
]