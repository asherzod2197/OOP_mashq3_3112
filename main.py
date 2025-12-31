class Telefon:
    def __init__(self):
        self.batareya = 100

    def ishlat(self, foiz):
        self.batareya = max(0, self.batareya - foiz)

    def zaryadla(self):
        self.batareya = 100

    def holat(self):
        print(f"🔋 Batareya: {self.batareya}%")


telefon1 = Telefon()

telefon1.holat()
telefon1.ishlat(30)
telefon1.holat()
telefon1.zaryadla()
telefon1.holat()
