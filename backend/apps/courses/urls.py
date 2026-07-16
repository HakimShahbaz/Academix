from django.urls import path

from .views import CourseDetailView, CourseDeleteView, CourseListView, CourseCreateView, CourseUpdateView

app_name = "courses"

urlpatterns = [
    path(
        "",
        CourseListView.as_view(),
        name="course_list"
    ),
    path(
        "create/",
        CourseCreateView.as_view(),
        name="course_create"
    ),
    path(
        "<int:pk>/edit/",
        CourseUpdateView.as_view(),
        name="course_update"
    ),
    path(
        "<int:pk>/delete/",
        CourseDeleteView.as_view(),
        name="course_delete"
    ),
    path(
        "<int:pk>/",
        CourseDetailView.as_view(),
        name="course_detail"
    )

]