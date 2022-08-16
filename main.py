
import sys
from database_file import manage


class personal:

    def __init__(self):

        self.m1 = manage()
        self.menu()

    def menu(self):
        print(
            """Select from followings numbers to continue :)

                For enter data press 1
                For retrieve data press 2
                For update data press 3
                For delete data press 4
        """)

        choise = int(input("Type your choise: "))
        if choise == 1:
            self.enter()
        elif choise == 2:
            self.retrieve()
        elif choise == 3:
            self.update()
        elif choise == 4:
            self.delete()
        else:
            sys.exit("Invalid input the system shutdown...")

    def enter(self):
        try:
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            gend = input("Enter gender: ")
            addr = input("Enter address: ")
            desig = input("Enter your designation: ")
            depart = input("Enter department name: ")
            print()
        except:
            print("Invalid input")

        res = self.m1.enter1(first_name, last_name, gend, addr, desig, depart)

        if res == 0:
            print("Something went wrongs! Try Again... ")
            self.menu()
        elif res == 1:
            self.menu()

    def retrieve(self):
        id_no = int(input("enter id no to get your data: "))
        print()
        res = self.m1.retrieve2(id_no)
        if res == 0:
            print("Something went wrongs! Try Again... ")
            print()
            self.menu()
        elif res == 1:
            self.menu()

    def update(self):
        try:
            id_no = int(input("enter id no to get your data: "))
            no = int(input("How many fields do you want to be updated from 6 ? "))
        except:
            print("Wrong input..")
            self.menu()
        else:
            for i in range(0, no):
                choise = int(input("""
                    Which field do you want to be update ?
                    Press no accordingly:
                        1.first_name 
                        2.last_name
                        3.Gender 
                        4.Address 
                        5.Desigination 
                        6.Department 
                """))
                print()
                if choise == 1:
                    res = self.m1.update2(id_no, "f_name")
                    if res == 0:
                        print()
                        print(f"The id no: {id_no} is not found... ")
                        self.menu()
                elif choise == 2:
                    res = self.m1.update2(id_no, "l_name")
                    if res == 0:
                        print()
                        print(f"The id no: {id_no} is not found... ")
                        self.menu()
                elif choise == 3:
                    res = self.m1.update2(id_no, "gender")
                    if res == 0:
                        print()
                        print(f"The id no:{id_no} is not found... ")
                        self.menu()
                elif choise == 4:
                    res = self.m1.update2(id_no, "address")
                    if res == 0:
                        print()
                        print(f"The id no:{id_no} is not found... ")
                        self.menu()
                elif choise == 5:
                    res = self.m1.update2(id_no, "designation")
                    if res == 0:
                        print()
                        print(f"The id no:{id_no} is not found... ")
                        self.menu()
                elif choise == 6:
                    res = self.m1.update2(id_no, "department")
                    if res == 0:
                        print()
                        print(f"The id no:{id_no} is not found... ")
                        self.menu()
        self.menu()

    def delete(self):
        a = int(input("Enter id number to delete that data.."))
        res = self.m1.delete2(a)
        if res == 0:
            print()
            print(f"The id no: {a} is not found... ")
            self.menu()
        self.menu()


p1 = personal()
