studentinfo = {
    'name': '',
    'age': None,
    'Fathers Name': '',
    'roll': None,
    'class': None,
    'subjects': []
}

teacher_info = {
    "name": "",
    "age": None,
    'dept': '',
    'salary': None,
    "class": [],
    "subjects": []
}
hr_info = {
    "name": "",
    "age": None,
    'salary': None,
    'dept': '',

}


def record(person_type: str, input_number: int):
    info_list = []
    for _ in range(input_number):
        info = {}

        while True:
            key = input("Enter key (or 'done' to finish): ").strip().lower()
            if key == "done":
                break

            if key == "name":
                value = input(f"Enter {person_type}'s name: ")
            elif key == "age":
                value = int(input("Enter age: "))
            elif key == "salary" and (person_type == "Teacher" or person_type == "HR"):
                value = int(input("Enter salary: "))
            elif key == "roll" and person_type == "Student":
                value = int(input("Enter roll number: "))
            elif key == "class" and person_type == "Student":
                value = int(input("Enter class: "))
            elif key == "father_name" and person_type == "Student":
                value = input("Enter father's name: ")
            elif key == "dept" and (person_type == "Teacher" or person_type == "HR"):
                value = input("Enter department: ")
            elif key == "subjects" and (person_type == "Teacher" or person_type == "Student"):
                subject_input=input("Enter subject name with comma(,)")
                subject_list=subject_input.split(',')
                value=subject_list
                # sub_count = int(input("Total subject choose: "))
                # subject_list = []
                # for _ in range(sub_count):
                #     subject_name = input(f"Enter subject name: ")
                #     subject_list.append(subject_name)
                # value = subject_list
            # elif key=='class' and (person_type=='Teacher'):
            #     teacher_class=int(input("Total class taken: "))
            #     class_list = []
            #     for _ in range(teacher_class):
            #         class_name = input(f"Enter class name: ")
            #         class_list.append(class_name)
            elif key == 'class' and person_type == 'Teacher':
                 class_input = input("Enter classes with comma (,): ")
                 class_list = class_input.split(',')
                 value=class_list
            else:
                print(f"Invalid key '{key}'.")
                continue

            info[key] = value

        info_list.append(info)

    return info_list


persontype = input("enter person type: ")
input_number = int(input(f"how many {persontype} want to entry: "))
record_list = record(persontype, input_number)
print((record_list))
