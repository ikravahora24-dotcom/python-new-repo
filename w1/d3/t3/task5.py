default_setting ={
    "Theme" : "light",
    "language" : "English",
    "font_size" :  12,
    "Notification" : True
}
user_setting ={
    "Theme": "Dark",
    "font_size": 16,
    "notifications": False
}
final_setting={**default_setting ,**user_setting}
print("final app setting:",final_setting)