#Superclass Pasar Online
class PasarOnline():
    
    def __init__(self, nama_toko, jenis_dagangan ) :
        self.nama_toko = nama_toko
        self.jenis_dagangan = jenis_dagangan

#Subclass Pasar Online Shopee dan Lazada
class PasarOnline_Shopee(PasarOnline):
    pass

class PasarOnline_Lazada(PasarOnline):
    pass

Kanaya = PasarOnline("Toko : Kanaya", "Jenis dagang : Hijab")
BeautyCan = PasarOnline_Shopee("Toko : BeautyCan", "Jenis dagang : Skincare dan Make up")
AllCloth = PasarOnline_Lazada("Toko : AllCloth", "Jenis dagang : Baju dan Celana")

#Output
print(Kanaya.nama_toko, Kanaya.jenis_dagangan)
print(BeautyCan.nama_toko, BeautyCan.jenis_dagangan)
print(AllCloth.nama_toko, AllCloth.jenis_dagangan)
