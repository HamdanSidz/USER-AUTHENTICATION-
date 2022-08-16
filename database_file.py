
import mysql.connector


class manage:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host="yourhost", user="yourroot", passwd="yourpassword", charset="utf8", database="yourdatabase")
            # print(mydb)
            self.mycursor = self.mydb.cursor()
        except:
            print("NOT CONNECTED TO DATABASE OR ELSE")
        else:
            print()
            print("    Successfully Connected...\n ")

    def enter1(self, first_name, last_name, gend, addr, desig, depart):
        try:
            self.mycursor.execute(
                f"INSERT INTO personal(id,f_name,l_name,address,gender,designation,department) VALUES('NULL','{first_name}','{last_name}','{gend}','{addr}','{desig}','{depart}');")
            self.mydb.commit()
        except:
            return 0
        else:
            print("Data Entered Successfully.")
            print()
            return 1

    def retrieve2(self, id_no):
        try:
            self.mycursor.execute(f"SELECT* FROM personal WHERE id ={id_no};")
            data = self.mycursor.fetchall()
            lis = ["id_no", "First_name", "Last_name",
                   "Address", "Gender", "Designation", "Department"]
            for i in range(len(lis)):
                print(f"{lis[i]}: {data[0][i]}")
            print()
            return 1
        except:
            print()
            print("Not found!...")
            return 0

    def update2(self, id_no, str):
        try:
            self.mycursor.execute(f"SELECT* FROM personal WHERE id ={id_no};")
            data = self.mycursor.fetchall()
            if data[0][0] != id_no:
                pass
            a = input("Enter updation value: ")
            self.mycursor.execute(
                f"UPDATE personal SET {str} = '{a}' WHERE id = {id_no};")
            self.mydb.commit()
        except:
            return 0
        else:
            print("Successfully Updated...")

    def delete2(self, id_no):
        try:
            self.mycursor.execute(f"SELECT* FROM personal WHERE id ={id_no};")
            data = self.mycursor.fetchall()
            if data[0][0] != id_no:
                pass
            self.mycursor.execute(f"DELETE FROM personal WHERE id = {id_no};")
            self.mydb.commit()
        except:
            return 0
        else:
            print("Sucessufully Deleted...")
