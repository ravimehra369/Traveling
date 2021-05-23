
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='serveces'),
    path('contact', views.contact, name='contact'),


]
