"""
使用二叉树表示二元表达式
"""

# 下面定义几个表达式的构造函数
# 构造加法
def make_sum(a, b):
    return ('+', a, b)

# 构造乘法
def make_prod(a, b):
    return ('*', a, b)

# 构造减法
def make_diff(a, b):
    return ('-', a, b)

# 构造除法
def make_div(a, b):
    return ('/', a, b)

# 在定义表达式处理函数时，经常需要区分基本表达式（直接处理）和复合表达式（递归处理），为分辨这两种情况，定义一个判别是否为基本表达式的函数
def is_basic_exp(a):
    return not isinstance(a, tuple)

# 为简单起见，这里认为只有int,float.complex三个只有数值类型的对象，判断是否数值的函数可以用下面定义
def is_number(x):
    return (isinstance(x, int) or isinstance(x, float) or isinstance(x, complex))


# 加法运算
def eval_sum(a, b):
    if is_number(a) and is_number(b):
        return a + b
    if is_number(a) and a == 0:
        return b
    if is_number(b) and b == 0:
        return a

    return make_sum(a, b)

# 减法运算
def eval_diff(a, b):
    if is_number(a) and is_number(b):
        return a - b
    if is_number(a) and a == 0:
        return -b
    if is_number(b) and b == 0:
        return a

    return make_diff(a, b)


# 乘法运算
def eval_prod(a, b):
    if is_number(a) and is_number(b):
        return a * b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 0:
        return 0

    return make_prod(a, b)

# 除法运算
def eval_div(a, b):
    if is_number(a) and is_number(b):
        return a / b
    if is_number(a) and a == 0:
        return 0
    if is_number(b) and b == 1:
        return a
    if is_number(b) and b == 0:
        raise ZeroDivisionError
    return make_div(a, b)




# 下面是求值函数的基本部分
def eval_exp(e):

    if is_basic_exp(e):
        return e

    op, a, b = e[0], eval_exp(e[1]), eval_exp(e[2])

    if op == '+':
        return eval_sum(a, b)

    if op == '-':
        return eval_diff(a, b)

    if op == '*':
        return eval_prod(a, b)

    if op == '/':
        return eval_div(a, b)

    else:
        raise ValueError('Unknow operater:', op)


if __name__ == '__main__':

    e1 = make_prod(3, make_sum(2, 5))
    print(eval_exp(e1))
