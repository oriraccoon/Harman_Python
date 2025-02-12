# 생성자 (Constructor)
# 클래스 생성 시 자동으로 호출되는 함수!!


class Addr():
    def __init__(self, name_o, age_o, tel_o):
        self.name = name_o
        self.age = age_o
        self.tel = tel_o
    def __init__(self, name_o, age_o):
        self.name = name_o
        self.age = age_o
        self.tel = " "
    
    def show_addr(self):
        print(f"name : {self.name}, age : {self.age}, tel : {self.tel}")
        