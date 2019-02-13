class Person():
    id = 0

    def __init__(self, name, age, address, birthday):
        self.name = name
        self.age = age
        self.address = address
        self.birthday = birthday

    def __str__(self):
        return "Person object : name {0}, age: {1}, address: {2}, birthday: {3}".format(self.name, self.age, self.address, self.birthday)
    