# Software Requirements Specification (SRS)

## 1. Introduction

### 1.1 Purpose
Develop a modular, web-based Learning Management System (LMS) 
core that can be adapted to different educational institutions such as universities, 
schools, language institutes, training centers, and corporate learning platforms.

### 1.2 Scope
- Authentication & Authorization
- User management
- Student management
- Teacher management
- Course management
- Enrollment
- Attendance
- Exams
- Grades
- Reports

### 1.3 Goals
- Replace paper-based workflows.
- Centralize academic data.
- Simplify course management.
- Provide a modular and extensible architecture.
- Improve reporting.
- Provide role-based access.
---

## 2. Actors
- Administrator
- Employee
- Teacher
- Student
---

## 3. Functional Requirements
3.1 Authentication:
- Login
- Logout
- Change Password

3.2 Student Management:
- Create Student
- Edit Student
- Archive Student
- Search Student

3.3 Teacher Management:
- Create Teacher
- Assign Courses
- View Schedule

3.4 Course Management:
- Create Course
- Assign Teacher
- Schedule Classes

3.5 Attendance:
- Record Attendance
- View Attendance History

3.6 Exams:
- Create Exam
- Record Scores

3.7 Reports:
- Student Transcript
- Attendance Report
- Financial Report
---

## 4. Non-Functional Requirements
- Responsive UI
- Secure Authentication
- Daily Database Backup
- Role-based Authorization
- Audit Logging (Future)
---

## 5. Business Rules
- A student can enroll in multiple courses.
- A course can have multiple students.
- Every course must have one teacher.
- Attendance is recorded per session.
- Grades cannot exceed the maximum score.
---

## 6. Future Features
- SMS notifications
- Email notifications
- Online payment
- Student portal
- REST API
- Mobile application
- QR-code attendance
- Multi-tenant support
---

## 7. Assumptions
- The system is designed as a generic LMS core.
- Institution-specific features should be implemented as extensions.
- Internet access is required.