from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views

app_name='accounts'

urlpatterns = [
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('bye/',views.ByeView.as_view(),name='bye'),
    path('<username>/upload/',views.upload_material,name='upload'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('uploads',views.self_uploads,name='self_uploads')
]