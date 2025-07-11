import random
import string

class PasswordGenerator:
    # DEFAULT CONFIG
    def __init__(self): 
        self.length = 12
        self.use_lowercase = True
        self.use_uppercase = True
        self.use_digits = True
        self.use_special = False
    
    
    # def configure(self, length=12, use_lowercase=True, use_uppercase=True, 
    #               use_digits=False, use_special=False):
    #     self.length = length
    #     self.use_lowercase = use_lowercase
    #     self.use_uppercase = use_uppercase
    #     self.use_digits = use_digits
    #     self.use_special = use_special

    def generate(self):
        char_pool = ""
        
        if self.use_lowercase:
            char_pool += string.ascii_lowercase
        if self.use_uppercase:
            char_pool += string.ascii_uppercase
        if self.use_digits:
            char_pool += string.digits
        if self.use_special:
            char_pool += "!@#$%^&*"
        
        # if all options are DISABLED
        if not char_pool:
            char_pool = string.ascii_letters + string.digits

        password = []
        password.extend(random.choice(char_pool) for _ in range(self.length))

        return ''.join(password)