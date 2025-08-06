"""


# Training System Project Overview

The `Sources/oop/training_system_project` is a comprehensive object-oriented training management
system designed to handle student enrollment, course management, and grade tracking.

## Project Structure

The project follows a clean modular architecture with separate packages for core business logic
and data models [1](#0-0) . The main components include:

- **Core Package**: Contains the `SystemManager` class that handles all business operations [2](#0-1) 
- **Model Package**: Contains data model classes `Student` and `Course` [3](#0-2) [4](#0-3) 
- **Main Interface**: Console-based user interface for system interaction [5](#0-4) 

## Key Features

### Student Management
- **Add Students**: Create new student records with auto-generated IDs [6](#0-5) 
- **Remove Students**: Delete students only if they have no active course enrollments [7](#0-6) 
- **Student Data**: Each student maintains grades dictionary and enrolled courses list [8](#0-7) 

### Course Management
- **Add Courses**: Create new courses with auto-incremented IDs [9](#0-8) 
- **Remove Courses**: Delete courses only when no students are enrolled [10](#0-9) 
- **Course Search**: Find courses by name with case-insensitive matching [11](#0-10) 

### Enrollment & Grading
- **Student Enrollment**: Enroll students in courses with duplicate prevention [12](#0-11) 
- **Grade Recording**: Record student grades for specific courses [13](#0-12) 

### Data Retrieval
- **List All Students**: Retrieve complete student roster [14](#0-13) 
- **List All Courses**: Retrieve complete course catalog [15](#0-14) 

## User Interface

The system provides a menu-driven console interface with 10 main options for system interaction [16](#0-15) .
The interface includes dedicated functions for each operation, such as adding students, managing courses, and
recording grades [17](#0-16) .

## Testing & Development

The project includes a Jupyter notebook for testing and development purposes, containing prototype implementations
and experimental code [18](#0-17) .

## Notes

This training system demonstrates solid object-oriented programming principles with clear separation of concerns
between data models and business logic. The system uses auto-incrementing IDs for both students and courses, 
maintains referential integrity by preventing deletion of entities with dependencies, and provides comprehensive
CRUD operations for educational management. However, there are some implementation issues in the codebase, such 
as bugs in the grade recording system where only the last grade is stored rather than maintaining a complete
grade history, and some inconsistencies in the Jupyter notebook implementations compared to the main codebase.
"""
