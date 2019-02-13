from faker import Faker
from Person import Person
import random
import sys

class FakerImpl:
    # def __init__(self):
    #     pass

    def createPerson(self):
        fake = Faker()        
        fakePerson = Person(fake.name(),random.randint(18,70),fake.address(),fake.date())
        return fakePerson
    
    def createPersons(self, numberOfPersons):
        persons = []
        ctr = 0
        for _ in range(numberOfPersons):
            ctr+=1
            person = self.createPerson()
            persons.append(person)
            sys.stdout.write("\r%s\r" % "Person # {0}/{1} created.".format(ctr,numberOfPersons))
            sys.stdout.flush()
            
        return persons
