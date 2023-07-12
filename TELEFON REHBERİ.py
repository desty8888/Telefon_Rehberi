telefon_numarası = {"BOT1":"05393745099", "BOT2":"05324813323", "BOT3":"05056290314", "BOT4":"05055943633", "BOT5":"05255253633"}
question = input("Kişiyi Arayın.")
question = question.upper()
if question in telefon_numarası.keys():
    print(telefon_numarası[question])
else:
    print("Aradığınız Kişi Bulunamadı , Lütfen Tekrar Deneyin.")    

