from datetime import date
from datetime import datetime

class Person():
    id = 0

    def __init__(self, name, age, address, birthday):
        self.name = name
        self.age = age
        self.address = address
        self.birthday = birthday

    def __init__(self, obj):
        self.id = obj[0]
        self.name = obj[1]
        self.age = obj[2]
        self.address = obj[3]
        self.birthday = obj[4]

    def __str__(self):
        return "Person object : name {0}, age: {1}, address: {2}, birthday: {3}".format(self.name, self.age, self.address, self.birthday)
    
    def getAge(self):
        currentYear = date.today().year
        birthYear = datetime.strptime(self.birthday,'%Y-%m-%d').year
        return currentYear-birthYear
