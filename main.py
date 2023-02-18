#SAKIN İLK SATIRI SİLMEYİN! Bu,programın doğru çalışmasını engelleyebilr.
#Lütfen son satırdan sonra enter a basıp o satırı boş bırakın toksa en son satırı okuyacakken hata verir.
######################################################################################################################
######################################################################################################################
#Örnek csvread.txt dosyası içeriği:
"""
İsim,Yaş
Deneme1,34
Deneme3,45
"""
with open("csvread.txt",encoding="utf-8",mode="r") as dosya:
    lines = dosya.readlines()
    linecount = len(lines)
    for i in range(1,linecount):
        bilgitoplam = lines[i]
        csvtoplam = bilgitoplam.split("\n")
        adyas = csvtoplam[0]
        ad,yas = adyas.split(",")
        print(f"{i}.kişi // Adı: {ad} // Yaşı: {yas}")

