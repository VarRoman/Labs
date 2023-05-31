C13 = 2102 % 13

print('Мій варіант №{}, за умовою потрібно визначити ієрархію легкових автомобілів. Створити таксопарк. '
      'Порахувати вартість автопарку. Провести сортування автомобілів парку за витратами палива. '
      'Знайти автомобіль у компанії, що відповідає заданому діапазону швидкості автомобіля.'.format(C13))


# Зазначу, що я погано розбираюся в машинах та бізнесі, що ґрунтується на автомобілях

class DefineCars:
    """Клас для визначення рейтингу введених автомобілів"""
    def calculate_rate(self, index, price, car):
        dif = (self.car_prices[index] - self.car_prices[index-1]) / 3
        for i in range(3):
            if price < ((dif + self.car_prices[index]) * (i + 1)):
                self.user_input.append([car, index * 3 + i + 1])
                break

    def __init__(self):
        self.car_prices = [4000, 40000, 100000]
        print('Введіть назву машини та її ціну (через кому з пробілом)')
        print('Машина, ціна: (Натисніть Enter якщо список закінчився)')
        self.user_input = []
        while True:
            try:
                inp = input().split(', ')
                if int(inp[1]) > 4000:
                    if int(inp[1]) < self.car_prices[2]:
                        if int(inp[1]) < self.car_prices[1]:
                            self.calculate_rate(1, int(inp[1]), inp[0])
                            continue
                        else:
                            self.calculate_rate(2, int(inp[1]), inp[0])
                            continue
                    else:
                        self.user_input.append([inp[0], 10])
            except IndexError:
                break
        print(self.user_input)

cl = DefineCars()

