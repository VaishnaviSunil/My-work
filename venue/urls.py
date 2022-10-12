
from django.urls import path
from . import views
app_name='venue'
urlpatterns = [
    path('',views.index) ,
    path('home',views.index)

]
