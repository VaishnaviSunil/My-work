
from django.urls import path
from . import views
app_name='venue'
urlpatterns = [
    path('',views.index,name='def') ,
    path('home',views.home,name='hom'),
    path('room',views.fun,name='rom')

]
