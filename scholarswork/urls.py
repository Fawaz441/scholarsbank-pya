"""scholars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.HomePage.as_view(),name='index'),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('schools/',views.SchoolListView.as_view(),name='schools'),
    path('schools/add/', views.SchoolCreateView.as_view(), name='add_school'),
    path('materials',views.Materials.as_view(),name='materials'),
    url('schools/(?P<slug>[-\w]+)/courses/$',views.SchoolCourseListView.as_view(),name='course_list'),
    url('schools/(?P<slug>[-\w]+)/courses/(?P<pk>\d+)/download/$',views.download,name='get'),
    path('approve/<pk>',views.material_approve,name='approve_material'),
    path('approve/<pk>',views.coursefile_approve,name='approve_pq'),
    path('admin_materials',views.adminmaterials,name='admin_materials'),
    path('admin_pqs',views.adminpqs,name='admin_pqs'),
    path('adverts/',views.adverts,name='adverts'),
    path('products/<pk>/detail',views.ProductDetail.as_view(),name='product_detail'),
    path('adverts/clothes/',views.ClothesView.as_view(),name='clothes'),
    path('approve/<pk>', views.coursefile_approve, name='approve_coursefile')]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


