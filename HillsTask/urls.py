from django.contrib import admin
from django.urls import path, include
from todolist.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist', include('todolist.urls')),
    path('', index, name='index')
]
