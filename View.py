import Connect



class View:

    # Initialization of class View
    def __init__(self, table, records):
        self.table = table
        self.records = records

    # Method that prints the list of DB tables
    @staticmethod
    def list():
        print('''
        1 => school
        2 => classes
        3 => discipline
        4 => teachers
        5 => students
        6 => teachers_discipline
        ''')

    # Method that prints the list of attributes of the selected table
    @staticmethod
    def attribute_list(table):
        if table == 1:
            print('''
            1 => name
            2 => city
            3 => type
            4 => id
            ''')
        elif table == 2:
            print('''
            1 => id
            2 => name
            3 => classroom
            4 => school
            ''')
        elif table == 3:
            print('''
            1 => id
            2 => name
            3 => "number of tests"
            4 => "lessons per week"
            5 => teachers
            ''')
        elif table == 4:
            print('''
            1 => id
            2 => full_name
            3 => numbers
            4 => school
            5 => classes
            ''')
        elif table == 5:
            print('''
            1 => id
            2 => full_name
            3 => phone_number
            4 => cities
            5 => classes
            ''')
        elif table == 6:
            print('''
            1 => id
            2 => teachers
            3 => discipline
            ''')

    # Method that prints content from a selected table
    def show(self):
        print("____________________\n")
        if self.table == 1:
            for row in self.records:
                print("Name = ", row[0])
                print("City = ", row[1])
                print("Type = ", row[2])
                print("ID = ", row[3])
                print("____________________\n")
        elif self.table == 2:
            for row in self.records:
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("Classroom = ", row[2])
                print("school = ", row[3])
                print("____________________\n")
        elif self.table == 3:
            for row in self.records:
                print("ID = ", row[0])
                print("Name = ", row[1])
                print("Number_of_tests = ", row[2])
                print("Lessons_per_week = ", row[3])
                print("Teachers = ", row[4])
                print("____________________\n")
        elif self.table == 4:
            for row in self.records:
                print("ID = ", row[0])
                print("Full_name = ", row[1])
                print("Phone_number = ", row[2])
                print("Cities = ", row[3])
                print("Classes = ", row[4])
                print("____________________\n")
        elif self.table == 5:
            for row in self.records:
                print("ID = ", row[0])
                print("Full_name = ", row[1])
                print("Number = ", row[2])
                print("School = ", row[3])
                print("Classes = ", row[4])

                print("____________________\n")
        elif self.table == 6:
            for row in self.records:
                print("ID = ", row[0])
                print("Teachers = ", row[1])
                print("Discipline = ", row[2])
                print("____________________\n")

# Method that prints the result of select query
    def showSelect(self):
        for row in self.records:
            print("classes_ID = ", row[0])
            print("classes_Name = ", row[1])
            print("classes_Classroom = ", row[2])
            print("classes_School = ", row[3])
            print("school_Name = ", row[4])
            print("school_City = ", row[5])
            print("school_Type = ", row[6])
            print("school_ID = ", row[7])
            print("____________________\n")

    # ----------TASK 4----------

