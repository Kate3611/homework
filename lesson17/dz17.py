# Два метода в классе, один принимает в себя либо строку, либо число.
# Если я передаю строку, то смотрим:
# если произведение гласных и согласных букв меньше
# или равно длине слова, выводить все гласные, иначе согласные;
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе.



class Something:

    def __init__(self, a):
        self.a = a

    def func(self):
        vowels = ''
        consonants = ''
        even = 0
        letters_v = 'eyuioa'
        letters_c = 'qwrtpsdfghjklzxcvbnm'

        if type(self.a) is str:
            for i in self.a:
                if i in letters_v:
                    vowels += i
                elif i in letters_c:
                    consonants += i
            res_1 = len(vowels) * len(consonants)

            if res_1 <= len(str(self.a)):
                print(f'vowels: {vowels}')
            else:
                print(f'consonants: {consonants}')

        elif type(self.a) is int:
            for x in str(self.a):
                if int(x) % 2 == 0:
                    even += x
            res_2 = even * len(str(self.a))
            return res_2

    def len(self):
        return len(str(self.a))


something = Something('hello my friends ')
print(something.func())
something_2 = Something(2225464)
print(something_2.len())



