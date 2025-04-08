import sys
import datetime

from .umbracoUserGroup import umbracoUserGroup

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
        self.groups = []

    
    def to_string(self):
        datetime_format = '%m/%d/%Y %I:%M:%S %p'
        last_login = self.lastLoginDate.strftime(datetime_format)
        
        groups_string = ''
        groups_strings = []

        for group in self.groups:
            inner_group = group[0]
            group_string = inner_group.to_string()
            groups_strings.append(group_string)
        
        groups_string = ', '.join(groups_strings)

        output: str = (f"""
ID: {self.id}
Username: {colors.LightCyan}{self.userName}{colors.ResetAll}
Disabled: {self.userDisabled}
Login: {self.userLogin}
Email: {self.userEmail}
Language: {self.userLanguage}
Last Login: {last_login}
Groups: {groups_string}
""")
        return output


    def set_groups(self, groups):
        for group in groups:
            self.groups.append(group)

    
    def print_user(self):
        print(self.to_string())