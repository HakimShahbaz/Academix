from django.urls import path
from .views import StudentListView

app_name = "profiles"

urlpatterns = [
    path(
        "students/",
        StudentListView.as_view(),
        name="student_list",
    ),
]