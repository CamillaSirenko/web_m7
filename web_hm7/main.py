from sqlalchemy import func, desc, select, and_

from conf.models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .select_from(Grade).join(Student).filter(Grade.subject_id == 1).group_by(Student.id).order_by(
        desc('average_grade')).limit(1).all()
    return result


def select_03():
    """
    SELECT
        g.name AS group_name,
        ROUND(AVG(gr.grade), 2) AS average_grade
    FROM groups g
    JOIN students s ON g.id = s.group_id
    JOIN grades gr ON s.id = gr.student_id
    JOIN subjects sub ON gr.subject_id = sub.id
    WHERE sub.name = 'IT' 
    GROUP BY g.name
    ORDER BY average_grade DESC
    """
    result = session.query(
        Group.name.label('group_name'),
        func.round(func.avg(Grade.grade), 2).label('average_grade')
    ).select_from(Group) \
     .join(Student, Group.id == Student.group_id) \
     .join(Grade, Student.id == Grade.student_id) \
     .join(Subject, Grade.subject_id == Subject.id) \
     .filter(Subject.name == "IT") \
     .group_by(Group.name) \
     .order_by(desc('average_grade')) \
     .all()
    return result

def select_04():
    """
    SELECT
        ROUND(AVG(gr.grade), 2) AS overall_average_grade
    FROM grades gr;
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('overall_average_grade')).scalar()
    return result

def select_05():
    """
    SELECT
        sub.name AS subject_name
    FROM subjects sub
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE t.fullname = 'Matthew Rush';
    """
    result = session.query(Subject.name.label('subject_name')) \
        .join(Teacher) \
        .filter(Teacher.fullname == "Matthew Rush").all()
    return result

def select_06():
    """
    SELECT
        s.fullname AS student_name
    FROM students s
    JOIN groups g ON s.group_id = g.id
    WHERE g.name = "1A";
    """
    result = session.query(Student.fullname.label('student_name')) \
        .join(Group) \
        .filter(Group.name =="1A" ).all()
    return result

def select_07():
    """
    SELECT
        s.fullname AS student_name,
        gr.grade AS grade
    FROM grades gr
    JOIN students s ON gr.student_id = s.id
    JOIN groups g ON s.group_id = g.id
    JOIN subjects sub ON gr.subject_id = sub.id
    WHERE g.name = '1C' AND sub.name = 'IT'

    """
    result = session.query(Student.fullname.label('student_name'), Grade.grade.label('grade')) \
        .join(Group).join(Grade).join(Subject) \
        .filter(Group.name == "1A", Subject.name == "IT").all()
    return result


def select_08():
    """
    SELECT
        ROUND(AVG(gr.grade), 2) AS average_grade_by_teacher
    FROM grades gr
    JOIN subjects sub ON gr.subject_id = sub.id
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE t.fullname =  'Matthew Rush';
    """
    result = session.query(func.round(func.avg(Grade.grade), 2).label('average_grade_by_teacher')) \
        .join(Subject).join(Teacher) \
        .filter(Teacher.fullname == "Matthew Rush" ).scalar()
    return result

def select_09():
    """
    SELECT
        sub.name AS subject_name
    FROM subjects sub
    JOIN grades gr ON sub.id = gr.subject_id
    JOIN students s ON gr.student_id = s.id
    WHERE s.fullname = 'Bryan Campbell'
    GROUP BY sub.name;
    """
    result = session.query(Subject.name.label('subject_name')) \
        .join(Grade).join(Student) \
        .filter(Student.fullname == 'Bryan Campbell').group_by(Subject.name).all()
    return result

def select_10():
    """
    SELECT
        sub.name AS subject_name
    FROM subjects sub
    JOIN teachers t ON sub.teacher_id = t.id
    JOIN grades gr ON sub.id = gr.subject_id
    JOIN students s ON gr.student_id = s.id
    WHERE s.fullname = 'Bryan Campbell' AND t.fullname = 'Matthew Rush'
    GROUP BY sub.name;
    """
    result = session.query(Subject.name.label('subject_name')) \
        .join(Teacher).join(Grade).join(Student) \
        .filter(Student.fullname == 'Bryan Campbell', Teacher.fullname =="Matthew Rush") \
        .group_by(Subject.name).all()
    return result


if __name__ == '__main__':
    # print(select_01())
    # print(select_02())
    # print(select_03())
    # print(select_04())
    # print(select_05())
    # print(select_06())
    # print(select_07())
    # print(select_08())
    # print(select_09())
    print(select_10())