C13 = 2102 % 13

print('Мій варіант №{}, за умовою потрібно визначити ієрархію легкових автомобілів. Створити таксопарк. '
      'Порахувати вартість автопарку. Провести сортування автомобілів парку за витратами палива. '
      'Знайти автомобіль у компанії, що відповідає заданому діапазону швидкості автомобіля.'.format(C13))

# Зазначу, що я погано розбираюся в машинах та бізнесі, що ґрунтується на автомобілях

cars = ['Машина1, 43000, 50, 200 \
Машина2, 17000, 60, 300\
Машина3, 79000, 80, 400\
Машина4, 110000, 30, 500']


class DefineCars:
    """Клас для визначення рейтингу введених автомобілів"""

    def calculate_rate(self, car, price, fuel, speed, index):
        dif = (self.car_prices[index] - self.car_prices[index - 1]) / 3
        for i in range(3):
            if price < ((dif + self.car_prices[index-1]) * (i + 1)):
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
                        self.user_input.append([inp[0], int(inp[1]), int(inp[2]), int(inp[3]), 10])
                        break
            except IndexError:
                break

class SortAndSearch:
    """Клас для сортування та пошуку"""

    @staticmethod
    def getkey(x):
        return x[2]

    def sort_the_car_list(self, some_list):
        some_list.sort(key=self.getkey, reverse=True)

    @staticmethod
    def search_in_range(some_list):
        print('За яким параметром ви хочете виконати пошук? ')
        print('1 - Ціна\n2 - Витрата палива\n3 - Швидкість\n4 - Рейтинг')
        inp = input()
        range_input = input('В якому діапазоні?(Через пробіл) ').split(' ')
        sorted_list = []
        try:
            for i in some_list:
                if int(range_input[0]) < int(i[int(inp)]) < int(range_input[1]):
                    sorted_list.append(i)
            return sorted_list
        except ValueError:
            print('Ви неправильно ввели значення')


class TaxiPark(DefineCars, SortAndSearch):
    """Клас для виведення таблички та рахування вартості таксопарку"""

    @staticmethod
    def show_park(car_list):
        print('Назва:      Ціна:       Витр. пал.:   Швидкість:   Рейтинг:')
        for i in car_list:
            print('{0}{1:>{2}}{3:>{4}}{5:>{6}}{7:>{8}}'.format(i[0], i[1], 12 - len(i[0]) + len(str(i[1])), i[2],
                                                               12 - len(str(i[1])) + len(str(i[2])), i[3],
                                                               14 - len(str(i[2])) + len(str(i[3])), i[4],
                                                               13 - len(str(i[3])) + len(str(i[4]))))

    def __init__(self):
        super().__init__()

    def total_price(self):
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


class Control(TaxiPark):
    """Клас для контролю інишх класів"""
    def __init__(self):
        super().__init__()

    def control_unit(self):
        self.define_rate()
        while True:
            sort_table_input = input('Чи бажаєте сортувати табличку за витратами палива?(Так/....) ')
            if sort_table_input == 'Так':
                self.sort_the_car_list(self.user_input)
            show_table_input = input('Чи бажаєте переглянути табличку?(Так/....) ')
            if show_table_input == 'Так':
                self.show_park(self.user_input)
            self.total_price()
            search_input = input('Чи бажаєте виконати пошук за фільтром параметра?(Так/....) ')
            if search_input == 'Так':
                sorting_list = self.search_in_range(self.user_input)
                show_input = input('Чи бажаєте переглянути відсортовану табличку? табличку?(Так/....) ')
                if show_input == 'Так':
                    self.show_park(sorting_list)
            ask_input = input('Чи бажаєте закінчити програму?(Так/....) ')
            if ask_input == 'Так':
                break


cl = Control()
cl.control_unit()
