import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('kullanici_veritabani.db')
cursor = conn.cursor()

# Verileri sil
cursor.execute("DELETE FROM saglik_olcumleri;")

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

#Kullanılması tavsiye edilmez