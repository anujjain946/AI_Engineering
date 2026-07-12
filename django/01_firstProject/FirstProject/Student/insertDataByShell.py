'''
Step 1: Open Django Shell
    python manage.py shell

Step 2: Import Models
    from student.models import Department, Course, Student

    
step 3:Insert Department
    
    d1 = Department(name='Computer Science', dec_code='CS', description='Department of Computer Science')
    d1.save()

    d2 = Department(name='Mathematics', dec_code='MATH', description='Department of Mathematics')
    d2.save()

    d3 = Department(name='Physics', dec_code='PHY', description='Department of Physics')
    d3.save()

step 4: Insert Course
    c1 = Course(name='Data Structures', course_code='CS101', description='Introduction to Data Structures', department=d1)
    c1.save()

    c2 = Course(name='Calculus', course_code='MATH101', description='Introduction to Calculus', department=d2)
    c2.save()

    c3 = Course(name='Quantum Mechanics', course_code='PHY101', description='Introduction to Quantum Mechanics', department=d3)
    c3.save()

step 5: Insert Student
    s1 = Student(name='Alice', student_code='S001', email='alice@example.com', course=c1)
    s1.save()

    s2 = Student(name='Bob', student_code='S002', email='bob@example.com', course=c2)
    s2.save()

    s3 = Student(name='Charlie', student_code='S003', email='charlie@example.com', course=c3)
    s3.save()

'''

from Student.models import Department, Course, Student
'''
dept = Department.objects.create(
    name="Computer Science",
    dec_code="CS",
    description="Computer Science Department"
)

course = Course.objects.create(
    name="Python Django",
    course_code="DJ01",
    description="Django Framework",
    department=dept
)

student = Student.objects.create(
    name="Anuj Jain",
    student_code="ST001",
    email="anuj@gmail.com",
    course=course
)
'''
print(Department.objects.all())
print(Course.objects.all())
print(Student.objects.all())

