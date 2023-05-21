
textic = ["Python, Python, oh, how I love Python! It's a language that's powerful, Python, Python, so delightful to "
    "use.With Python, Python, you can solve problems with ease. Its syntax is clean, Python, Python, it's a breeze. " 
    "From data analysis to web development, Python, Python, it's the ultimate tool. With libraries "
    "galore, Python, Python, "
    "you'll never be a fool. Whether it's loops or conditionals, Python, Python, it's all there. "
    "Just write your code, Python, Python, and watch it run without a care. Python, Python, "
    "you're my go-to language of choice. With your versatility and simplicity, Python, Python, I rejoice!"]

words = ['Python', 'breeze']

C3 = 2102 % 3
print('C3 = ' + str(C3) + ', тому тип текстових змінних буде String')

C17 = 2102 % 13
print('C17 = ' + str(C17) + ', дія з текстовим рядком:\nЗадано текст та масив слів. '
                            'Підрахувати у скількох реченнях зустрічається кожне слово масиву.')

def count_words(arr, text):
    modified = text[0].translate(str.maketrans('', '', '.,'))
    modified_list = modified.split(' ')
    for i in arr:
        counter = 0
        tempor = [arr.index(i), arr.pop(arr.index(i))]
        arr.insert(tempor[0], [tempor[1]])
        while True:
            try:
                modified_list.remove(i)
                counter += 1
            except ValueError:
                try:
                    modified_list.remove(i.capitalize())
                    counter += 1
                except ValueError:
                    arr[tempor[0]].append(counter)
                    break
    return arr

print(count_words(words, textic))
