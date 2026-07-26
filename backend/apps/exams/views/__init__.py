from .exam import (
    ExamCreateView, ExamListView, ExamDeleteView,
    ExamDetailView, ExamUpdateView
)

from .grade import (
    GradeCreateView, GradeListView, GradeDeleteView,
    GradeDetailView, GradeUpdateView
)

EXAM_VIEWS = [
    'ExamCreateView',
    'ExamListView',
    'ExamDeleteView',
    'ExamDetailView',
    'ExamUpdateView',
]

GRADES_VIEWS = [
    'GradeCreateView',
    'GradeListView',
    'GradeDeleteView',
    'GradeDetailView',
    'GradeUpdateView'
]

__all__ = EXAM_VIEWS + GRADES_VIEWS