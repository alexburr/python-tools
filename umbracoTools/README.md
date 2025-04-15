# umbracoTools

A simple tool to list Umbraco users and their groups from a local Umbraco database

## Execution
`> python umbracoTools.py`

## Example output

```
ID: -1
Username: User Name
Disabled: False
Login: user.name@email.com
Email: user.name@email.com
Language: en-US
Last Login: 01/20/2025 10:17:28 PM
Groups: Administrators, Sensitive data


ID: 1
Username: Named User
Disabled: False
Login: named.user@email.com
Email: named.user@email.com
Language: en-US
Last Login: 09/30/2024 03:36:02 PM
Groups: Editors
```

## Example log
```
2025-04-14 22:05:42,913 | INFO | ...
2025-04-14 22:05:42,913 | INFO | Added file handler umbracoTools.log to logger
2025-04-14 22:05:43,000 | INFO | Found group 1: Administrators
2025-04-14 22:05:43,000 | INFO | Found group 2: Writers
2025-04-14 22:05:43,000 | INFO | Found group 3: Editors
2025-04-14 22:05:43,000 | INFO | Found group 4: Translators
2025-04-14 22:05:43,000 | INFO | Found group 5: Sensitive data
2025-04-14 22:05:43,000 | INFO | Found 5 groups
2025-04-14 22:05:43,005 | INFO | Found user -1: User Name
2025-04-14 22:05:43,005 | INFO | Found user 1: Named User
2025-04-14 22:05:43,005 | INFO | Found 2 users
2025-04-14 22:05:43,007 | INFO | Finding 2 groups for user -1...
2025-04-14 22:05:43,007 | INFO |   Searching 5 groups for group 1...
2025-04-14 22:05:43,007 | INFO |   Searching 5 groups for group 5...
2025-04-14 22:05:43,007 | INFO | Found 2 groups for user -1
2025-04-14 22:05:43,007 | INFO | Finding 1 groups for user 1...
2025-04-14 22:05:43,007 | INFO |   Searching 5 groups for group 3...
2025-04-14 22:05:43,007 | INFO | Found 1 groups for user 1
```