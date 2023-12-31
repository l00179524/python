###########################################Below code is for directory creation ###########################################################
'''
Create Directory
By: Ishan Samant
19 DEC 2023
'''

def create_directory(a_new_dir_name: str) ->bool:
    # Working with try and except
    try:
        # we are creating a new directory below
        os.mkdir(a_new_dir_name)
        return True
    except:
       
        print(f"Error creating directory {a_new_dir_name}")
        return False    