from FakerImpl import FakerImpl
import sqlite3
import sys
from Person import Person

class DBAccess:

    def __init__(self):
        pass

    def main(self):
        fakerImpl = FakerImpl()
        persons = fakerImpl.createPersons(200)
        for person in persons:
            self.insertToDb(person)

    def insertToDb(self, person):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = "INSERT INTO Person(name, age, address, birthday) VALUES(?,?,?,?)"
            cursor.execute(sql, (person.name, person.age,
                                 person.address, person.birthday))

    def create_connection(self):
        try:
            conn = sqlite3.connect(
                "D:\githome\PythonPractices\Databases\sampleDB.db")
            return conn
        except Error as e:
            print(e)
        return None

    def retrieveDataFromDB(self):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM PERSON"
            cursor.execute(sql)
            return(cursor.fetchall())

    def retrieveDataFromDBByID(self,id):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = "SELECT * FROM PERSON WHERE ID = ?"
            cursor.execute(sql,id)
            person = cursor.fetchone()
            return person

    def updateDataAgeById(self, id, age):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = '''UPDATE PERSON SET AGE = ? WHERE ID = ?'''
            cursor.execute(sql,(age,id))
        print("Age Updated!")

    def deleteDataByLowerThanAge(self, age):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = '''DELETE FROM PERSON WHERE AGE < ?'''
            cursor.execute(sql, (age,))


if __name__ == "__main__":
    dbAccess = DBAccess()
    # dbAccess.main()
    dbAccess.deleteDataByLowerThanAge("18")