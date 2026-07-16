from .course import (
    CourseCreateView, CourseUpdateView, CourseListView,
    CourseDeleteView, CourseDetailView
)
from .section import (
    SectionCreateView, SectionListView, SectionUpdateView,
    SectionDeleteView, SectionDetailView
)

__all__ = [
    "CourseCreateView",
    "CourseUpdateView",
    "CourseListView",
    "CourseDeleteView",
    "CourseDetailView",
    "SectionCreateView",
    "SectionUpdateView",
    "SectionListView",
    "SectionDeleteView",
    "SectionDetailView",
]