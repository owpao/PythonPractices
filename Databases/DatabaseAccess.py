from FakerImpl import FakerImpl
import sqlite3


class DBAccess:

    def __init__(self):
        pass

    def main(self):
        fakerImpl = FakerImpl()
        persons = fakerImpl.createPersons(100)
        for person in persons:
            self.insertToDb(person)

    def insertToDb(self, person):
        conn = self.create_connection()
        with conn:
            cursor = conn.cursor()
            sql = "INSERT INTO Person(name, age, address, birthday) VALUES(?,?,?,?)"
            cursor.execute(sql, (person.name, person.age, person.address, person.birthday))

    def create_connection(self):
        try:
            conn = sqlite3.connect(
                "D:\githome\PythonPractices\Databases\sampleDB.db")
            return conn
        except Error as e:
            print(e)
        return None


if __name__ == "__main__":
    dbAccess = DBAccess()
    dbAccess.main()
