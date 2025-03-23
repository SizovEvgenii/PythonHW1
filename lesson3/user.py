class User:
    first_name = 'Evgenii'
    last_name = 'Ivanov'

    def __init__(self, name):
          self.first_name = name

    def sayName(self):
         print("Меня зовут ", self.first_name)

    def sayLast(self):
         print("Моя фамилия ", self.last_name)

    def sayAllname(self):
         print(self.first_name, self.last_name)