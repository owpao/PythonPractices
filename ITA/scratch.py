from SuperClass import SampleSuperClass
import random

papa = "Apolinario"

class SampleClass(SampleSuperClass):
    name = 'pao'

    # constructor
    def __init__(self, name):
        #attribute
        self.name = name
        
        # protected attribute
        self._age = random.randint(1,70)

        # private attribute
        self.__birthday = '11/29/2019'

    # class method
    def get_name(self):
        return self.__birthday

    # class static method
    @staticmethod
    def get_name_of_your_mama():
        print("Shiela")

    # global variables
    def use_global_variable(self):
        global papa # if need to modify global variable, use global keyword
        print(papa)
        papa = "Mabini"
        print(papa)

    # subclass definition of my_method in superclass
    def my_method(self):
        print("my_method")
    
    # use the default definition of an abstract method in superclass
    def use_the_superclass_abstract_method(self):
        super().my_method(None) #super abstract class method
        self.my_method() # subclass definition
    
    # can we add other non abstract methods in abstract superclass?
    def use_the_other_method_in_superclass(slef):
        slef.my_non_abstract_method()

    def overloaded_method(this, mama):
        print("my mama is: "+mama)

    def overloaded_method(this, mama, papa):
        print("my parent's names are: ")


    


# print(SampleClass().get_name())
# SampleClass().get_name_of_your_mama()
# SampleClass().use_global_variable()
x = SampleClass('owpao')
x.use_the_superclass_abstract_method()

# x.use_the_superclass_abstract_method()
# x.use_the_other_method_in_superclass()

# print(x.name)
# print(x._age)
# print(x.get_name())
