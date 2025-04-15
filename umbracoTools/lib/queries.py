GetUmbracoUserGroups = '''
SELECT id,
       userGroupAlias,
       userGroupName
  FROM umbracoUserGroup
'''


GetUmbracoUsersWithGroups = '''
SELECT umbracoUser.id, 
       umbracoUser.userDisabled, 
       umbracoUser.userName, 
       umbracoUser.userLogin, 
       umbracoUser.userEmail, 
       umbracoUser.userLanguage, 
       umbracoUser.lastLoginDate,
       STRING_AGG(umbracoUser2UserGroup.userGroupId, ', ') WITHIN GROUP (ORDER BY umbracoUser2UserGroup.userGroupId) AS userGroupIds
  FROM umbracoUser,
       umbracoUser2UserGroup
 WHERE umbracoUser2UserGroup.userId = umbracoUser.id
 GROUP BY umbracoUser.id, 
       umbracoUser.userDisabled, 
       umbracoUser.userName, 
       umbracoUser.userLogin, 
       umbracoUser.userEmail, 
       umbracoUser.userLanguage, 
       umbracoUser.lastLoginDate
 ORDER BY umbracoUser.id
'''