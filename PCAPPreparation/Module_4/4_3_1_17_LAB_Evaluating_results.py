from os import strerror
"""Read student scores from file and generate a report. dr_jekyll.txt"""

class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass

students_evaluation = {}

def evaluate_line(line):
    """Split each line of the file"""
    try:
        values = line.split()
        full_name = values[0] + ' ' + values[1]
        points = float(values[2])
        return full_name, points
    except Exception as e:
        raise BadLine(f"This line does not have the correct format: {line}")

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rt')
    line = src.readline()
    if not line:
        raise FileEmpty("No data in file!")
    while True:
        if not line:
            break
        name, score = evaluate_line(line)
        if name in students_evaluation.keys():
            students_evaluation[name] = students_evaluation[name] + score
        else:
             students_evaluation[name] = score
        line = src.readline()
    des = open(srcname + ".report", 'wt')
    for item in sorted(students_evaluation.items()):
        des.write( f'{item[0]:<20}{item[1]:>5.2f}\n')
    print(students_evaluation)
            
except Exception as e:
    print(e)
    exit()	