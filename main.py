import subprocess
import os
from datetime import datetime
import re
# from module_1.part_2 import main as m12
# from module_2.part_1 import main as m21
# from module_3.part_1.part_2 import main as m312
# from module_3.part_2.part_1 import main as m321

print("************************************")

while True:
    main_menu_choice = input("a. data load \n"
                             "b. data query \n"
                             "q. exit: \n"
                             )

    if main_menu_choice == 'q':
        break

    if main_menu_choice == 'a':
        # Change directory to module_1/part_2
        os.chdir('module_1/part_2')
        os.system('python main.py')
        # Change directory back to the main directory
        os.chdir('../../')

        # Change directory to module_2/part_1
        os.chdir('module_2/part_1')
        os.system('python main.py')
        # Change directory back to the main directory
        os.chdir('../../')

    elif main_menu_choice == 'b':

        while True:
            query_menu_choice = input("a. data query \n"
                                      "b. data query - get changes in countries \n"
                                      "c. data query - get news and response \n"
                                      "d. data query \n"
                                      "q. back to the previous menu: \n"
                                      )

            if query_menu_choice == 'q':
                break

            if query_menu_choice == 'a':
                pass

            elif query_menu_choice == 'b':
                # Change directory to module_3/part_1/part_2
                os.chdir('module_3/part_1/part_2')
                os.system('python main.py')
                # Change directory back to the main directory
                os.chdir('../../../')

            elif query_menu_choice == 'c':
                # Change directory to module_3/part_2/part_1
                os.chdir('module_3/part_2/part_1')
                os.system('python main.py')
                # Change directory back to the main directory
                os.chdir('../../../')

            elif query_menu_choice == 'd':
                pass

            else:
                print("Invalid Input ")

    else:
        print("Invalid Input ")
