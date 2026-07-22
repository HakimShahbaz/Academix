from django.urls import path

from .views import (
    EnrollmentListView, EnrollmentDeleteView, EnrollmentCreateView,
    EnrollmentUpdateView, EnrollmentDetailView
)

app_name = 'enrollments'

urlpatterns = [
    path(
        '',
         EnrollmentListView.as_view(),
        name='enrollment_list',
    ),
    path(
        "<int:pk>/",
        EnrollmentDetailView.as_view(),
        name='enrollment_detail',
    ),
    path(
        "<int:pk>/edit/",
        EnrollmentUpdateView.as_view(),
        name='enrollment_update'
    ),
    path(
        "<int:pk>/delete/",
        EnrollmentDeleteView.as_view(),
        name='enrollment_delete',
    ),
    path(
        "create/",
        EnrollmentCreateView.as_view(),
        name='enrollment_create',
    )
]