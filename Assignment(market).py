def print_ishlar():
    print("""\nNima vazifa bajarish kerak.
          a - meva olish
          b - meva sotish
          c - bitta meva tekshirish
          d - hamma meva tekshirish
          e - meva narxini o'zgartirish
          f - topgan pul ko'rsatish
          g - chiqish""")
    ish = input("Vazifa harfini kiriting: ").lower() # adashib katta harf kiritsa, kichik harfga almashtirib qo'yamiz
    return ish


def meva_olish(magazin_lugat):
    print("\n**** Meva qo'shyapmiz! ****")
    meva = input("Nima meva oldingiz: ")
    meva_soni = input("necha kg oldinggiz: ")
    meva_narxi = input("nech pul: ")
    if not meva_soni.isdigit() or not meva_narxi.isdigit():
        print("faqat son kiriting")
    else:
        if meva not in magazin_lugat:
            magazin_lugat[meva] = [meva_soni, meva_narxi]
        else:
            magazin_lugat[meva][0] =int(magazin_lugat[meva][0]) + int(meva_soni)
        print("Meva qo'shildi!")
    # Qolgan ko'dni shu yerga yozing, lug'atni o'zgartirish, print qilishlar shu yerda bo'ladi
    return magazin_lugat

def meva_sotish(magazin_lugat):
        print("\n**** Meva sotyapmiz! ****")
        meva = input("Nima meva sotdingiz: ")
        nechta = input("necha kg meva sotdinggiz:")
        if meva in magazin_lugat:
            if int(magazin_lugat[meva][0]) > int(nechta):
                magazin_lugat[meva][0] = str(int(magazin_lugat[meva][0]) - int(nechta))
            elif int(magazin_lugat[meva][0]) == int(nechta):
                del magazin_lugat[meva]
            else:
                print("meva yetarli emas")
                return

            hisob = int(magazin_lugat[meva][1]) * int(nechta)
            if 'topgan_pul' in magazin_lugat:
                magazin_lugat['topgan_pul'] = int(magazin_lugat['topgan_pul']) + int(hisob)
            else:
                magazin_lugat['topgan_pul'] = int(hisob)
            return magazin_lugat
        else:
            print("bunday meva mavjud emas")
            return magazin_lugat
    # Qolgan ko'dni shu yerga yozing, lug'atni o'zgartirish, print qilishlar shu yerda bo'ladi

def bitta_meva_tekshirish(magazin_lugat):
    print("\n**** Meva ko'rsatish! ****")
    meva = input("Qaysi mevani ko'rmoqchisiz: ")
    if meva in magazin_lugat:
        print(meva,'-',(magazin_lugat[meva][0]),'kg',(magazin_lugat[meva][1]),"som")
    elif meva not in magazin_lugat:
         print("bunday meva mavjud emas")
    # Qolgan ko'dni shu yerga yozing, lug'atni o'zgartirish, print qilishlar shu yerda bo'ladi

    return magazin_lugat

def hamma_meva_tekshirish(magazin_lugat):
    for meva, malumotlar in magazin_lugat.items():
        if isinstance(malumotlar, list):
           kg = malumotlar[0]
           pul = malumotlar[1]
           print(f"{meva} - {kg} kg - {pul} so’m")
    print("\n**** Hamma meva ko'rsatish! ****")
    # Qolgan ko'dni shu yerga yozing, lug'atni o'zgartirish, print qilishlar shu yerda bo'ladi

    return magazin_lugat

def meva_narxi_ozgartirish(magazin_lugat):
    print("\n**** Meva narxini o'zgartiryapmiz! ****")
    meva = input("Qaysi mevani narxini o'zgartirasiz: ")
    yangi_narx = input("yangi_narx:")
    if not yangi_narx.isdigit():
        print("faqat son kiriting")
    else:
        if meva in magazin_lugat:
            magazin_lugat[meva][1] = yangi_narx
        elif meva not in magazin_lugat:
            print("bunday meva mavjud emas")
    # Qolgan ko'dni shu yerga yozing, lug'atni o'zgartirish, print qilishlar shu yerda bo'ladi

    return magazin_lugat

# Bu funksiyani o'zim yozib qo'ydim
def topgan_pul_korsatish(magazin_lugat):
    print("\n**** Topgan pul ko'rsatish! ****")
    topgan_pul = magazin_lugat["topgan_pul"] # lug'at ichidan topamiz
    print(f"Topgan pulingiz {topgan_pul} - so'm.") # Magazinchiga ko'rsatamiz

    return magazin_lugat # O'zgarib qolmasin deb qaytaramiz

def magazin_dastur():
    # Lu'gat yaratamiz
    # Hechtima yo'q, topgan pulimizham 0 so'm hozircha
    magazin_lugat = {"topgan_pul":0}
    
    print("Salom!")
    # Ishlarni print qilamiz va kiritgan javobini olamiz
    ish = print_ishlar()

    while ish != "g": # chiqish deguncha ishlaydi
        if ish == "a":
            magazin_lugat = meva_olish(magazin_lugat)
        elif ish == "b":
            magazin_lugat = meva_sotish(magazin_lugat)
        elif ish == "c":
            magazin_lugat = bitta_meva_tekshirish(magazin_lugat)
        elif ish == "d":
            magazin_lugat = hamma_meva_tekshirish(magazin_lugat)
        elif ish == "e":
            magazin_lugat = meva_narxi_ozgartirish(magazin_lugat)
        elif ish == "f":
            magazin_lugat = topgan_pul_korsatish(magazin_lugat)
        else: # boshqa harf/raqam kiritibti
            print("Ko'rsatilgan harflardan bittasini kiriting!")
        
        # Yana nima qilishni so'raymiz
        ish = print_ishlar()

    # Chiqishni tanlabti
    print(f"\nRahmat! Bugun {magazin_lugat['topgan_pul']} so'm topdingiz.")

magazin_dastur()