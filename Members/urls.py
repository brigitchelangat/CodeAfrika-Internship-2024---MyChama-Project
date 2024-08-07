from django.urls import path

from . import views


app_name ='Members'
urlpatterns = [
    #member views
    path('', views.member_list,name ='member_list'),
    path('<int:id>/',views.member_details, name ='member_details'),
]