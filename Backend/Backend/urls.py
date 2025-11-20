"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Common import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Tạo CV
    path('cv/create/', views.create_cv, name='create_cv'),

    # Cập nhật CV
    path('cv/update/<str:cv_id>/', views.update_cv, name='update_cv'),

    # Xóa CV
    path('cv/delete/<str:cv_id>/', views.delete_cv, name='delete_cv'),

    # Lấy danh sách CV theo user
    path('cv/user/<str:user_id>/', views.get_cvs_by_user, name='get_cvs_by_user'),

    # Xem chi tiết CV
    path('cv/<str:cv_id>/', views.get_cv_detail, name='get_cv_detail'),
]
