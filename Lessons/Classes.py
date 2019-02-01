class MyClass:
    def sampleMethod1(self): 
        print("Hello world")

    def sampleMethod2(self): 
        name = input("Enter your name: ")
        print("Good day, {0}!".format(name))

    #static methods
    @staticmethod
    def sampleStaticMethod():
        print("This message came from a static method.")

def main():
    myClass = MyClass()
    myClass.sampleMethod1()
    myClass.sampleMethod2()

    MyClass.sampleStaticMethod()

if __name__ == "__main__":
    main()