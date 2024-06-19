
# X/O games with robot

import random
class Oyin():
    # Klasslarni ko'pincha katta harf bilan boshlaydi

    def __init__(self):
        '''
        O'yinga nimalar kerak bo'ladi?
        > Taxta/doska: kim qayerga X/O qo'ygani
        '''
        self.taxta = [] # Qanday saqlaysiz? O'yin boshlanganda nima bo'lishi kerak
        for i in range(9):
            self.taxta.append(' ')
    def korsatish(self):
        '''
        Hozirgi o'yinda nima harakatlar qilingan bo'lsa, shuni ko'rsatishi kerak.
        '''
        print(f"| {self.taxta[0]} | {self.taxta[1]} | {self.taxta[2]} |")
        print(f"| {self.taxta[3]} | {self.taxta[4]} | {self.taxta[5]} |")
        print(f"| {self.taxta[6]} | {self.taxta[7]} | {self.taxta[8]} |")
        return

    def yurish_kiritish(self): # Yana biror narsa qo'shish kerakmi?
        '''
        O'yinchi qayerga qo'yishni aytsa, o'yinni yangilab, saqlab qo'yish kerak.
        '''

        odam = input(f"Kimning navbati(X vs O):")
        if odam == 'X':
            oyinchi = int(input(f"{odam} ning joylashuvini kiriting(1:9):"))
            if self.taxta[oyinchi - 1] == ' ':
                self.taxta[oyinchi - 1] = f'{odam}'
                return True
        elif odam == 'O':
            return self.computer()
        else:
            print("raqam kiritganinggizga ishonch hosil qiling!")
    def computer(self):
        list = []
        for i in range(len(self.taxta)):
            if self.taxta[i] == ' ':
                list.append(i)
        yurish = random.choice(list)
        self.taxta[yurish] = 'O'
        return True


    def yutish(self):
        yutish_k = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
        for i in yutish_k:
            if self.taxta[i[0]] == self.taxta[i[1]] == self.taxta[i[2]] != ' ':
                return True
        return False


def oynash_test():
    '''
    O'yin o'ynash.
    '''
    oyin = Oyin()
    while True:
        oyin.korsatish()
        if oyin.yurish_kiritish() == True:
            if oyin.yutish():
                oyin.korsatish()
                print("Siz yutdingiz!")
                break
            continue
        else:
            break



    # O'yinchilardan yurishini so'rab, yangilab ko'rsatingchi
    '''
    --> ko'rsatish funksiyasi
        | | | |
        | | | |
        | | | |
    --> X o'yinchi yurish kiritadi
    --> ko'rsatish funksiyasi
        |X| | |
        | | | |
        | | | |
    --> O o'yinchi yurish kiritadi
    --> ko'rsatish funksiyasi
        |X| | |
        | | | |
        | |O| |
    ......
    '''




oynash_test()