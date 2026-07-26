from django.urls import path

from .views import (
    ExamCreateView, ExamListView, ExamDeleteView,
    ExamDetailView, ExamUpdateView
)

from .views import (
    GradeCreateView, GradeListView, GradeDeleteView,
    GradeDetailView, GradeUpdateView
)

app_name = 'exams'

urlpatterns = [
    path(
        '',
        ExamListView.as_view(),
        name='exam_list'),
    path(
        'create/',
        ExamCreateView.as_view(),
        name='exam_create',
    ),
    path(
        '<int:pk>/',
        ExamDetailView.as_view(),
        name='exam_detail',
    ),
    path(
        '<int:pk>/edit/',
        ExamUpdateView.as_view(),
        name='exam_update',
    ),
    path(
        '<int:pk>/delete/',
        ExamDeleteView.as_view(),
        name='exam_delete',
    ),

    path(
        'grades/',
        GradeListView.as_view(),
        name='grade_list',
    ),
    path(
        'grades/create/',
        GradeCreateView.as_view(),
        name='grade_create',
    ),
    path(
        'grades/<int:pk>/',
        GradeDetailView.as_view(),
        name='grade_detail',
    ),
    path(
        'grades/<int:pk>/edit/',
        GradeUpdateView.as_view(),
        name='grade_update',
    ),
    path(
        'grades/<int:pk>/delete/',
        GradeDeleteView.as_view(),
        name='grade_delete',
    )
]