# tab 选中的代码向右移动
# shift+tab 选中的代码向左移动

'''sex = input("请输入性别：")
if sex == "男":
    print("您好，先生!")
elif sex == "女":
    print("您好，女士！")
else:
    print("性别未知.")'''

str_prince = input("请输入一个商品单价：")
str_num = input("请输入一个购买的数量：")
money = input("请输入支付金额：")
result = float(money) - float(str_prince) * int(str_num)
if result < 0:
    print("金额不足！")
else:
    print("应找回：" + str(result) + "元")
