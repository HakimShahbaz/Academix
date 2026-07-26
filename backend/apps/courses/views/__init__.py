from .course import (
    CourseCreateView, CourseUpdateView, CourseListView,
    CourseDeleteView, CourseDetailView
)
from .section import (
    SectionCreateView, SectionListView, SectionUpdateView,
    SectionDeleteView, SectionDetailView
)

COURSE_VIEWS = [
    "CourseCreateView",
    "CourseUpdateView",
    "CourseListView",
    "CourseDeleteView",
    "CourseDetailView",
]

SECTION_VIEWS = [
    "SectionCreateView",
    "SectionUpdateView",
    "SectionListView",
    "SectionDeleteView",
    "SectionDetailView",
]

__all__ = COURSE_VIEWS + SECTION_VIEWS