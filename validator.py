
class PasswordValidator:
    def validate(self, password):
        criteria = 0

        if len(password) < 8:
            print("VERY WEAK!")

        criteria += 1 if any(letter.islower() for letter in password) else 0
        criteria += 1 if any(letter.isupper() for letter in password) else 0
        criteria += 1 if any(letter.isdigit() for letter in password) else 0
        criteria += 1 if any(letter in "!@#$%^&*" for letter in password) else 0

        # reliability assessment
        if criteria == 4 and len(password) > 12: return "Excellent"
        elif criteria >= 3: return "Strong"
        elif criteria >=2: return "Medium"
        return "Weak"