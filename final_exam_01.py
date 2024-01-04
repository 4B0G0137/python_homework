# 建立一個炸雞的類別FriedChicken
class FriedChicken:

    # 定義建構子(建立五個屬性:名稱、價格、數量、辣度及評論)
    def __init__(self, name, price, quantity, spiciness, review=''):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.spiciness = spiciness
        self.review = review

    # 副函式change_quantity()改變炸雞的數量
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    # 副函式change_price()改變炸雞的價格
    def change_price(self, new_price):
        self.price = new_price

    # 副函式get_fried_chicken_info()輸出炸雞的詳細訊息
    def get_fried_chicken_info(self):
        print(f"name:{self.name}\nprice:{self.price} NTD\nquantity:{self.quantity}\nspiciness:{self.spiciness}\nreview:{self.review}\n")


# 建立炸雞物件一
fried_chicken_01 = FriedChicken(
    'spicy_fried_chicken', 60, 20, 'very spicy', 'It is so spicy!')
# 更改價格
fried_chicken_01.change_price(65)

# 更改數量
fried_chicken_01.change_quantity(10)

# 輸出炸雞的詳細訊息
fried_chicken_01.get_fried_chicken_info()

#  建立炸雞物件二
fried_chicken_01 = FriedChicken(
    'Pepper_fried_chicken', 70, 30, 'a little spicy', 'It is so delicious!')

# 更改價格
fried_chicken_01.change_price(60)

# 更改數量
fried_chicken_01.change_quantity(15)

# 輸出炸雞的詳細訊息
fried_chicken_01.get_fried_chicken_info()

#  建立炸雞物件三
fried_chicken_01 = FriedChicken(
    'garlic_fried_chicken', 80, 40, 'very spicy', 'I like this so much!')

# 更改價格
fried_chicken_01.change_price(90)

# 更改數量
fried_chicken_01.change_quantity(20)

# 輸出炸雞的詳細訊息
fried_chicken_01.get_fried_chicken_info()
