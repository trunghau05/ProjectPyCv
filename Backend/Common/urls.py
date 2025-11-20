from django.urls import path
from Common.views import seed_cv_data

urlpatterns = [
    path('api/seed/', seed_cv_data, name='seed_cv_data'),
]
