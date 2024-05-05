import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('kullanici_veritabani.db')
cursor = conn.cursor()

# Kullanıcı bilgileri ve sağlık ölçümlerini birleştirerek eşleşen id'lere sahip verileri al
cursor.execute("SELECT Kullanicilar.isim, Kullanicilar.soyisim, Kullanicilar.yas, Kullanicilar.cinsiyet, \
                saglik_olcumleri.nabiz, saglik_olcumleri.tansiyon_buyuk, saglik_olcumleri.tansiyon_kucuk, saglik_olcumleri.kan_sekeri \
                FROM Kullanicilar LEFT JOIN saglik_olcumleri ON Kullanicilar.id = saglik_olcumleri.id")

eslesen_veriler = cursor.fetchall()

# Eşleşen verileri ekrana yazdır
for veri in eslesen_veriler:
    print("İsim:", veri[0])
    print("Soyisim:", veri[1])
    print("Yaş:", veri[2])
    print("Cinsiyet:", veri[3])
    print()
    print("Nabız:", veri[4] if veri[4] else "N/A")
    print("Tansiyon (Büyük):", veri[5] if veri[5] else "N/A")
    print("Tansiyon (Küçük):", veri[6] if veri[6] else "N/A")
    print("Kan Şekeri:", veri[7] if veri[7] else "N/A")
    print()


    #veritabanını görüntülemek için cmd kısmına kodun yerini girin örnek : cd C:\Users\bense\OneDrive\Masaüstü\proje12
    #daha sonra python veritabani.py yazmanız yeterli olacaktır
