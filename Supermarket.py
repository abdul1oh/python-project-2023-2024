

import csv

store = {}


with open('MarketProdact.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for index, qator in enumerate(reader):
        nom = qator[0].strip()
        narx = qator[1].strip()
        kategoriya = qator[4].strip()
        kod = qator[5].strip()
        store[index + 1] = {
            'nom': nom,
            'narx': narx,
            'kategoriya': kategoriya,
            'kod': kod
        }


arava = {}

def menyu():
    print("Supermarket Menyu:")
    print("1 - Menyu Ko'rsatish ")
    print("2 - Mahsulot Ishtash ")
    print("3 - Kategoriyalar Ko'rsatish")
    print("4 - Kategoriyadagi Mahsulotlar Ko'rsatish ")
    print("5 - Arava Ko'rsatish")
    print("6 - Aravaga Solish")
    print("7 - Aravadan O'chirish ")
    print("8 - Aravani Sotib Olish ")


def tanlov():
    while True:
        choice = input("Nima qilmoqchisiz? ")
        if choice.lower() in ['menyu', '1']:
            menyu()
        elif choice == '2':
            mahsulot = input("Nima istamoqchisiz? ")
            javoblar = mahsulotni_istash(mahsulot)
            print("Shu mahsulotlarni topdim:")
            javobni_korsatish(javoblar)
        elif choice == '3':
            kategoriyalarni_korsatish()
        elif choice == '4':
            kategoriya = input("Qaysi kategoriyani istamoqchisiz? ")
            javoblar2 = kategoriya_mahsulot_korsatish(kategoriya)
            print(f"Shu mahsulotlarni topdim:")
            kategoriya_javobini_korsatish(javoblar2)
        elif choice == '5':
            print(arava)
        elif choice == '6':
            raqam = int(input("Mahsulot kodini kiriting: "))
            sotib_olish(raqam)
        elif choice == '7':
            aravadan_ochirish()
        elif choice == '8':
            kassa()
        else:
            print("Noto'g'ri tanlov, qaytadan urinib ko'ring.")


def mahsulotni_istash(mahsulot):
    javoblar = []
    for product in store.values():
        if mahsulot.lower() in product['nom'].lower():
            javoblar.append(product)
    return javoblar

def javobni_korsatish(javoblar):
    if not javoblar:
        print("Hech narsa topilmadi.")
        return

    for index, narsa in enumerate(javoblar[:20]):
        print(f"{narsa['nom']} - {narsa['narx']} - {narsa['kategoriya']}")

    if len(javoblar) > 20:
        print(f"Yana {len(javoblar) - 20} ta mahsulot bor.")




def kategoriyalarni_korsatish():
    javob = []
    for product in store.values():
        if product['kategoriya'] not in javob:
            javob.append(product['kategoriya'])

    print("Supermarketda shu kategoriyalar bor:")
    for kategoriya in javob:
        print(kategoriya)


def kategoriya_mahsulot_korsatish(kategoriya):
    javoblar2 = []
    for product in store.values():
        if kategoriya.lower() == product['kategoriya'].lower():
            javoblar2.append(product)
    return javoblar2

def kategoriya_javobini_korsatish(javoblar2):
    if not javoblar2:
        print("Hech narsa topilmadi.")
        return

    for index, mahsulot in enumerate(javoblar2[:50]):
        print(f"{index + 1}: {mahsulot['nom']} - {mahsulot['narx']} - {mahsulot['kategoriya']}")

    if len(javoblar2) > 50:
        print(f"Yana {len(javoblar2) - 50} ta mahsulot bor.")





def sotib_olish(raqam):
    for code, mahsulot in store.items():
        if raqam == code:
            print("Shu mahsulotni topdim:")
            print(f"{code}: {mahsulot['nom']} - {mahsulot['narx']} - {mahsulot['kategoriya']}")

            miqdori = int(input("Nechta olmoqchilisiz? "))
            umumiy_narx = miqdori * float(mahsulot['narx'].replace('$', ''))
            if code in arava:
                arava[code]['miqdori'] += miqdori
                arava[code]['umumiy'] = f"${float(arava[code]['umumiy'].replace('$', '')) + umumiy_narx:.2f}"
            else:
                arava[code] = {
                    'nomi': mahsulot['nom'],
                    'narxi': mahsulot['narx'],
                    'miqdori': miqdori,
                    'umumiy': f"${umumiy_narx:.2f}"
                }

            print(f"{miqdori} {mahsulot['nom']} aravaga qo'shildi - {umumiy_narx:.2f}")
            return

    print("Mahsulot topilmadi.")


def aravadan_ochirish():
    if not arava:
        print("Aravangiz bo'sh.")
        return

    print("Sizni Aravangiz:")
    print("Ko'd - Mahsulot - Narxi - Soni - Jami")

    for code, mahsulot in arava.items():
        print(f"{code} - {mahsulot['nomi']} - {mahsulot['narxi']} - {mahsulot['miqdori']} - {mahsulot['umumiy']}")

    product_code = int(input("Qaysi mahsulotni o'chirmoqchisiz (code): "))

    if product_code in arava:
        soni = int(input("Nechtasini o'chirmoqchisiz: "))

        if soni > arava[product_code]['miqdori']:
            print("Siz so'ragan miqdordagi mahsulot aravada yo'q.")
            return

        umumiy_narx = soni * float(arava[product_code]['narxi'].replace('$', ''))

        arava[product_code]['miqdori'] -= soni
        arava[product_code]['umumiy'] = f"${float(arava[product_code]['umumiy'].replace('$', '')) - umumiy_narx:.2f}"

        if arava[product_code]['miqdori'] == 0:
            del arava[product_code]


        print(f"{soni} {arava[product_code]['nomi']} o'chirildi.")
    else:
        print("Bunday mahsulot code topilmadi, qaytadan urinib ko'ring.")




def kassa():
    if not arava:
        print("Aravangiz bo'sh, sotib olish mumkin emas.")
        return

    for code, mahsulot in arava.items():
        print(f"{code} - {mahsulot['nomi']} - {mahsulot['narxi']} - {mahsulot['miqdori']} - {mahsulot['umumiy']}")

    jami = sum(float(mahsulot['umumiy'].replace('$', '')) for mahsulot in arava.values())
    print(f"Jami: ${jami:.2f}")

    sotib_olish = input("Sotib olmoiqchimisz (HA/YO`Q): ")

    if sotib_olish.lower() == "ha":
        karta_nomer = input("Karta nomerni kiriting: ")
        print(f"Kartangizdan - {karta_nomer} - jami == ${jami:.2f} olindi.")
        print("Supermarket ishlatganingizga rahmat!")
        arava.clear()
    else:
        print("Sotib olish bekor qilindi.")

menyu()
tanlov()




























