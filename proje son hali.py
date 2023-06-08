calis = 1
giris = 1

class Sistem:
    def __init__(self):
        self.kullanicilar = []
        self.mevcut_kullanici = ""
        self.ihtiyaclar = {}

    def ad(self):
        kullanici_adi = input("Kullanıcı adı: ").lower()
        return kullanici_adi

    def sifre(self):
        sifre = input("Şifre: ").lower()
        return sifre

    def menu_goster(self):
        menu = (
        "1. Sisteme üye ol",
        "2. Sisteme giriş yap",
        "3. Şifremi unuttum",
        "4. Programı kapat"
        )
        for secenek in menu:
            print(secenek)

    def uye_ol(self):
        kullanici_adi = self.ad()
        for kullanici in self.kullanicilar:
            if kullanici[0] == kullanici_adi:
                print("Bu kullanıcı adı zaten alınmış.\n")
                return
        sifre = self.sifre()
        self.kullanicilar.append([kullanici_adi, sifre])
        print("Üyelik başarıyla oluşturuldu.\n")
        
    def kullanicilari_listele(self):
        for kullanici in self.kullanicilar:
            print("{}: Şifre: {}".format(kullanici[0], kullanici[1]))

    def kullanici_sil(self):
        kullanici_adi = input("Silinecek kullanıcının adını giriniz: ").lower()
        sifre = input("Şifre: ").lower()
        
        for kullanici in self.kullanicilar:
            if kullanici[0] == kullanici_adi and kullanici[1] == sifre:
                self.kullanicilar.remove(kullanici)
                print("Kullanıcı hesabı başarıyla silindi.")
                return  
            
    def admin_girisi(self):
            print("Hoş geldin admin!")
            self.mevcut_kullanici = "admin"
            
            while True:
                secim = input("1. Kayıtlı kullanıcılarını ve şifrelerini görüntüle\n"
                              "2. Kullanıcı hesaplarını sil\n"
                              "3. Hesaptan çıkış\n"
                              "seçim: ")
                
                if secim == "1":
                    self.kullanicilari_listele()
                elif secim == "2":
                    self.kullanici_sil()
                elif secim == "3":
                    self.mevcut_kullanici = ""
                    break
                else:
                    print("Hatalı seçim. Lütfen tekrar deneyin.")
    
        
    def giris_yap(self):
        kullanici_adi = self.ad()
        sifre = self.sifre()
        for kullanici in self.kullanicilar:
            if kullanici[0] == kullanici_adi and kullanici[1] == sifre:
                continue
            else:
                print("Kullanıcı adı veya şifre hatalı.\n")
                break
            
        for kullanici in self.kullanicilar:
            if kullanici[0] == kullanici_adi and kullanici[1] == sifre:
                if not kullanici_adi == "admin":
                    print("Hoş geldin {}\n".format(kullanici[0]))
                    self.mevcut_kullanici = kullanici[0]
                    global giris
                    giris = 0
                    break 
                
                elif kullanici_adi == "admin":    
                    sistem.admin_girisi()
                    

    def sifremi_unuttum(self):
        kullanici_adi = self.ad()
        for kullanici in self.kullanicilar:
            if kullanici[0] == kullanici_adi:
                yeni_sifre = input("Yeni şifre: ").lower()
                kullanici[1] = yeni_sifre
                print("Şifreniz başarıyla güncellendi.\n")
                return
        print("Bu kullanıcı adı sistemde kayıtlı değil.\n")

    def ihtiyac_ekle(self):
        ihtiyac = input("İhtiyaç malzemesi girin: ").lower()
        adet = int(input("Adet girin: "))
        if ihtiyac not in self.ihtiyaclar:
            self.ihtiyaclar[ihtiyac] = {'istenen': 0, 'mevcut': 0}
        self.ihtiyaclar[ihtiyac]['istenen'] += adet
        
    def tedarik(self):
        ihtiyac = input("Tedarik edilen ihtiyaç malzemesi girin: ").lower()
        adet = int(input("Adet girin: "))
        if ihtiyac not in self.ihtiyaclar:
            self.ihtiyaclar[ihtiyac] = {'istenen': 0, 'mevcut': 0}
        self.ihtiyaclar[ihtiyac]['mevcut'] += adet        

    def dagitim(self):
        ihtiyac = input("Dağıtılan ihtiyaç malzemesi girin: ").lower()
        adet = int(input("Adet girin: "))
        if ihtiyac not in self.ihtiyaclar:
            print("Bu ihtiyaç sistemde kayıtlı değil.")
        elif adet > self.ihtiyaclar[ihtiyac]['mevcut']:
            print("Girilen adet mevcut adetten fazla.")
        else:
            self.ihtiyaclar[ihtiyac]['mevcut'] -= adet
            print("Dağıtım başarıyla gerçekleştirildi.")
    
    def bilgileri_goruntule(self):
        for ihtiyac, deger in self.ihtiyaclar.items():
            print("{}: İstenen: {}, Mevcut: {}".format(ihtiyac, deger['istenen'], deger['mevcut']))        

                
sistem = Sistem()

import pandas as pd

# Dosya yolunu belirtin
dosya_yolu = r'C:\Users\Serhat\Desktop\üniversite bilişi\algoritma\proje\kullanici_kaydi.csv'

# CSV dosyasını oku, noktalı virgül ile ayrılmış değerler için sep parametresini kullan
df = pd.read_csv(dosya_yolu, sep=';')

print(df.columns)
# DataFrame'deki her bir satır için
for index, row in df.iterrows():
    # Kullanıcıyı listeye ekle
    kullanici_adi = row['kullanici_adi']  # KullaniciAdi sütununu varsayıyoruz
    sifre = str(row['sifre'])  # Sifre sütununu varsayıyoruz
    sistem.kullanicilar.append([kullanici_adi, sifre])
    
while calis == 1:
    while giris == 1:
        sistem.menu_goster()
        secim = input("Seçiminiz (1-4): ")
    
        if secim == "1":
            sistem.uye_ol()        
        elif secim == "2":
            sistem.giris_yap()
        elif secim == "3":
            sistem.sifremi_unuttum()
        elif secim == "4":
            print("Program kapatılıyor.")
            calis = 0
            break
        else:
            print("Hatalı seçim.")
              
    while sistem.mevcut_kullanici != "":
        print("1. İhtiyaç malzemesi ekle")
        print("2. Tedarik bilgisi gir")
        print("3. Dağıtım bilgisi gir")
        print("4. Bilgileri görüntüle")
        print("5. Çıkış")
        secim = input("\nSeçiminizi yapın (1-5): ")
    
        if secim == "1":
            sistem.ihtiyac_ekle()
            
        elif secim == "2":
            sistem.tedarik()
        elif secim == "3":
            sistem.dagitim()
        elif secim == "4":
            sistem.bilgileri_goruntule()
        elif secim == "5":
            print("Çıkış yapılıyor.")
            sistem.mevcut_kullanici = ""
            giris = 1
        else:
            print("Hatalı seçim.")