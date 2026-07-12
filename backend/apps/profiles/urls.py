from django.urls import path
from .views import StudentListView, StudentCreateView

app_name = "profiles"

urlpatterns = [
    path(
        "students/",
        StudentListView.as_view(),
        name="student_list",
    ),
    path(
        "students/create/",
        StudentCreateView.as_view(),
        name="student_create",
    )
]