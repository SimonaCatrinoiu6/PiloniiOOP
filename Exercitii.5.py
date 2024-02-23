# Sesiunea 5 Exercitii ( functii si exceptii )
# Creati o metoda care returneaza suma a 2 numere.
#
# def suma_numere_2(a, b):
#     suma = a + b
#     return suma
#
#
# total = suma_numere_2(3, -5)
# print(total)
# print("-----" * 10)
#
#
# # Creati o metoda care returneaza rezultatul inmultirii a trei numere
# def inmultire_numere(a, b, c):
#     inmultire = a * b * c
#     return inmultire
#
#
# print(inmultire_numere(a=2, b=4, c=-5))

dict = {
    "apa": " Lichid incolor, fără gust și fără miros, compus hidrogenat al oxigenului, care formează unul dintre învelișurile Pământului.",
    "pamant": "Scoarța globului terestru, partea de uscat a globului terestru; suprafața lui (împreună cu atmosfera) pe care trăiesc oamenii și alte vietăți.",
    "zebra": "Nume generic dat speciilor de cai sălbatici africani cu blana vărgată cu benzi alternative, deschise și închise; animal care face parte din aceste specii"
}
# Creati un scurt program care sa consulte cuvinte citite de la tastatura in dictionar.
cuvant=input("Introduceti un cuvant: ")
print(dict[cuvant])
print(dict.values())
print(dict.keys())