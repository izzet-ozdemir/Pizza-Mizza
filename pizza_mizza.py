import random
import csv
import datetime

class clsPizza:
    def __init__(self, pDescription, pPrice):
        self.pDescription = pDescription
        self.pPrice = pPrice

    def getDescription(self):
        return self.pDescription

    def getPrice(self):
        return self.pPrice

class clsMargaritta(clsPizza):
    def __init__(self):
        self.pDescription = 'Mozarella peyniri, Domates'
        self.pPrice = 79.0

class clsClassicPizza(clsPizza):
    def __init__(self):
        self.pDescription = 'Mozarella peyniri, Sosis, Siyah Zeytin, Mısır, Domates'
        self.pPrice = 89.0

class clsTurkPizza(clsPizza):
    def __init__(self):
        self.pDescription = 'Mozarella peyniri, Sucuk, Siyah Zeytin, Mısır, Mantar'
        self.pPrice = 99.0

class clsPizzaMizza(clsPizza):
    def __init__(self):
        self.pDescription = 'Mozarella peyniri, Pastırma, Siyah Zeytin, Mısır, Domates, Yeşil Biber'
        self.pPrice = 109.0

class clsMaterial:
    def __init__(self, pCost):
        self.pCost = pCost

class clsZeytin(clsMaterial):
    def __init__(self):
        self.pCost = 4.0

class clsMantar(clsMaterial):
    def __init__(self):
        self.pCost = 4.0

class clsKırmızıBiber(clsMaterial):
    def __init__(self):
        self.pCost = 4.0

class clsJalapenoBiber(clsMaterial):
    def __init__(self):
        self.pCost = 6.0

class clsSogan(clsMaterial):
    def __init__(self):
        self.pCost = 3.0

class clsMısır(clsMaterial):
    def __init__(self):
        self.pCost = 3.0



def getOption ():
    print('\n\n=== PİZZA MİZZA ===')
    print('[1] Menüyü Gör ')
    print('[2] Sipariş Ver')
    print('[3] Çıkış')
    while True:
        try:
            option = int(input("Seçiminiz : "))
            if 1 <= option <= 3:
                break
            print("Geçersiz seçenek!..")
        except:
            print("Geçersiz giriş!..")
    return option

def addMenu():
    txtMenu = "\n\n=== Pizza Mizza Menü === \n"
    txtMenu = txtMenu + " * Nefis pizzalar sizi bekliyor. Hemen siparişinizi verin! \n"
    txtMenu = txtMenu + "[1] Margarita Pizza : " + clsMargaritta().pDescription + " (" + str(clsMargaritta().pPrice) + " TL) \n"
    txtMenu = txtMenu + "[2] Klasik Pizza : " + clsClassicPizza().pDescription + " (" + str(clsClassicPizza().pPrice) + " TL) \n"
    txtMenu = txtMenu + "[3] Türk Pizza : " + clsTurkPizza().pDescription + " (" + str(clsTurkPizza().pPrice) + " TL) \n"
    txtMenu = txtMenu + "[4] Pizza Mizza: " + clsPizzaMizza().pDescription + " (" + str(clsPizzaMizza().pPrice) + " TL) \n"
    txtMenu = txtMenu + "======================== \n"
    txtMenu = txtMenu + " * Ekstre malzemeler ile lezzetinizi şimdi artırın! \n"
    txtMenu = txtMenu + "[11] Siyah Zeytin \n"
    txtMenu = txtMenu + "[12] Mantar \n"
    txtMenu = txtMenu + "[13] Kırmızı Köz Biber \n"
    txtMenu = txtMenu + "[14] Jalapeno Biber\n"
    txtMenu = txtMenu + "[15] Soğan \n"
    txtMenu = txtMenu + "[16] Mısır \n\n"
    with open("menu.txt", "w") as menu:
        menu.write(txtMenu)
        menu.close()

def getMenu():
    menu = open("menu.txt")
    for txtRec in menu:
        print(txtRec, end="")
    menu.close()

def getPizza():
    print('\n==== PİZZA SEÇENEKLERİMİZ')
    print('[1] Margarita Pizza')
    print('[2] Klasik Pizza ')
    print('[3] Türk Pizza')
    print('[4] Pizza Mizza')
    print('------------------')
    print('==== DİĞER İŞLEMLER')
    print('[5] Ödeme Noktası')
    print('[6] Sipariş İptal')
    try:
        pizzaOption = int(input("Seçiminiz : "))
        if pizzaOption < 1 or pizzaOption > 6:
            print("Hatalı giriş yaptınız. Lütfen tekrar deneyin!\n\n")
            getPizza()
    except:
        print("Hata Oluştu !.. Hata:Pizza")
    return pizzaOption

def getMaterial():
    print('\n==== EKSTRA MALZEME SEÇENEKLERİMİZ')
    print('[11] Siyah Zeytin')
    print('[12] Mantar')
    print('[13] Kırmızı Köz Biber')
    print('[14] Jalapeno Biber')
    print('[15] Soğan')
    print('[16] Mısır')
    print('------------------')
    print('[17] Pizza Menü')

    try:
        materialOption = int(input("Seçiminiz : "))
        if materialOption < 11 or materialOption > 17:
            print("Hatalı giriş yaptınız. Lütfen tekrar deneyin!\n\n")
            getMaterial()
    except:
        print("Hata Oluştu!.. Hata:Material")
    return materialOption

def getPrice(pITEM):
    if pITEM == 'margarita':
        pPrice = clsMargaritta().pPrice
    elif pITEM == 'classic':
        pPrice = clsClassicPizza().pPrice
    elif pITEM == 'turk':
        pPrice = clsTurkPizza().pPrice
    elif pITEM == 'pizzamizza':
        pPrice = clsPizzaMizza().pPrice
    elif pITEM == 'zeytin':
        pPrice = clsZeytin().pCost
    elif pITEM == 'mantar':
        pPrice = clsMantar().pCost
    elif pITEM == 'kbiber':
        pPrice = clsKırmızıBiber().pCost
    elif pITEM == 'jbiber':
        pPrice = clsJalapenoBiber().pCost
    elif pITEM == 'sogan':
        pPrice = clsSogan().pCost
    elif pITEM == 'mısır':
        pPrice = clsMısır().pCost
    return int(pPrice)

def doPayment(pBasket):
    try:
        pOrderID = pBasket["orderID"]
        print('\n==== ÖDEME İŞLEMLERİ')
        showBasket(pBasket)
        print('\n==== Ödeme için bilgilerinizi giriniz')
        pName = str(input("Adınız ve Soyadınız : "))
        pTCID = str(input("TC Kimlik Numaranız: "))
        pKKNO = str(input("Kredi Kartı Numaranız : "))
        pKKPASS = str(input("Kredi Kartı Şifreniz : "))
        pTIME = str(datetime.datetime.now())

        pfilename = "PizzaMizza_Order"+pOrderID+".csv"
        pOrderTitle = ['ORDER_ID', 'CUSTOMER', 'TCID', 'KKNO', 'KK_PASSWORD', 'ORDER_TIME']
        pOrderData = [pOrderID, pName, pTCID, pKKNO, pKKPASS, pTIME]
        with open(pfilename, mode='a') as orderFile:
            order = csv.writer(orderFile)
            order.writerow(pOrderTitle)
            order.writerow(pOrderData)

            pBasketTitle = ['ORDER_ID', 'ITEMS', 'QUANTITY', 'PRICE', 'AMOUNT']
            order.writerow(pBasketTitle)

            for a1, b1 in pBasket.items():
                if a1 == 'orderID':
                    pass
                else:
                    for a2, b2 in b1.items():
                        if int(b2) > 0:
                            if a2 == "qty":
                                pAmount = str(int(b2) * int(getPrice(a1)))
                                pBasketData = [str(pOrderID), a1, str(b2), str(getPrice(a1)), pAmount]
                                order.writerow(pBasketData)
                            else:
                                pAmount = str(int(b2) * int(getPrice(a2)))
                                pBasketData = [str(pOrderID), a1 + "-" + a2, str(b2), str(getPrice(a2)), pAmount]
                                order.writerow(pBasketData)

        print("Ödeme İşleminiz Başarıyla Tamamlandı.")
        result = 1
    except:
        print("Ödeme işleminde hata oluştu. HATA : Payment")
        result = 0

    return result

def showBasket(pBasket):
    print("\nSepetiniz : ")
    print("============ ")
    for a1, b1 in pBasket.items():
        if a1 == 'orderID':
            print("{}\t : {}".format(a1, b1))
        else:
            for a2, b2 in b1.items():
                if int(b2) > 0:
                    if a2 == "qty":
                        print("{} pizza\t : {} adet".format(a1, b2))
                    else:
                        print("{} pizza\t - extra {}\t : {} porsiyon".format(a1, a2, b2))

def makeExtraBasket(pExtra):
    pExtra["zeytin"] = 0
    pExtra["mantar"] = 0
    pExtra["kbiber"] = 0
    pExtra["jbiber"] = 0
    pExtra["sogan"] = 0
    pExtra["mısır"] = 0

def makeBasket():
    basket = {}
    orderID = str(random.randint(1, 9999))
    basket["orderID"] = orderID

    mbMargarita={}
    mbClassic = {}
    mbTurk = {}
    mbPizzaMizza = {}

    mbMargarita["qty"] = 0
    mbClassic["qty"] = 0
    mbTurk["qty"] = 0
    mbPizzaMizza["qty"] = 0

    makeExtraBasket(mbMargarita)
    makeExtraBasket(mbClassic)
    makeExtraBasket(mbTurk)
    makeExtraBasket(mbPizzaMizza)

    basket["margarita"] = mbMargarita
    basket["classic"] = mbClassic
    basket["turk"] = mbTurk
    basket["pizzamizza"] = mbPizzaMizza
    return basket

def addMsg(pMode, pItem):
    if pMode == 'pizza':
        txtMsg = "\nSepetinize 1 adet " + pItem + " pizza eklendi.\n"
    elif pMode == 'extra':
        txtMsg = "Sepetinize ek olarak " + pItem + " eklendi."
    print(txtMsg)

def addOrder():
    basket = makeBasket()
    while True:
        try:
            orderOption = int(getPizza())
            if orderOption == 5:
                pPayment = doPayment(basket)
                if pPayment == 1:
                    break
                else:
                    pass
            elif orderOption == 6:
                pOut = str(input("\nİşleminiz sonucu sepetiniz silinecek. Onaylıyor musunuz? [E/H] : "))
                if pOut in ['H', 'h']:
                    pass
                else:
                    break
            else:
                if orderOption == 1:
                    basket["margarita"]["qty"] += 1
                    addMsg("pizza", "margarita")
                    showBasket(basket)
                    pOut = str(input("\nEkstra malzeme eklemek ister misiniz? [E/H] : "))
                    if pOut in ['H', 'h']:
                        pass
                    else:
                        while True:
                            orderExtra = int(getMaterial())
                            if orderExtra == 11:
                                basket["margarita"]["zeytin"] += 1
                                addMsg("extra", "zeytin")
                                showBasket(basket)
                            elif orderExtra == 12:
                                basket["margarita"]["mantar"] += 1
                                addMsg("extra", "mantar")
                                showBasket(basket)
                            elif orderExtra == 13:
                                basket["margarita"]["kbiber"] += 1
                                addMsg("extra", "kırmızı biber")
                                showBasket(basket)
                            elif orderExtra == 14:
                                basket["margarita"]["jbiber"] += 1
                                addMsg("extra", "jalapeno biber")
                                showBasket(basket)
                            elif orderExtra == 15:
                                basket["margarita"]["sogan"] += 1
                                addMsg("extra", "soğan")
                                showBasket(basket)
                            elif orderExtra == 16:
                                basket["margarita"]["mısır"] += 1
                                addMsg("extra", "mısır")
                                showBasket(basket)
                            elif orderExtra == 17:
                                #getPizza()
                                #showBasket(basket)
                                break

                elif orderOption == 2:
                    basket["classic"]["qty"] += 1
                    addMsg("pizza", "classic")
                    showBasket(basket)
                    pOut = str(input("\nEkstra malzeme eklemek ister misiniz? [E/H] : "))
                    if pOut in ['H', 'h']:
                        pass
                    else:
                        while True:
                            orderExtra = int(getMaterial())
                            if orderExtra == 11:
                                basket["classic"]["zeytin"] += 1
                                addMsg("extra", "zeytin")
                                showBasket(basket)
                            elif orderExtra == 12:
                                basket["classic"]["mantar"] += 1
                                addMsg("extra", "mantar")
                                showBasket(basket)
                            elif orderExtra == 13:
                                basket["classic"]["kbiber"] += 1
                                addMsg("extra", "kırmızı biber")
                                showBasket(basket)
                            elif orderExtra == 14:
                                basket["classic"]["jbiber"] += 1
                                addMsg("extra", "jalapeno biber")
                                showBasket(basket)
                            elif orderExtra == 15:
                                basket["classic"]["sogan"] += 1
                                addMsg("extra", "soğan")
                                showBasket(basket)
                            elif orderExtra == 16:
                                basket["classic"]["mısır"] += 1
                                addMsg("extra", "mısır")
                                showBasket(basket)
                            elif orderExtra == 17:
                                #getPizza()
                                #showBasket(basket)
                                break

                elif orderOption == 3:
                    basket["turk"]["qty"] += 1
                    addMsg('pizza', 'turk')
                    pOut = str(input("\nEkstra malzeme eklemek ister misiniz? [E/H] : "))
                    if pOut in ['H', 'h']:
                        pass
                    else:
                        while True:
                            orderExtra = int(getMaterial())
                            if orderExtra == 11:
                                basket["turk"]["zeytin"] += 1
                                addMsg("extra", "zeytin")
                                showBasket(basket)
                            elif orderExtra == 12:
                                basket["turk"]["mantar"] += 1
                                addMsg("extra", "mantar")
                                showBasket(basket)
                            elif orderExtra == 13:
                                basket["turk"]["kbiber"] += 1
                                addMsg("extra", "kırmızı biber")
                                showBasket(basket)
                            elif orderExtra == 14:
                                basket["turk"]["jbiber"] += 1
                                addMsg("extra", "jalapeno biber")
                                showBasket(basket)
                            elif orderExtra == 15:
                                basket["turk"]["sogan"] += 1
                                addMsg("extra", "soğan")
                                showBasket(basket)
                            elif orderExtra == 16:
                                basket["turk"]["mısır"] += 1
                                addMsg("extra", "mısır")
                                showBasket(basket)
                            elif orderExtra == 17:
                                #getPizza()
                                #showBasket(basket)
                                break

                elif orderOption == 4:
                    basket["pizzamizza"]["qty"] += 1
                    addMsg("pizza", "pizzamizza")
                    pOut = str(input("\nEkstra malzeme eklemek ister misiniz? [E/H] : "))
                    if pOut in ['H', 'h']:
                        pass
                    else:
                        while True:
                            orderExtra = int(getMaterial())
                            if orderExtra == 11:
                                basket["pizzamizza"]["zeytin"] += 1
                                addMsg("extra", "zeytin")
                                showBasket(basket)
                            elif orderExtra == 12:
                                basket["pizzamizza"]["mantar"] += 1
                                addMsg("extra", "mantar")
                                showBasket(basket)
                            elif orderExtra == 13:
                                basket["pizzamizza"]["kbiber"] += 1
                                addMsg("extra", "kırmızı biber")
                                showBasket(basket)
                            elif orderExtra == 14:
                                basket["pizzamizza"]["jbiber"] += 1
                                addMsg("extra", "jalapeno biber")
                                showBasket(basket)
                            elif orderExtra == 15:
                                basket["pizzamizza"]["sogan"] += 1
                                addMsg("extra", "soğan")
                                showBasket(basket)
                            elif orderExtra == 16:
                                basket["pizzamizza"]["mısır"] += 1
                                addMsg("extra", "mısır")
                                showBasket(basket)
                            elif orderExtra == 17:
                                #getPizza()
                                #showBasket(basket)
                                break
        except:
            print('Hata Oluştu!.. Hata : order')
        showBasket(basket)

def main():
    try:
        addMenu()
        while True:
            option = getOption()
            if option == 3:
                break
            {1: getMenu, 2: addOrder}[option]()
    except:
        print('Hata Oluştu!.. Hata : Main')
    finally:
        print('Teşekkürler. Yine bekleriz!...')

main()