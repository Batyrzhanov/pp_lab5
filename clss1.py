class UpperString():
    def __init__(self):
        self.input_str = " "

    def get_string(self):
        self.input_str = input("Введите строку: ")

    def print_uppercase(self):
        print(self.input_str.upper())

string_m = UpperString()
string_m.get_string()
string_m.print_uppercase()
