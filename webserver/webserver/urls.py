from django.contrib import admin
from django.urls import path
from shopapp import views  # import your view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # root URL
]

