CREATE SCHEMA school;

CREATE TABLE school.groups(
group_id SERIAL PRIMARY KEY,
group_name VARCHAR(255) NOT NULL
);


CREATE TABLE school.students(
student_id SERIAL PRIMARY KEY,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL,
group_id INT,
FOREIGN KEY(group_id) REFERENCES school.groups(group_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE school.subjects(
subject_id SERIAL PRIMARY KEY,
subject_title VARCHAR(255) NOT NULL

);

CREATE TABLE school.marks(
mark_id SERIAL PRIMARY KEY,
date DATE,
mark INT,
student_id INT,
subject_id INT,

FOREIGN KEY(student_id) REFERENCES school.students(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(subject_id) REFERENCES school.subjects(subject_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE school.teachers(
teacher_id SERIAL PRIMARY KEY,
first_name VARCHAR(255) NOT NULL,
last_name VARCHAR(255) NOT NULL
);


CREATE TABLE school.subject_teacher(
subject_id INT,
teacher_id INT,
group_id INT,
FOREIGN KEY(subject_id) REFERENCES school.subjects(subject_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(teacher_id) REFERENCES school.teachers(teacher_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY(group_id) REFERENCES school.groups(group_id) ON DELETE CASCADE ON UPDATE CASCADE
);
