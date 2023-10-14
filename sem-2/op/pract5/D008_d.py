import os
import time
import traceback
import math
from Oznak_pract.A.A420 import operation

def files():
    try:
        folder_name = "Oznak_pract"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            os.makedirs(folder_name + "/A")
            os.makedirs(folder_name + "/B")
        else:
            print("Exists")
    except Exception as e:
        print("Error:", e)

    try:
        folder_name = "Oznak_pract"
        if os.path.exists(folder_name):
            file_list = os.listdir()
            for file in file_list:
                if file.endswith('.py'):
                    if file.startswith('A'):
                        os.replace(file, folder_name + "/A/" + file)
                    elif file.startswith('B'):
                        os.replace(file, folder_name + "/B/" + file)
        else:
            print("Folder not exists")
    except Exception as e:
        print("Error:", e)


def run():
    folder_name = "Oznak_pract"
    try:
        if os.path.exists(folder_name):
            for root, dirs, files in os.walk(folder_name):
                for file in files:
                    if file.endswith('.py'):
                        print("File:", os.path.join(root, file))
                        with open(os.path.join(root, file), 'r') as f:
                            file_content = f.read()
                            func_name_start = file_content.find('def') + len('def')
                            func_name_end = file_content.find('(', func_name_start)
                            func_name = file_content[func_name_start:func_name_end]
                            print("Func:", func_name)
                            func_params_start = file_content.find('(', func_name_end) + 1
                            func_params_end = file_content.find(')', func_params_start)
                            func_params = file_content[func_params_start:func_params_end].replace(' ', '').replace('\n','')
                            if func_params == "":
                                func_params = []
                            else:
                                func_params = func_params.split(',')
                            print("Par func:", func_params)
                            try:
                                start_time = time.time()
                                exec(file_content)
                                end_time = time.time()
                                print("Time:", round(end_time - start_time, 3), "sek\n")
                            except Exception as e:
                                print("Error:", e)
                                print("Traceback:", traceback.format_exc())
        else:
            print("Folder")
    except Exception as e:
        print("Error:", e)



files()
run()