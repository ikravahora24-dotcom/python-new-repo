admin_permissions={'read','write','delete','manage_users'}
editor_permissions={'read','write'}

user_permissions=editor_permissions
required_permissions='delete'

if required_permissions in admin_permissions:
    print("access granted!user can perform this action")
else:
    print("access denied!user cannot perform this action")
print("admin permissions:",admin_permissions)
print("editor permissions:",editor_permissions)
print("user permissions:",user_permissions)
    