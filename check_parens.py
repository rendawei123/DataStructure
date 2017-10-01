"""
括号匹配问题
    在扫描正文的过程中，遇到的闭括号应该与此前最近遇到的且尚未获得匹配的开括号配对.如果最近的未匹配开括号与当前闭括号不配对，或者找不到这样的开括号，就是匹配失败，说明这段正文里的括号不配对
使用缓存结构
    由于存在多种不同的括号对，每种括号都可能出现多次，而且还可能嵌套，为了检查是否匹配，扫描中必须保存遇到的开括号，由于写程序时无法预知要处理的正文里会有多少括号需要保存，因此不能使用固定数目的变量保存，必须使用缓存结构
使用栈
    如果一个括号已配对，就应该删除这个括号，为随后的匹配做好准备，由于括号的性质，后遇到并保存的括号应该先配对并被删除，为倒数第二个保存的括号做准备，这就是按照出现的顺序后进先出
总结：
    以上情况分析，使用栈保存遇到的开括号可以正确支持匹配工作。
    1、顺序扫描被检查正文（一个字符串）里的一个个字符
    2、检查中跳过无关字符（所有非括号的字符都和当前处理无关）
    3、遇到开括号将其压入栈
    4、遇到闭括号时，弹出当前栈顶元素与之匹配。
    5、如果匹配成功则继续，发现不匹配时检查以失败告终
"""
from list_stack import ListStack  # 引入ListStack

# 定义变量记录中有用的数据
parens = "()[]{}"  # 所有括号字符
open_parens = '([{'  # 开括号字符
match_parens_dict = {')':'(', ']':'[', '}':'{'}  # 各种括号对应关系


# 定义括号生成器，每次调用返回text里的下一括号以及位置
def parentheses(text):
    i, text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        yield text[i], i
        i += 1


def check_parens(text):
    """
    定义括号匹配函数
    """
    st = ListStack()    # 实例化栈

    for per,i in parentheses(text):
        if per in open_parens:
            st.push(per)
        elif st.pop() != match_parens_dict[per]:
            print('不匹配的括号是：', i, per)
            return False

    print('匹配成功')
    return True



if __name__ == '__main__':
    # a = ListStack()
    # a.push(1)
    # print(a.pop())
    text = 'laskdjf{alskdflskd9(laskdjflskd)}lksdjf}'
    # for i in parentheses(text):
        # print(i)
    check_parens(text)
