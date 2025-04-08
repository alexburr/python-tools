class umbracoUserGroup():
    def __init__(self, id, userGroupAlias, userGroupName):
        self.id = id
        self.userGroupAlias = userGroupAlias
        self.userGroupName = userGroupName


    def to_string(self):
        return f'{self.userGroupName}'