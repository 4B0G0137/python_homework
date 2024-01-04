class StustBeverageShop:
    class Employee:
        def __init__(self, name, experience, work_hours):
            # 初始化員工物件的屬性
            self.name = name
            self.experience = experience
            self.work_hours = work_hours

        def query_name(self):
            # 查詢員工名字
            return self.name

        def query_experience(self):
            # 查詢員工年資
            return self.experience

        def query_work_hours(self):
            # 查詢員工工時
            return self.work_hours

        def calculate_salary(self):
            # 假設每小時工資為100元，計算月薪
            hourly_rate = 100
            return self.work_hours * hourly_rate

        def increase_work_hours(self, hours):
            # 增加工時
            self.work_hours += hours

        def increase_experience(self, years):
            # 增加年資
            self.experience += years

    class Beverage:
        def __init__(self, price, ingredient1, ingredient2):
            # 初始化飲料物件的屬性
            self.price = price
            self.ingredient1 = ingredient1
            self.ingredient2 = ingredient2

    class ColdBeverage(Beverage):
        def __init__(self, name, ice_level, sweetness, price, ingredient1, ingredient2):
            # 初始化冷飲物件的屬性，並呼叫父類別的初始化函式
            super().__init__(price, ingredient1, ingredient2)
            self.name = name
            self.ice_level = ice_level
            self.sweetness = sweetness

        def modify_name(self, new_name):
            # 修改名稱
            self.name = new_name

        def adjust_sweetness(self, new_sweetness):
            # 調整甜度
            self.sweetness = new_sweetness

        def adjust_price(self, new_price):
            # 調整價錢
            self.price = new_price

    class HotBeverage(Beverage):
        def __init__(self, name, sweetness, price, ingredient1, ingredient2):
            # 初始化熱飲物件的屬性，並呼叫父類別的初始化函式
            super().__init__(price, ingredient1, ingredient2)
            self.name = name
            self.sweetness = sweetness

        def modify_name(self, new_name):
            # 修改名稱
            self.name = new_name

        def adjust_sweetness(self, new_sweetness):
            # 調整甜度
            self.sweetness = new_sweetness

        def adjust_price(self, new_price):
            # 調整價錢
            self.price = new_price


# 建立 StustBeverageShop 物件
stust_shop = StustBeverageShop()

# 建立員工物件
employee1 = stust_shop.Employee("John", 3, 160)
employee2 = stust_shop.Employee("Jane", 5, 180)
employee3 = stust_shop.Employee("Bob", 2, 140)

# 呼叫員工物件的副函式
print(employee1.query_name())
print(employee2.query_experience())
print(employee3.calculate_salary())

# 建立飲料物件
beverage1 = stust_shop.ColdBeverage(
    "Iced Tea", "Regular", "50%", 50, "Tea", "Ice")
beverage2 = stust_shop.HotBeverage("Hot Coffee", "75%", 40, "Coffee", "Water")
beverage3 = stust_shop.ColdBeverage(
    "Smoothie", "Extra Ice", "25%", 60, "Fruit", "Ice")

# 呼叫飲料物件的副函式
beverage1.modify_name("Green Tea")
beverage2.adjust_sweetness("80%")
beverage3.adjust_price(65)
