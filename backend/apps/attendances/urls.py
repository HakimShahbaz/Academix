from django.urls import path

from .views import (
    AttendanceListView, AttendanceDeleteView, AttendanceCreateView,
    AttendanceDetailView, AttendanceUpdateView
)

app_name = "attendances"

urlpatterns = [
    path(
        "",
        AttendanceListView.as_view(),
        name="attendance_list",
    ),
    path(
        "<int:pk>/delete/",
        AttendanceDeleteView.as_view(),
        name="attendance_delete",
    ),
    path(
        "create/",
        AttendanceCreateView.as_view(),
        name="attendance_create",
    ),
    path(
        "<int:pk>/",
        AttendanceDetailView.as_view(),
        name="attendance_detail",
    ),
    path(
        "<int:pk>/edit/",
        AttendanceUpdateView.as_view(),
        name="attendance_update",
    )
]