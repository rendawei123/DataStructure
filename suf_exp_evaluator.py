"""
后缀表达式求值

后缀表达式也就是将1+2写为12+，这样便于计算机便利及运算

根据后缀表达式的计算规则，计算过程应该是顺序检查表达式里的一个个项，分两种情况：
1.遇到运算对象时，应该记录它以备后面使用
2.遇到运算符（函数名也一样）时，应该根据其元数（假定都是二元运算符），取得前面最近遇到的几个运算对象或已完成运算的结果（二元运算符都要取两个），应用这个运算符（或函数）计算，并保存其结果

经过上面的分析之后，又出现了需要记录信息以备将来使用的问题，因为考虑到有的计算表达式可以任意复杂，不能实现确定需要记录的信息的项数，这时，就必须要一个缓存结构：
    1、需要记录的是已经已经掌握的数据，无论这些数据是直接由外部获得还是前面计算出来的结果，都需要缓存
    2、每次处理运算，应该使用的都是此前记录的最后几个结果
综合以上分析，咱们应该使用栈结构作为缓存结构
"""

from list_stack import ListStack
from trans_infix_fuffix import trans_infix_suffix


# 定义一个函数，把表达式的字符串转化为项的表
def split_exp(line):
    return line.split()


# 定义检查深度的栈，由于前面定义的栈类不能检查深度，因此我们要继承前面的类然后修改
class EListStack(ListStack):
    def depth(self):
        return len(self._elems)


def suf_exp_evaluator(exp_list):

    # exp_list = split_exp(exp)
    operators = '+-*/'
    st = EListStack()

    for i in exp_list:
        if i not in operators:   # 如果不再运算符里面，则必须是元素，压入栈
            st.push(float(i))
            continue

        if st.depth() < 2:  # 经过上次过滤，此时i肯定是运算符，则栈里面的元素必须要大于2
            raise SyntaxError('Extra operand(s)')

        x = st.pop()
        y = st.pop()

        if i == '+':
            z = x + y
        elif i == '-':
            z = y - x
        elif i == '*':
            z = y * x
        elif i == '/':  # 这里可能引发异常，除数不能为零
            z = y / x
        else:
            break

        st.push(z)
    if st.depth() == 1:
        return st.pop()

    # 处理完整个表达式后，栈里面应该只剩下一个值，否则表达式错误引发异常
    raise SyntaxError('Extra operand(s)')


# 为了提高用户体验，包装一下，让用户可以自动输入
def suffix_exp_calculator():
    while True:
        try:
            line = input('请输入中缀表达式（输入end退出）：').strip()
            if line == 'end':
                return
            res = suf_exp_evaluator(trans_infix_suffix(line))
            print(res)
        except Exception as ex:
            print('errot:', type(ex), ex.args)


if __name__ == '__main__':
    # s = EListStack()
    # s.push(1)
    # print(s.depth())
    # s = suf_exp_evaluator('1 2 +')
    # print(s)
    suffix_exp_calculator()
