import art
from generator import PasswordGenerator
from validator import PasswordValidator


class PasswordGeneratorUI:
    def __init__(self):
        self.generator = PasswordGenerator()
        self.validator = PasswordValidator()
        self.current_length = self.generator.length
        self.current_strength = "..."

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
        while True:
            print("\n========== НАСТРОЙКА ПАРОЛЯ ==========")
            print(f"  [length -> {self.current_length}]  [strength -> {self.current_strength}]")
            print("-------------------------------------")
            print(f"    lowercase [{"+" if self.generator.use_lowercase else "-"}]    uppercase [{"+" if self.generator.use_uppercase else "-"}]")
            print(f"    digits [{"+" if self.generator.use_digits else "-"}]       special [{"+" if self.generator.use_special else "-"}]")
            print("-------------------------------------\n")

            print("[1] GENERATE")
            print("[2] CHANGE LENGTH")
            print("[3] CHANGE CHARACTERS TYPES")
            print("\n[0] BACK")
            choice = input("?> ")
            
            if choice == "1":
                print(f'Password: {self.generator.generate()}')
                input()
            if choice == "2":
                self.change_length()
            if choice == "3":
                self.toggle_character_types()
            if choice == "0":
                break
    

    def change_length(self):
        """Изменение длины пароля"""
        try:
            new_length = int(input("(8-64)> "))
            if 8 <= new_length <= 64:
                self.current_length = new_length
                self.generator.length = new_length

                self.check_current_strength()
            else:
                print("8 - 64")
        except ValueError:
            print("Only 8-64)")

        
    def check_current_strength(self):
        """Генерация текстового пароля для проверки силы"""
        test_password = self.generator.generate()
        self.current_strength = self.validator.validate(test_password)

    
    def toggle_character_types(self):
        while True:
            print(f"lower - {self.generator.use_lowercase}", end=' ')
            print(f"upper - {self.generator.use_uppercase}", end=' ')
            print(f"digit - {self.generator.use_digits}", end=' ')
            print(f"special - {self.generator.use_special}")
            choice = input("l / u / d / s / ENTER>")
            if choice == "l":
                self.generator.use_lowercase = False if self.generator.use_lowercase else True
            elif choice == "u":
                self.generator.use_uppercase = False if self.generator.use_uppercase else True
            elif choice == "d":
                self.generator.use_digits = False if self.generator.use_digits else True
            elif choice == "s":
                self.generator.use_special = False if self.generator.use_special else True
            else:
                self.check_current_strength()
                break

            