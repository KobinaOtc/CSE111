import csv

# Define main

def main():
    # Try and except block for errors
    try:
        user_i_num = input('Please enter an I-Number (xxxxxxxxx): ')
        students = read_dictionary('students.csv', 0)
        print(students[user_i_num])
    except (KeyError, TypeError, IndexError):
        print('No such student')

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    STUDENT_INDEX = 1
    students = {}
    with open(filename, 'rt') as students_doc:
        read_students_doc = csv.reader(students_doc)

        # Skip first line
        next(read_students_doc)

        # Creat dictionary for the students file
        for student in read_students_doc:
            students[student[key_column_index]] = student[STUDENT_INDEX]
    return students


if '__main__' == __name__:
    main()