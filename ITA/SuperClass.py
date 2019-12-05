from abc import ABC, abstractmethod

# ABC is needed to define abstract classes

class SampleSuperClass(ABC):
    @abstractmethod
    def my_method(self, args):
        print("default definition")

    def my_non_abstract_method(self):
        print("hello")