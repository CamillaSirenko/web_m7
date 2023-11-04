from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Teacher, Group, Student, Subject, Grade  # Import your models

# Database configuration
DATABASE_URL = 'postgresql://postgres:Roksi2015@localhost:5432/web_d_7hm'

# Create the SQLAlchemy engine and session
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# Create a Faker instance
fake = Faker()

# Create random data and add it to the existing tables
# Modify the code below to fit your existing tables and relationships
# Example: if you have a 'courses' table instead of 'subjects', replace 'Subject' with 'Course' and adjust relationships accordingly.

# Create random groups
groups = [Group(name=fake.word()) for _ in range(3)]
session.add_all(groups)

# Create random teachers
teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
session.add_all(teachers)

# Create random students and assign them to groups
students = [Student(fullname=fake.name(), group_id=fake.random_int(min=1, max=3)) for _ in range(30)]
session.add_all(students)

# Create random subjects (courses) and assign them to teachers
subjects = [Subject(name=fake.word(), teacher_id=fake.random_int(min=1, max=5)) for _ in range(8)]
session.add_all(subjects)

# Create random grades for students in subjects (courses)
for student in students:
    for subject in subjects:
        grades = [Grade(grade=fake.random_int(min=2, max=5),
                        grade_date=fake.date_between(start_date='-1y', end_date='today'),
                        student=student, discipline=subject) for _ in range(fake.random_int(min=3, max=5))]
        session.add_all(grades)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
