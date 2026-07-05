# Entity Relationship Design (ERD)

## Overview

This document describes the initial domain model of the Academix project.

The goal is to define the core entities and their relationships before implementation. The design intentionally focuses only on the minimum set of entities required for the first development phase. Institution-specific features are excluded and will be introduced as extensions when necessary.

---

# Core Entities

| Entity          | Purpose                                    |
| --------------- | ------------------------------------------ |
| User            | Authentication and common user information |
| StudentProfile  | Student-specific information               |
| TeacherProfile  | Teacher-specific information               |
| EmployeeProfile | Employee-specific information              |
| Course          | Reusable educational course                |
| Class           | A scheduled offering of a course           |
| Enrollment      | Student enrollment in a class              |

---

# Entity Details

## User

Represents every authenticated person in the system.

Examples:

* Student
* Teacher
* Employee
* Administrator

Authentication and shared user information are stored in this entity.

---

## StudentProfile

Stores information specific to students.

Examples:

* Student Number
* Initial Enrollment Date

Uses a One-to-One relationship with the User model.

---

## TeacherProfile

Stores information specific to teachers.

Examples:

* Employee Number
* Hire Date
* Specialization

Uses a One-to-One relationship with the User model.

---

## EmployeeProfile

Stores information specific to employees.

Examples:

* Employee Number
* Department
* Hire Date

Uses a One-to-One relationship with the User model.

---

## Course

Represents a reusable educational course.

Examples:

* Python Basics
* English A1
* Database Fundamentals

A Course does not represent a scheduled class.

---

## Class

Represents a specific offering of a Course.

Examples:

* Python Basics – Morning
* Python Basics – Evening

Each Class belongs to one Course and is taught by one Teacher.

---

## Enrollment

Represents the enrollment of a student in a Class.

This entity allows future expansion by storing information such as enrollment date, status, notes, or final result.

---

# Relationships

| Source         | Relationship | Target          |
| -------------- | ------------ | --------------- |
| User           | One-to-One   | StudentProfile  |
| User           | One-to-One   | TeacherProfile  |
| User           | One-to-One   | EmployeeProfile |
| Course         | One-to-Many  | Class           |
| TeacherProfile | One-to-Many  | Class           |
| StudentProfile | One-to-Many  | Enrollment      |
| Class          | One-to-Many  | Enrollment      |

---

# Design Decisions

* Authentication is handled by the User model.
* Student, Teacher, and Employee contain only role-specific information.
* Course represents reusable educational content.
* Class represents one scheduled offering of a Course.
* Enrollment is modeled as an independent entity instead of a simple many-to-many relationship to support future extensions.
* The initial design favors simplicity while allowing future growth.

---

# Future Extensions

The following entities are intentionally excluded from Version 1:

* Session
* Attendance
* Assessment
* Grade 
* Announcement
* Payment
* Notification
* Certificate
* QR Code Attendance

These entities will be introduced when their corresponding modules are implemented.
