from db import session
from faker import Faker
from models import Teacher, Group, Student, Subject, Grade   



# Create a Faker instance
fake = Faker()

# Create random data and add it to the existing tables
# Modify the code below to fit your existing tables and relationships
# Example: if you have a 'courses' table instead of 'subjects', replace 'Subject' with 'Course' and adjust relationships accordingly.

# Create random groups
List_groups= ["1A", "1B", "1C"]
groups = [Group(name=gr) for gr in  List_groups]
session.add_all(groups)

# Create random teachers
teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)

# Create random students and assign them to groups
students = [Student(fullname=fake.name(), group_id=fake.random_int(min=1, max=3)) for _ in range(30)]
session.add_all(students)

# Create random subjects (courses) and assign them to teachers
list_subjects=["Math", "Literature", "IT", "Phisics", "Chemistry"]
subjects = [Subject(name=subl, teacher_id=fake.random_int(min=1, max=5)) for subl in list_subjects]
session.add_all(subjects)
session.commit()


students = session.query(Student).all()

subjects = session.query(Subject).all()

# Create random grades for students in subjects (courses)
for student in students:
    for subject in subjects:
        print(student.id, subject.id)
        grades = [Grade(grade=fake.random_int(min=2, max=5),
                        grade_date=fake.date_between(start_date='-1y', end_date='today'),
                        student_id=student.id, subject_id=subject.id) for _ in range(fake.random_int(min=3, max=5))]
        session.add_all(grades)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
