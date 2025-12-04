from django.urls import path
from ..views.cv_views import CvListCreate, CvDetail

urlpatterns = [
    path("", CvListCreate.as_view(), name="cv-list-create"),
    path("<str:cv_id>/", CvDetail.as_view(), name="cv-detail"),
]
