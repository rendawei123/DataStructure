"""
中缀表达式转换为后缀表达式

在扫描中如果遇到一个运算符时不能将其输出，只有遇到下一运算符的优先级不高于本运算符时才应该去做本运算符要求的计算，外加上括号等问题，因此，中缀表达式直接计算是不可取的

因此，我们应该考虑转换算法，先将中缀表达式转化为后缀表达式，然后再进行计算

"""

# 导入栈
from list_stack import ListStack

# 定义优先级
priority = {'(':1, '+':3, '-':3, '*':5, '/': 5}

# 定义运算符集
infix_operators = '+-*/()'

def tokens(line):
    """定义生成器函数，逐一生成line中的每一个项，项是浮点数和运算符，这里先不考虑一元运算符和带符号的浮点数"""
    i, line_length = 0, len(line)
    while i < line_length:

        # 如果遇到空格的话，i+1
        while i < line_length and line[i].isspace():
            i += 1
        if i >= line_length:
            break

        # 如果遇到运算符的话，输出
        if line[i] in infix_operators:
            yield line[i]
            i += 1
            continue

        # 开始处理运算对象，j主要针对科学计数发中e的情况
        j = i + 1

        while (j < line_length and not line[j].isspace() and line[j] not in infix_operators):
            if ((line[j]=='e' or line[j]=='E') and j+1 < line_length and line[j+1]=='-'):
                j +=1
            j += 1

        yield line[i:j]
        i = j

# 定义中缀表达式转化为后缀表达式函数
def trans_infix_suffix(line):
    st = ListStack()
    exp = []

    for x in tokens(line):  # 循环便利处理好了的表达式
        if x not in infix_operators:   # 如果每一项是运算对象，直接添加进表达式
            exp.append(x)

        elif st.is_empty() or x == '(':   # 左括号进栈
            st.push(x)

        # 如果是右括号的话需要将左括号和右括号里面的内容先放到表达式里面，因为括号中的运算符是优先级最高的
        elif x == ')':
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
            if st.is_empty():  # 如果只有右括号没有左括号的话说明表达式有问题，此时应该引发异常
                raise SyntaxError('Missing"()".,')
            st.pop()   # 不论是左右括号都应该最后出栈，因为括号不应该出现在表达式中

        else:
            # 根据优先级判断运算符应该放的位置
            while (not st.is_empty() and priority[st.top()] >= priority[x]):
                exp.append(st.pop())
            st.push(x)

    while not st.is_empty():  # 最后将栈中剩下的运算符依次放入表达式
        exp.append(st.pop())

    return exp


if __name__ == '__main__':
    # line = '(123 + 456) * 3e-2'
    line = '( 1 - 2 ) * 3'
    # for i in tokens(line):
        # print(i)
    exp = trans_infix_suffix(line)
    print(exp)
