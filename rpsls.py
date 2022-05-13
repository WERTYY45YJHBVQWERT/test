#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李艳华
日期：2022|5|12
"""





# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    if name == "石头":
        return 0
    elif name == "史波克":
        return 1
    elif name == "纸":
        return 2
    elif name == "蜥蜴":
        return 3
    elif name == "剪刀":
        return 4
    else:
        return "Error：No Correct Name"



    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


     #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    if number == 0:
        return "石头"
    elif number == 1:
        return "史波克"
    elif number == 2:
        return "纸"
    elif number == 3:
        return "蜥蜴"
    elif number == 4:
        return "剪刀"
    else:
        return "Error.No Correct Name"




    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

     #编写执行代码,代码完成后将pas
import random
def rpsls(player_choice):
    print("")
    print("您的选择是",player_choice)
    player_number = name_to_number(player_choice)#调用函数将名字转化为数字
    comp_number = random.randrange(0,5)#随机选择数字
    comp_choice = number_to_name(comp_number)#调用函数将数字转化为名字
    print("计算机的选择为:%s" % comp_choice)
    difference = (player_number-comp_number) % 5
    if difference == 1 or difference == 2:
        print("您赢了")
    elif difference == 3 or difference == 4:
        print("计算机赢了")
    elif difference == 0:
        print("您和计算机出的一样呢")
    else:
        print("Error")






    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("规则是：剪刀裁剪纸；纸包裹石头；石头砸碎剪刀；石头砸死蜥蜴；蜥蜴毒死史波克；剪刀腰斩蜥蜴；蜥蜴吃掉纸；纸反驳史波克；史波克蒸发石头")
print("----------------")
print("请输入您的选择:")
name = input()
rpsls(name)



