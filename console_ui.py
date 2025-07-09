import art
from generator import PasswordGenerator
from validator import PasswordValidator


class PasswordGeneratorUI:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.validator = PasswordValidator()

    def main_menu(self):
        print("opening password manager...")
        while True:
            print(art.logo2)

            print("[1] GENERATE")
            print("[2] STORAGE\n")
            print("[0] EXIT")

            choice = input("> ")

            if choice == "1":
                self.password_setting()
            if choice == "2":
                print("in development...")     # <- THEN ADD
            if choice == "0":
                print("bye")
                break
    

    def password_setting(self):
        print("========== НАСТРОЙКА ПАРОЛЯ ==========")
        strength = self.validator.validate('qwerTY12abcd') #<- ПЕРЕДЕЛАТЬ!!!!
        length = self.generator.length

        self.generator.configure(
            length=length
        )

        while True:
            print(f"[ length -> {length} ]  [ strength -> {strength}]")
            print(f"lowercase [ ] | uppercase [ ] | digits [ ] | special [ ]")

            print("[1] GENERATE")
            print("[2] CHANGE LENGTH")
            print("\n[0] BACK")
            choice = input("?> ")
            
            if choice == "1":
                print(self.generator.generate())
                input()
            if choice == "2":
                length = input("your len: ")
            if choice == "0":
                break
                