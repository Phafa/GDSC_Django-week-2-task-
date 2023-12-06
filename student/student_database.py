# a student database the whole program based on 
students = [
    {'name': 'fares', 'age': '19', 'grade': '12', 'favourite color': 'black'},
]

ckeys = int(input('Add(1), view(2), list(3), update(4), delete(5)=>>>>=>>>::: '))

#a functinon to add a new student from user info    
if ckeys == 1:
    def new_adds():
        name = input('Name:')
        age = int(input('Age:'))
        grade = int(input('Grade:'))
        favcolor = str(input('Favourite Color:'))
        add_student = {'name': name, 'age': age, 'grade': grade, 'favourite color': favcolor}
        students.append(add_student)
        print('successfully adde a student')
        print(students)
    new_adds()

 
# to show specific a student by using values
elif ckeys == 2:
    def view_student(key, value):
        for student in students:
            if student['name'] == value:
                return student
            return None

    value = input('search by name:')  
    found_student = view_student('name', value)

    if found_student:
        print('Student:', found_student)
    else:
        print('student not found')
    view_student('name', value)
#to list all of student  
elif ckeys == 3:
    print(students)

#delete a specific student
elif ckeys == 5:
    def find_student_index(key, value):
        for i, student in enumerate(students):
            if student['name'] == value:
                return i
            return None

    value = input('Enter a Name: ')

    student_index = find_student_index("name", value)
    if student_index is not None:
        del students[student_index]
        print('student removed')
        print(students)
    else:
        print('student not found')
    find_student_index('name', value)

#update a specific student database
elif ckeys == 4:
    def student_database(key, value):
        for student in students:
            if student['name'] == value:
                return student
            return None
    
    value = input('Enter a Name: ')

    foundd_student = student_database('name', value)

    if foundd_student:
        new_age = int(input('Enter new age:'))
        new_grade = input('new grade: ')
        new_favcolor = input('new favourite color: ')
        foundd_student['age'] = new_age
        foundd_student['grade'] = new_grade
        foundd_student['favourite color'] = new_favcolor
        print('student info updated')
        print(students)
    else:
        print('student not found')
    student_database('name', value)
else:
    print('wrong command key')




    













    

    










