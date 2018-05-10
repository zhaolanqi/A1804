#获取 输入的价格
xgprice = input("请您输入西瓜的价格:")
#获取 输入的重量
xgweight = input("请您输入西瓜的重量:")
#-------------------
#把输入的str类型数据转化成int进行计算
price = float(xgprice)
weight = float(xgweight)
#计算西瓜的总金额
money = price * weight
print ("该西瓜的单价是 %.2f 元/斤 " % (price))
print ("该西瓜的重量是 %.2f 斤 " % (weight))
print ("您应当支付总金额 %.2f 元 " % (money))
