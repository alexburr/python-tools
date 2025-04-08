GetUmbracoUsers = '''
SELECT id, 
       userDisabled, 
       userName, 
       userLogin, 
       userEmail, 
       userLanguage, 
       lastLoginDate 
  FROM umbracoUser
'''

GetUmbracoUser2UserGroup = '''
SELECT userId,
       userGroupId
  FROM umbracoUser2UserGroup
 WHERE userId = {0}
'''


GetUmbracoUserGroups = '''
SELECT id,
       userGroupAlias,
       userGroupName
  FROM umbracoUserGroup
'''