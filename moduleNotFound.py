#import custom_module

import sys

custom_module_path = "C:\Users\user\Desktop\my_module2\modules\custom"

sys.path.append(custom_module_path)

import custom_module

custom_module.hello()

