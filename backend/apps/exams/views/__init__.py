from .exam import (
    ExamCreateView, ExamListView, ExamDeleteView,
    ExamDetailView, ExamUpdateView
)

from .grade import (
    GradeCreateView, GradeListView, GradeDeleteView,
    GradeDetailView, GradeUpdateView
)

__all__ = [
    'ExamCreateView',
    'ExamListView',
    'ExamDeleteView',
    'ExamDetailView',
    'ExamUpdateView',

    'GradeCreateView',
    'GradeListView',
    'GradeDeleteView',
    'GradeDetailView',
    'GradeUpdateView'
]