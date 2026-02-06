#########################################################################

students = [
    {
        'name': "Mohamed",
        'age': 29,
        'grade': 20,
        'honors': 'Excellent',
        'city': 'Casa',
    },
    {
        'name': "Fatima",
        'age': 24,
        'grade': 18,
        'honors': 'Excellent',
        'city': 'Rabat',
    },
    {
        'name': "Youssef",
        'age': 27,
        'grade': 15,
        'honors': 'Good',
        'city': 'Fès',
    },
    {
        'name': "Salma",
        'age': 22,
        'grade': 13,
        'honors': 'Fairly Good',
        'city': 'Agadir',
    },
    {
        'name': "Amine",
        'age': 30,
        'grade': 17,
        'honors': 'Good',
        'city': 'Tanger',
    },
    {
        'name': "Khadija",
        'age': 25,
        'grade': 19,
        'honors': 'Excellent',
        'city': 'Marrakech',
    },
    {
        'name': "Omar",
        'age': 28,
        'grade': 12,
        'honors': 'Passable',
        'city': 'Oujda',
    },
    {
        'name': "Sara",
        'age': 23,
        'grade': 16,
        'honors': 'Good',
        'city': 'Kenitra',
    },
    {
        'name': "Anas",
        'age': 26,
        'grade': 10,
        'honors': 'Passable',
        'city': 'Tétouan',
    },
    {
        'name': "Imane",
        'age': 21,
        'grade': 14,
        'honors': 'Fairly Good',
        'city': 'El Jadida',
    },
    {
        'name': "Safouan",
        'age': 29,
        'grade': 20,
        'honors': 'Excellent',
        'city': 'Casa',
    }
]

current_name = 'Safouan'

continue_flag = "yes"

print('Hello')

while continue_flag.lower() == "yes":
    print('Add a student       : 1')
    print('Modify a student    : 2')
    print('Delete a student    : 3')
    print('Quit the program    : 4')
    
    try:
        choice = int(input('Enter a choice:  '))
    except ValueError:
        print('Invalid input, please enter a number between 1 and 4.')
        continue
    
    # Add block
    if choice == 1:
        print('Selected: Add')
        name = input('Enter the name: ')
        try:
            age = int(input('Enter the age: '))
        except ValueError:
            print('Invalid age, setting to 0')
            age = 0
        try:
            grade = float(input('Enter the grade: '))
        except ValueError:
            print('Invalid grade, setting to 0.0')
            grade = 0.0
        city = input('Enter the city: ')
        students.append({
            'name': name,
            'age': age,
            'grade': grade,
            'honors': 'Excellent',
            'city': city,
        })
        for i, student in enumerate(students):
            print(f'student : {i} - {student}')
        
    elif choice == 2:
        print('Selected: Modify')
        search_name = input("Type the student's name to modify: ").lower()
        found = False
        for index, s in enumerate(students):
            if s['name'].lower() == search_name:
                found = True
                print('Student to modify:')
                print(f'Name : {s["name"]}')
                print(f'Age  : {s["age"]}')
                print(f'Grade: {s["grade"]}')
                print(f'City : {s["city"]}')
                update_key = input('Choose the key to modify (name - age - grade - city): ').lower()
                if update_key not in ('name', 'age', 'grade', 'city'):
                    print('Invalid key selection.')
                    break
                new_value = input(f'Current value of {update_key}: {s[update_key]}\nEnter the new value: ')
                if update_key == 'age':
                    try:
                        new_value = int(new_value)
                    except ValueError:
                        print('Invalid age value, keeping old value.')
                        new_value = s['age']
                elif update_key == 'grade':
                    try:
                        new_value = float(new_value)
                    except ValueError:
                        print('Invalid grade value, keeping old value.')
                        new_value = s['grade']
                s.update({update_key: new_value})
                break
        if not found:
            print('Student does not exist!')
        print(f'Students: {students}')
        for i, student in enumerate(students):
            print(f'student : {i} - {student}')
        
    elif choice == 3:
        print('Selected: Delete')
        for s in students:
            print(s)
        name_to_delete = input('Type the name of the student to delete: ').lower()
        for index, s in enumerate(students):
            if name_to_delete == str(s['name']).lower():
                print("Are you sure you want to delete this student?")
                print(f'index: {index} - {s}')
                confirm = input('Answer yes or no: ')
                if confirm.lower() == 'yes':
                    removed = students.pop(index)
                    print(f'Student {removed["name"]} removed.')
                break
        for s in students:
            print(s)

    elif choice == 4:
        print('Selected: Quit')
        continue_flag = "no"
        break
    else:
        print('Please enter a number between 1 and 4.')
    
    continue_flag = input('Do you want to continue? yes/no:  ')

for s in students:
    print(s)

print(f'Number of students: {len(students)}')
