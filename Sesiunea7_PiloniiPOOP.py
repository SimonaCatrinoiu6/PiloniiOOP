from abc import abstractmethod, ABC


class Gradinita(ABC):
    @abstractmethod
    def joaca(self):
        raise NotImplementedError  # am instruit sistemul sa returneze o eroare specifica daca metoda nu este implementata


    def somn(self):
        print("Copii dorm intre 2 jumate si 3 fara un sfert.")


    @abstractmethod
    def activitati(self):
        pass


class Gradinita_privata(Gradinita):
    nr_copii = 0        #Definirea unui atribut public de clasa
    _adresa = None       #Definirea unui atribut protected de clasa
    __orar = "9-17"         #Definirea unui atribut privat de clasa

    def get_orar(self):
        return self.__orar

    def set_orar(self,orar_nou):
        self.__orar = orar_nou
    def joaca(self):
        print("copiii alearga")

    def activitati(self):
        print("Copiii coloreaza")


class Gradinita_publica(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("copiii sar coarda")

    def activitati(self):
        print("Copiii canta")
gradinita_1 = Gradinita_publica()
gradinita_1.somn()

gradinita_2 = Gradinita_privata()
gradinita_2.activitati()
gradinita_2.joaca()
print("-----" * 10)
gradinita_2.nr_copii = 100
gradinita_2._adresa = "Strada Trandafirilor, Nr.14"
print(F"Numarul de copii este:{gradinita_2.nr_copii}")
print(F"Adresa gradinitei este:{gradinita_2._adresa}")
print("-----" * 10)
print(F"Orarul gradinitei este:{gradinita_2.get_orar()}")
#   Modificam orarul gradinitei private(Noul Orar: 8-18)
orar_nou = "8-18"
gradinita_2.set_orar(orar_nou)
print(F"Noul Orar al gradinitei este:{gradinita_2.get_orar()}")
gradinita_3 = Gradinita_privata()
print(gradinita_3.get_orar())
print(gradinita_3.nr_copii)