from django.urls import path
from whitecardapp import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('usr_login', views.usr_login, name="usr_login"),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name="home"),
    path('application', views.application, name="application"),
    path('card_status', views.card_status, name="card_status"),
    path('usr_app_del/<int:id>', views.usr_app_del, name="usr_app_del"),
    path('system_admin', views.system_admin, name="system_admin"),
    path('adminapprove/<int:id>', views.adminapprove, name="adminapprove"),
    path('rto', views.rto, name="rto"),
    path('rtoapprove/<int:id>', views.rtoapprove, name="rtoapprove"),
    path('ration', views.ration, name="ration"),
    path('rationapprove/<int:id>', views.rationapprove, name="rationapprove"),
    path('voter', views.voter, name="voter"),
    path('voterapprove/<int:id>', views.voterapprove, name="voterapprove"),
    path('it_return', views.it_return, name="it_return"),
    path('it_return_approve/<int:id>', views.it_return_approve, name="it_return_approve"),
    path('admin_module_create', views.admin_module_create, name="admin_module_create"),
    path('admin_update/<int:id>', views.admin_update, name="admin_update"),
    path('delete_dep', views.delete_dep, name="delete_dep"),
]
