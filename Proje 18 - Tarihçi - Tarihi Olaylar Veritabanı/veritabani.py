import sqlite3

def reset_database():
    try:
        # Veritabanına bağlan
        db_connection = sqlite3.connect("tarih.db")
        cursor = db_connection.cursor()
        
        # Tabloyu sil
        cursor.execute("DROP TABLE IF EXISTS tarihler")
        
        # Yeni tabloyu oluştur
        create_table_query = """
        CREATE TABLE IF NOT EXISTS tarihler (
            olay_no INTEGER PRIMARY KEY,
            sahsiyet TEXT,
            yasadigi_donem TEXT,
            olay_adi TEXT,
            tarih TEXT,
            donem_adi TEXT,
            baslangic TEXT,
            bitis TEXT
        );
        """
        cursor.execute(create_table_query)
        
        # Değişiklikleri kaydet ve bağlantıyı kapat
        db_connection.commit()
        db_connection.close()
        
        print("Veritabanı sıfırlandı ve yeniden oluşturuldu.")
    except Exception as e:
        print("Veritabanı sıfırlama işlemi başarısız oldu:", str(e))

# Veritabanını sıfırla ve tekrar yükle
reset_database()
