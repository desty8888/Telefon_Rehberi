telefon_numarası = {"BOT1":"05393742399", "BOT2":"05324813223", "BOT3":"05056290014", "BOT4":"05055941233", "BOT5":"05255251233"}
question = input("Kişiyi Arayın.")
question = question.upper()
if question in telefon_numarası.keys():
    print(telefon_numarası[question])
else:
    print("Aradığınız Kişi Bulunamadı , Lütfen Tekrar Deneyin.")    

