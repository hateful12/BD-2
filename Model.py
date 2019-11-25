import random
import Connect
from View import View

tables = {
    1: 'school',
    2: 'classes',
    3: 'discipline',
    4: 'teachers',
    5: 'students',
    6: 'teachers_discipline',
}

# Data for randomization School table
name = 'name'
city = 'city'
type = 'type'
randomSchool = {
    name: {
        1: 'School №1',
        2: 'School №2',
        3: 'School №3',
        4: 'School №4',
        5: 'School №5',
        6: 'School №6',
        7: 'School №7',
        8: 'School №8',
        9: 'School №9',
        10: 'School №10',
    },
    city: {
        1: 'Київ',
        2: 'Львів',
        3: 'Одеса',
        4: 'Харків',
        5: 'Житомир',
        6: 'Івано-Франківськ',
        7: 'Тернопіль',
        8: 'Херсон',
        9: 'Миколаїв',
        10: 'Суми',
    },
    type: {
        1: 'lyceum',
        2: 'school',
    },
}


class Model:
    # Method that checks valid of the number of table that user input and returns it
    @staticmethod
    def validTable():
        incorrect = True
        while incorrect:
            table = input('Choose table number => ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 6:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')
        return table

        # Method that prints all table of DB

    @staticmethod
    def showAllTables():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        for table in range(1, 7):
            table_name = '''"''' + tables[table] + '''"'''
            print(tables[table])

            show = 'select * from public.{}'.format(table_name)

            print("SQL query => ", show)
            print('')
            cursor.execute(show)
            records = cursor.fetchall()
            obj = View(table, records)
            obj.show()
        cursor.close()
        Connect.closeConnect(connect)

        # Method that prints one table

    @staticmethod
    def showOneTable():
        View.list()
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        table = Model.validTable()

        table_name = '''"''' + tables[table] + '''"'''
        print(tables[table])

        show = 'select * from public.{}'.format(table_name)

        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    @staticmethod
    def insert():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                scname = input("Name = ")
                sccity = input("City = ")
                sctype = input("Type = ")
                scid = input('ID = ')

                insert = 'insert into "school" ("name", "city", "type", "id") values ({}, {}, {}, {})'.format(
                    scname, sccity, sctype, scid)

                restart = False
            elif table == 2:
                clid = input('ID = ')
                clname = input('Name = ')
                clclassroom = input('Classroom = ')
                clschool = input('School = ')

                insert = 'insert into "classes" ("id", "name", "classroom", "school") values ({}, {}, {}, {}, {}, {})'.format(
                    clid, clname, clclassroom, clschool)

                restart = False
            elif table == 3:
                diid = input('ID = ')
                diname = input('Name = ')
                dinumberoftests = input('Number_of_tests = ')
                dilessonsperweek = input('Lessons_per_week = ')
                diteachers = input('Teachers = ')

                insert = 'insert into "discipline" ("id", "name", ""number of tests"", ""lessons per week"", "teachers") values ({}, {}, {})'.format(
                    diid, diname,
                    dinumberoftests, dilessonsperweek, diteachers)

                restart = False
            elif table == 4:
                teid = input('ID = ')
                tefull_name = input('Full_name = ')
                tenumber = input('Number = ')
                teschool = input('School = ')
                teclasses = input('Classes = ')

                insert = 'insert into "teachers" ("id", "full_name", "number", "school", "classes") values ({}, {}, {})'.format(
                    teid, tefull_name, tenumber, teschool, teclasses)

                restart = False
            elif table == 5:
                stid = input('ID = ')
                stfull_name = input('Full_name = ')
                stphone_number = input('Number = ')
                stcities = input('School = ')
                stclasses = input('Classes = ')

                insert = 'insert into "students" ("id", "full_name", "phone_number", "cities", "classes") values ({}, {}, {})'.format(
                    stid, stfull_name, stphone_number, stcities, teclasses)

                restart = False
            elif table == 6:
                tdid = input('ID = ')
                tdteachers = input('Teachers = ')
                tddiscipline = input('Discipline = ')

                insert = 'insert into "teachers_discipline" ("id", "teachers", "discipline") values ({}, {}, {})'.format(
                    tdid, tdteachers, tddiscipline)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print('SQl query => ', insert)
        cursor.execute(insert)
        connect.commit()
        print('Data added successfully!')
        cursor.close()
        Connect.closeConnect(connect)

# ----------TASK 1----------Deleting data from DB

    # Method that deletes data from DB
    @staticmethod
    def delete():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()

            if table == 1:
                scname = input('Attribute to delete name = ')
                delete = 'delete from "school" where "name"= {}'.format(scname)
                restart = False
            elif table == 2:
                clname = input('Attribute to delete name = ')
                delete = 'delete from "classes" where "name"=  {}'.format(clname)
                restart = False
            elif table == 3:
                dsname = input('Attribute to delete name = ')
                delete = 'delete from "discipline" where "name"= {}'.format(dsname)
                restart = False
            elif table == 4:
                tsfull_name = input('Attribute to delete Full_name = ')
                delete = 'delete from "teachers" where "full_name"= {}'.format(tsfull_name)
                restart = False
            elif table == 5:
                stfull_name = input('Attribute to delete Full_name = ')
                delete = 'delete from "students" where "full_name"=  {}'.format(stfull_name)
                restart = False
            elif table == 6:
                tdid = "'" + input('Attribute to delete PsNumber = ') + "'"
                delete = 'delete from "teachers_discipline" where "id"=  {}'.format(tdid)
                restart = False
            elif table == 7:
                rsname = "'" + input('Attribute to delete RsName = ') + "'"
                delete = 'delete from "Restaurant" where "RsName"= {}'.format(rsname)
                restart = False
            elif table == 8:
                trname = "'" + input('Attribute to delete TrName = ') + "'"
                delete = 'delete from "Transport" where "TrName"= {}'.format(trname)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", delete)
        cursor.execute(delete)
        connect.commit()
        print('Data deleted successfully!')
        cursor.close()
        Connect.closeConnect(connect)

# ----------TASK 1----------Updating data in DB

    # Method that updates data in DB
    @staticmethod
    def update():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                scname = "'" + input('Attribute to update(where) name = ') + "'"
                View.attribute_list(1)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"name"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"city"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"type"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "school" set {} where "name"= {}'.format(set, scname)
                restart = False
                pass
            elif table == 2:
                clname = "'" + input('Attribute to update(where) name = ') + "'"
                View.attribute_list(2)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"Name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"Classroom"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"School"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "classes" set {} where "name"= {}'.format(set, clname)
                restart = False
                pass
            elif table == 3:
                diname = "'" + input('Attribute to update(where) Name = ') + "'"
                View.attribute_list(3)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"Name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"Number of tests"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"Lessons per week"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"Teachers"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "discipline" set {} where "name"= {}'.format(set, diname)
                restart = False
                pass
            elif table == 4:
                tename = input('Attribute to update(where) Full_name = ')
                View.attribute_list(4)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"Full_name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"Number"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"School"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"Classes"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "teachers" set {} where "full_name"= {}'.format(set, tename)
                restart = False
                pass
            elif table == 5:
                stname = input('Attribute to update(where) Full name = ')
                View.attribute_list(5)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"Full_name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"Phone_number"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"Cities"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"Classes"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "students" set {} where "full_name"= {}'.format(set, stname)
                restart = False
                pass
            elif table == 6:
                dtname = "'" + input('Attribute to update(where) ID = ') + "'"
                View.attribute_list(6)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"ID"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"Teachers"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"Discipline"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "teachers_discipline" set {} where "id"= {}'.format(set, dtname)
                restart = False
                pass
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", update)
        cursor.execute(update)
        connect.commit()
        print('Data updeted successfully!')
        cursor.close()
        Connect.closeConnect(connect)
        pass

    # ----------TASK 3----------

    # Method that selects data from DB
    @staticmethod
    def select():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        print('''
        In my variant you can select range.

        ''')
        print('You may enter integer range:')
        a = input('')
        b = input('')

        select = """
        select * from "classes" 
        join "school" on "school"."id" = "classes"."school" 
        where {}<school.id and school.id<{};
        """.format(a, b)

        print("SQL query => ", select)
        cursor.execute(select)
        records = cursor.fetchall()
        obj = View(5, records)
        obj.showSelect()

        print('Data selected successfully!')
        cursor.close()
        Connect.closeConnect(connect)

# Method that runs full text search in DB
    @staticmethod
    def text_search():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            text = "'" + input('Search text = ') + "'"
            incorrect = True
            while incorrect:
                mode = input('''
                1 -- Word is not included
                2 -- Required word entry
                Choose mode = > ''')
                if mode.isdigit():
                    mode = int(mode)
                    if mode >= 1 and mode <= 2:
                        incorrect = False
                    else:
                        print('Incorrect input, try again.')
                else:
                    print('Incorrect input, try again.')

            if mode == 1:
                if table == 1:
                    text_search = 'select * from "school" where not (to_tsvector("name") @@ plainto_tsquery({}))'.format(
                        text)
                    restart = False
                elif table == 2:
                    text_search = 'select * from "classes" where not (to_tsvector("name") @@ plainto_tsquery({}))'.format(
                        text)
                    restart = False
                elif table == 3:
                    text_search = 'select * from "discipline" where not (to_tsvector("name") @@ plainto_tsquery({}))'.format(
                        text)
                    restart = False
                elif table == 4:
                    text_search = 'select * from "teachers" where not (to_tsvector("full_name") @@ plainto_tsquery({}))'.format(
                        text)
                    restart = False
                elif table == 5:
                    text_search = 'select * from "students" where not (to_tsvector("full_name") @@ plainto_tsquery({}))'.format(
                        text)
                    restart = False
                else:
                    print('\nIncorrect input, try again.')
            elif mode == 2:
                if table == 1:
                    text_search = 'select * from "school" where to_tsvector("name") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 2:
                    text_search = 'select * from "classes" where to_tsvector("name") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 3:
                    text_search = 'select * from "discipline" where to_tsvector("name") @@ plainto_tsquery({})'.format(text)
                    restart = False
                elif table == 4:
                    text_search = 'select * from "teachers" where to_tsvector("full_name") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                elif table == 5:
                    text_search = 'select * from "students" where to_tsvector("full_name") @@ plainto_tsquery({})'.format(
                        text)
                    restart = False
                else:
                    print('\nIncorrect input, try again.')
            else:
                print('\nIncorrect input, try again.')

        print(tables[table])
        print('SQL query => ', text_search)
        cursor.execute(text_search)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        print('Data searched successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    # ----------TASK2----------

    # Method that randoms data into Client table
    @staticmethod
    def random():
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        incorrect = True
        while incorrect:
            num = input('How many schools to random? => ')
            if num.isdigit():
                num = int(num)
                if num >= 1:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')

        for i in range(1, num + 1):
            randomName = "'" + randomSchool[name][random.randint(1, 10)] + "'"
            randomCity = "'" + randomSchool[city][random.randint(1, 10)] + "'"
            randomType = "'" + randomSchool[type][random.randint(1, 2)] + "'"
            insert = 'insert into "school" ("name", "city", "type", "id") values ({}, {}, {}, DEFAULT)'.format(
                randomName, randomCity, randomType)

            print("SQL query => ", insert)
            cursor.execute(insert)
            connect.commit()

        print('Data randomed successfully!')
        cursor.close()
        Connect.closeConnect(connect)