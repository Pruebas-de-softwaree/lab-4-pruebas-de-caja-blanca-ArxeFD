def process_grades(students):
    passed = []
    failed = []
    overall_average = 0
    total_grades = 0
    counter = 0

    for student in students:
        name = student['name']
        grades = student['grades']
        
        if grades == None:  
            print(f"Student {name} has no grades")
            continue
        
        average = sum(grades) / len(grades)
        total_grades += average
        #counter += 1

        if average > 70:  
            passed.append(name)
        elif average >= 50:
            print(f"{name} is in recovery")
        else:
            failed.append(name)
    
    if counter > 0:  
        overall_average = total_grades / counter
    
    return {
        'passed': passed,
        'failed': failed,
        'overall_average': round(overall_average, 2)
    }


if __name__ == "__main__":
    students = [
    {'name': 'Ana', 'grades': [90, 80, 85]},  
    {'name': 'Luis', 'grades': [60, 50, 55]},  
    {'name': 'Marta', 'grades': [20, 40, 30]},
    {'name': 'Jorge', 'grades': None},        
    {'name': 'Test', 'grades': []}           
]




    result = process_grades(students)
    print("\nFinal processing result:")
    print(result)
