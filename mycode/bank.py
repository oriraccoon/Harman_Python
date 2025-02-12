class Piggy():

    def __init__(self, money):
        self.__money = money

    def deposit(self, money):
        self.__money += money
    

    
    def show_money(self):
        print(f"현재 잔액은 : {self.__money}입니다.")