my_value = ""


def set_value(value):
    global my_value
    my_value = value

def print_value():
    print("my_value: " +my_value)


if __name__ == "__main__":
    set_value("pao")
    print_value()