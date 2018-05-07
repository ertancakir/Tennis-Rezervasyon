from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('login/',views.loginView, name= 'login'),
    path('register/',views.register, name= 'register'),
    path('datePick/',views.ajaxRequest,name = "ajaxRequest"),
    path('reservation/',views.reservation,name = "reservation"),
    path('admin/',views.adminPanel,name = "adminPanel"),
    path('reservation/<int:res_id>',views.deleteReservation,name = "deleteReservation"),
    path('logoff/',views.logoffSession,name="logoff"),
    path('listRes/',views.getReservation,name = "getReservation"),
]
