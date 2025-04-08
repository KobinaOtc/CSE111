import csv

# Define main
def main():
    try:
        i_number = input('Please enter an I-Number (xxxxxxxxx): ')
        student = read_dictionary('students.csv')
        new_i_number = i_number.replace('-', '')
        
        if len(new_i_number) == 9:
            print(student[new_i_number])
        elif len(new_i_number) < 9:
            print('Invalid I-Number: too few digits')
        elif len(new_i_number) > 9:
            print('Invalid I-Number: too many digits')
        else:
            print('Invalid I-Number')
        
    except (KeyError, ValueError, IndexError):
        print('No such student')


def read_dictionary(filename):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    ID_INDEX = 0
    STUDENT_INDEX = 1
    students = {}
    with open(filename, 'rt') as student_doc:
        file = csv.reader(student_doc)
        # Skip first line in file
        next(file)
        # For loop for creating student dirctory
        for student in file:
            # store in students dictionary and 
            # make the student ID's the key and the  
            # full names the value
            students[student[ID_INDEX]] = student[STUDENT_INDEX]
    # Return the student with the right key value
    return students



if '__main__' == __name__:
    main()