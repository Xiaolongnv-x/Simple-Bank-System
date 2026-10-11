total_money = 5000000
#定义存款函数
def my_deposit():
    global total_money
    try:
        deposit_amount = int(input("请输入您的存储金额："))
    except ValueError:
        print("请输入数字！")
        return
    total_money += deposit_amount
    print(f"存储成功！现在总金额:{total_money}元")

#定义取款函数
def my_withdraw():
    global total_money
    try:
        withdraw_amount=int(input("请输入您的取出金额："))
    except ValueError:
        print("请输入数字！")
        return
    if withdraw_amount > total_money:
        print(f"当前余额为{total_money}元不够，请重新输入！")
        return None
    total_money -= withdraw_amount
    print(f"取款成功，当前总金额为{total_money}元")

#定义菜单
def my_menu():
    print("'欢迎进入银行菜单'\n你现在有三个功能使用:\t1.存款\t2.查询金额\t3.取款\t4.退出")

    choice = input("请输入你的选择序号：")
    if choice == "1":
        my_deposit()
    elif choice =="2":
        print(f"总金额：{total_money}")
    elif choice =="3":
        my_withdraw()
    elif choice =="4":
        return "quit"
    else:
        print("输入错误!请在1~4之间填选")
    return None

#主函数模块
real_name ="Littlegrill"
def bank_system():
    while True:
        account_name = input("请输入您的姓名：")
        if account_name == real_name:
            break
        print("输入姓名有误，请重新输入")

    while True:
        result = my_menu()
        if result == "quit":
            print("谢谢使用！欢迎下次光迎！")
            break

#主程序
print("欢迎进入银行系统！\n您可以在这进行金钱交易")
bank_system()
