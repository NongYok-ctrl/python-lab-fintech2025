grades = ["a", "b", "c", "d"]

students = [{'name': 'mark','grades': 'A'},
            {'name': 'john','grades': 'B'},
            {'name': 'mike','grades': 'C'},
            {'name': 'sara','grades': 'D'},
            {'name': 'lisa','grades': 'A'},
            {'name': 'julia','grades':'B'}]
count_a = (1 for x in students if x['grades'] == 'A')
print(len(students))