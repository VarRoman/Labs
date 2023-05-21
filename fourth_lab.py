
C11 = 2102 % 11
print('Варіант №{0}, отже треба визначити клас навчальний заклад, який складається як мінімум з 5-и полів.\n'.format(C11))

class School(object):
    """Клас для визначення та сортування списків 5-их класів"""

    def __init__(self):
        self.pupils_a = ['Богунов', 'Безщасний', 'Романчук', 'Прокоплюк', 'Марещенко',
                         'Цуря', 'Чортиголов', 'Котигорошко', 'Шевчук', 'Журбенко']
        self.pupils_b = ['Палчей', 'Журбенко', 'Задорожний', 'Гуменюк', 'Губенко', 'Захаренко',
                         'Костенюк', 'Трипільна', 'Бояринова']
        self.list_classes = [[self.pupils_a, 'А']]

    def getkey(self, item):
        return item[0]
    def sort_classes(self):
        while True:
            ask = input('Чи хочете додати список ще одного класу? (Так/Ні) ')
            if ask == 'Так':
                letter = input('Введіть букву 5-ого класу, список якого хочете відсортувати: (Б, В, Г): ')
                if letter == 'Б':
                    self.list_classes.append([self.pupils_b, 'Б'])
                elif letter == 'В':
                    inp_for_lst = input('Введіть прізвища !через кому та пробіл!')
                    lst_c = inp_for_lst.split(', ')
                    self.list_classes.append([lst_c, 'В'])
                elif letter == 'Г':
                    inp_for_lst = input('Введіть прізвища !через кому та пробіл!')
                    lst_d = inp_for_lst.split(', ')
                    self.list_classes.append([lst_d, 'Г'])
                else:
                    print('Ви ввели неправильну букву')
            if ask == 'Ні':
                break
            else:
                'Ви ввели відповідь невірно'
        for i in self.list_classes:
            i[0].sort(key=self.getkey)
            print('Клас ' + i[1] + ': ')
            print(i[0])


use = School()
use.sort_classes()
