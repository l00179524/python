"""
directory_utilities.py
By: ishan
Date: 19thdec23
"""

import os, platform


current_working_directory = None

def detect_os()->str:
    # Os detection 
    return platform.system()

def detect_working_directory()->str:
    
    return os.getcwd()

if (__name__ == '__main__'):
    print(f"This module executes as a standalone script")
    
    # This is use to detect the operating system and converting to lower case 
    a = detect_os()
    a = my_os.lower()
    
    # Checking if the os is windows or linux
    if a == "windows":
        print("Your system is Windows")
    elif a == "linux":
        print("Your system is Linux")
    else:
        print(f"Cannot continue, unidentified system = {a}")
        sys.exit()

    
    current_working_directory = detect_working_directory()
    print(f"You are coding in: {current_working_directory}")

else:
    print(f"This module is called {__name__} and is being called by another script")