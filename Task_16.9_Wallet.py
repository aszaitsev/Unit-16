# Task_16.9.3
class Clients:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}, г.{self.city}, Баланс: {self.balance} руб.'

# Task_16.9.4
    def guests(self):
        return f'{self.name} {self.surname}, г.{self.city}'


client1 = Clients('Иван', 'Петров', 'Москва', 50)
client2 = Clients('Алексей', 'Зайцев', 'Северодвинск', 100)
client3 = Clients('Вячеслав', 'Данилов', 'Санкт-Петербург', 83)
print(f"{client1}")

guests_list = [client1, client2, client3]
for guest in guests_list:
    print(guest.guests())