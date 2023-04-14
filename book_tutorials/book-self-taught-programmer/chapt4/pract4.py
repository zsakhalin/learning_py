print('start')


def sqr():
    """
    input num
    :return: num^2
    """
    num = int(input("enter the num: "))
    return num * num


def str_return(str):
    """
    input and return str
    :param str: string
    :return: str
    """
    return str


def param_test(required1, required2, required3, optional4=1, optional5="not"):
    """
    f represent required and optional parameters
    :param required1: int
    :param required2: int
    :param required3: int
    :param optional4: int, equals 1
    :param optional5: string, equals "not"
    :return: nothing
    """
    print(required1, " ", required2, " ", required3, " ", optional4, ' ', optional5)


def div2(int_num):
    """
    division on 2
    :param int_num: int
    :return: int_num/2
    """
    return int_num/2


def multiply4(int_num: int):
    """
    multiply 4
    :param int_num: int 
    :return: int_num * 4
    """
    return int_num*4


def stringToFloat(str):
    """
    convert string To Float
    :param str: string
    :return: float
    """
    try:
        float(str)
        print("float ", str)
    except ValueError:
        print("cant convert to float")


stringToFloat(input("enter str "))
# num = int(div2(10))
# multiply4(num)
# param_test(10, 2, 3, 90000)
# print("in str_return:")
# print(str_return("string to return"))
# print("in sqr:")
# print(sqr())

print('fin')
