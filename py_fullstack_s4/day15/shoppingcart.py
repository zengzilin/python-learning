product_list = [["Iphone",5800],
               ["coffee",30],
               ['疙瘩汤',10],
               ['Python Book',99],
               ['Bike',199],
               ['ViVo X9',2499]
               ]

shopping_cart = []

salary = int(input("input your salary:"))

while True:

    index = 0
    for product in product_list :
        print(index,product)
        index +=1

    choice = input(">>:").strip()

    if choice.isdigit(): #判断是否为数字
        choice = int(choice)
        if choice >=0 and choice < len(product_list):#商品存在
            product = product_list[choice] #得到商品
            if product[1] <= salary: #判断能否买得起
                #买得起
                shopping_cart.append(product) #加入购物车
                salary -= product[1] #扣钱
                print("Added product" + product[0] + "into shopping cart,your current balance:" + str(salary) )
            else:
                print("买不起,穷逼!产品价格是" + str(product[1]) + "你还差" + str(product[1]-salary) + "钱")

        else:
            print("商品不存在!")

    elif choice == "q":
        print("---已购买商品列表----")

        for i in shopping_cart:
            print(i)

        print("您的余额为:",salary)
        print("----end-----")
        break
    else:
        print("无此选项")