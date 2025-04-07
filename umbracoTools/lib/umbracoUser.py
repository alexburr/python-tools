import sys
import datetime

sys.path.append('../lib')

from colors import colors

class umbracoUser():
    def __init__(self, id, userDisabled, userName, userLogin, userEmail, userLanguage, lastLoginDate):
        self.id = id
        self.userDisabled = userDisabled
        self.userName = userName
        self.userLogin = userLogin
        self.userEmail = userEmail
        self.userLanguage = userLanguage
        self.lastLoginDate = lastLoginDate

    
    def to_string(self):
        datetime_format = '%m/%d/%Y %I:%M:%S %p'
        last_login = self.lastLoginDate.strftime(datetime_format)
        output: str = (f"""
ID: {self.id}
Username: {colors.LightCyan}{self.userName}{colors.ResetAll}
Disabled: {self.userDisabled}
Login: {self.userLogin}
Email: {self.userEmail}
Language: {self.userLanguage}
Last Login: {last_login}
""")
        return output

    
    def print_user(self):
        print(self.to_string())