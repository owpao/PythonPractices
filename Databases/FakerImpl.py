from faker import Faker
from Person import Person
import random

class FakerImpl:
    # def __init__(self):
    #     pass

    def createPerson(self):
        fake = Faker()        
        fakePerson = Person(fake.name(),random.randint(18,70),fake.address(),fake.date())
        return fakePerson
    
    def createPersons(self, numberOfPersons):
        persons = []
        for _ in range(numberOfPersons):
            persons.append(self.createPerson())
        return persons
