# import requi9red module
import sys

def print_sys_path(message: str):
    """
    :return: readable, multi-line output of Python Path
    """
    sys_path = ""
    for each_node in sys.path:
        sys_path += str(each_node) + "\n"
    print(f'\n{message}\n{sys_path}')
    return sys_path

# append the path of the
# parent directory
print_sys_path("initial path")
sys.path.append("..")
print_sys_path("after sys.path append ..")

# import method from sibling
# module
from SiblingB.B import methodB

# call method
s = methodB()
print(s)
