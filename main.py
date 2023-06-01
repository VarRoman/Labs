C13 = 2102 % 13

print('Мій варіант №{}, за умовою потрібно визначити ієрархію легкових автомобілів. Створити таксопарк. '
      'Порахувати вартість автопарку. Провести сортування автомобілів парку за витратами палива. '
      'Знайти автомобіль у компанії, що відповідає заданому діапазону швидкості автомобіля.'.format(C13))

# Зазначу, що я погано розбираюся в машинах та бізнесі, що ґрунтується на автомобілях

cars = ['Машина1, 43000, 50, 200 \
Машина2, 16000, 60, 300']


class DefineCars:
    """Клас для визначення рейтингу введених автомобілів"""

    def calculate_rate(self, car, price, fuel, speed, index):
        dif = (self.car_prices[index] - self.car_prices[index - 1]) / 3
        for i in range(3):
            if price < ((dif + self.car_prices[index]) * (i + 1)):
                self.user_input.append([car, price, fuel, speed, index * 3 + i + 1])
                break

    def __init__(self):
        self.car_prices = [4000, 40000, 100000]
        self.user_input = []

    def define_rate(self):
        print('Введіть назву машини, її ціну, витрата палива на 100 кілометр, швидкість (через кому з пробілом)')
        print('(Натисніть Enter якщо список закінчився)')
        while True:
            try:
                inp = input().split(', ')
                if int(inp[1]) > 4000:
                    if int(inp[1]) < self.car_prices[2]:
                        if int(inp[1]) < self.car_prices[1]:
                            self.calculate_rate(inp[0], int(inp[1]), int(inp[2]), int(inp[3]), 1)
                            continue
                        else:
                            self.calculate_rate(inp[0], int(inp[1]), int(inp[2]), int(inp[3]), 2)
                            continue
                    else:
                        self.user_input.append([inp[0], 10])
            except IndexError:
                break


class TaxiPark(DefineCars):
    """Клас для виведення таблички та рахування вартості таксопарку"""
    def show_park(self):
        print('Назва:      Ціна:       Витр. пал.:   Швидкість:   Рейтинг:')
        for i in self.user_input:
            print('{0}{1:>{2}}{3:>{4}}{5:>{6}}{7:>{8}}'.format(i[0], i[1], 12 - len(i[0]) + len(str(i[1])), i[2],
                                                               12 - len(str(i[1])) + len(str(i[2])), i[3],
                                                               14 - len(str(i[2])) + len(str(i[3])), i[4],
                                                               13 - len(str(i[3])) + len(str(i[4]))))

    def __init__(self):
        super().__init__()
        self.define_rate()

    def table_and_price(self):
        while True:
            inp = input('Чи бажаєте переглянути табличку автопарку?(Так/Ні) ')
            if inp == 'Так':
                self.show_park()
                break
            if inp == 'Ні':
                break
            else:
                'Ви неправильно ввели відповідь'
        price_inp = input('Чи бажаєте побачити загальну вартість автопарку? ')
        while True:
            if price_inp == 'Так':
                worth = 0
                for i in self.user_input:
                    worth += i[1]
                print('Загальна вартість автопарку - ' + str(worth))
                break
            if price_inp == 'Ні':
                break
            else:
                'Ви неправильно ввели відповідь'


cl = TaxiPark()
cl.table_and_price()
