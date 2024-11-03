def total_salary(path):
    fh = open(path)
    allEmployees = list()
    while True:
        dict = {"name": "", "salary": 0}
        line = fh.readline()
        if not line:
            break
        dict["name"] = line.split(',')[0]
        dict["salary"] = line.split(',')[1]
        allEmployees.append(dict)
    total = 0
    for employee in allEmployees:
        total += int(employee["salary"])
    avarage = total/len(allEmployees)
    return [total, avarage]

total, average = total_salary('salaries.txt')

print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")