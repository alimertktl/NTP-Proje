from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from deneme import Ui_MainWindow
from egzersiz import EgzersizPage
import sqlite3
import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

class AnaPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Veritabanı bağlantısı oluştur
        self.connection = sqlite3.connect("kullanici_veritabani.db")
        self.cursor = self.connection.cursor()

        # Buton tıklama olayları
        self.ui.pushButton_kaydet.clicked.connect(self.kaydet)
        self.ui.pushButton_egzersiz.clicked.connect(self.egzersiz)
        self.ui.pushButton_rapor.clicked.connect(self.rapor_olustur)

        # Tansiyon ve kan şekeri için geçerli aralıklar
        self.min_tansiyon_buyuk = 70
        self.max_tansiyon_buyuk = 200
        self.min_tansiyon_kucuk = 40
        self.max_tansiyon_kucuk = 120
        self.min_kan_sekeri = 50
        self.max_kan_sekeri = 180

        # PDF dosyasının kaydedileceği dizin
        

    def kaydet(self):
        # Kullanıcı tarafından girilen değerleri al
        nabiz = self.ui.comboBox.currentText()
        tansiyon_buyuk = self.ui.lineEdit_tansiyonB.text()
        tansiyon_kucuk = self.ui.lineEdit_tansiyonK.text()
        kan_sekeri = self.ui.lineEdit_kansekeri.text()

        # Değerlerin boş olup olmadığını kontrol et
        if not nabiz or not tansiyon_buyuk or not tansiyon_kucuk or not kan_sekeri:
            QMessageBox.warning(self, "Uyarı", "Lütfen tüm alanları doldurun.")
            return

        # Tansiyon değerlerinin sayısal olup olmadığını ve aralıkta olup olmadığını kontrol et
        if not tansiyon_buyuk.isdigit() or not tansiyon_kucuk.isdigit():
            QMessageBox.warning(self, "Uyarı", "Tansiyon değerleri sayısal olmalıdır.")
            return
        if not (self.min_tansiyon_buyuk <= int(tansiyon_buyuk) <= self.max_tansiyon_buyuk) or \
           not (self.min_tansiyon_kucuk <= int(tansiyon_kucuk) <= self.max_tansiyon_kucuk):
            QMessageBox.warning(self, "Uyarı", f"Tansiyon değerleri {self.min_tansiyon_buyuk}-{self.max_tansiyon_buyuk} / {self.min_tansiyon_kucuk}-{self.max_tansiyon_kucuk} aralığında olmalıdır.")
            return

        # Kan şekeri değerinin sayısal olup olmadığını ve aralıkta olup olmadığını kontrol et
        if not kan_sekeri.isdigit():
            QMessageBox.warning(self, "Uyarı", "Kan şekeri değeri sayısal olmalıdır.")
            return
        if not (self.min_kan_sekeri <= int(kan_sekeri) <= self.max_kan_sekeri):
            QMessageBox.warning(self, "Uyarı", f"Kan şekeri değeri {self.min_kan_sekeri}-{self.max_kan_sekeri} aralığında olmalıdır.")
            return
              


        
        # Veritabanına verileri ekle
        self.cursor.execute("INSERT INTO saglik_olcumleri (nabiz, tansiyon_buyuk, tansiyon_kucuk, kan_sekeri) VALUES ( ?, ?, ?, ?)",
                            (nabiz, tansiyon_buyuk, tansiyon_kucuk, kan_sekeri))
        self.connection.commit()


        # Veritabanından son eklenen veriyi al
        self.cursor.execute("SELECT * FROM saglik_olcumleri ORDER BY id DESC LIMIT 1")
        son_veri = self.cursor.fetchone()

        # Son veriyi label_okuma kısmına yaz
        old_text = self.ui.label_okuma.text()
        new_text = f"Nabız: {son_veri[1]}, Tansiyon (Büyük): {son_veri[2]}, \nTansiyon (Küçük): {son_veri[3]}, Kan Şekeri: {son_veri[4]} \n"
        self.ui.label_okuma.setText(old_text + "\n" + new_text)

    def egzersiz(self):
        #self.hide()  # Ana pencereyi gizle
        self.egzersiz_page = EgzersizPage()  # Egzersiz sayfasını oluştur
        self.egzersiz_page.show()

    def kullanici_bilgileri(self):
        # Kullanıcı bilgilerini al
        self.cursor.execute("SELECT * FROM Kullanicilar ORDER BY id DESC LIMIT 1")
        kullanici_bilgisi = self.cursor.fetchone()
        return kullanici_bilgisi

    def son_olcumleri_getir(self):
        # Veritabanından son eklenen ölçümleri al
        self.cursor.execute("SELECT * FROM saglik_olcumleri ORDER BY id DESC LIMIT 1")
        son_olcumler = self.cursor.fetchone()
        return son_olcumler

    def rapor_olustur(self):
        # Kullanıcı bilgilerini al
        kullanici_bilgisi = self.kullanici_bilgileri()
        if kullanici_bilgisi:
            isim_soyisim = kullanici_bilgisi[1].title()
            soyisim = kullanici_bilgisi [2].title()
            yas = kullanici_bilgisi[3]
            # Kullanıcının son ölçümlerini al
            son_olcumler = self.son_olcumleri_getir()
            if son_olcumler:
                nabiz = son_olcumler[1]
                tansiyon_buyuk = son_olcumler[2]
                tansiyon_kucuk = son_olcumler[3]
                kan_sekeri = son_olcumler[4]
                # Riskli durumdaki ölçümleri belirle
                riskli_durmumlar = []
                if int(tansiyon_buyuk) > 130 or int(tansiyon_buyuk) < 110:
                    riskli_durmumlar.append("Tansiyon (Büyük)")
                if int(tansiyon_kucuk) > 100 or int(tansiyon_kucuk) < 66:
                    riskli_durmumlar.append("Tansiyon (Küçük)")
                if int(kan_sekeri) > 150 or int(kan_sekeri) < 60:
                    riskli_durmumlar.append("Kan Şekeri")

                # Rapor oluştur
                if riskli_durmumlar:
                    mesaj = ""
                    for durum in riskli_durmumlar:
                        if durum == "Tansiyon (Büyük)":
                            mesaj += "\n Büyük tansiyonunuz önerilen değerler dışında, acilen bir uzmana başvurun.\n"
                        elif durum == "Tansiyon (Küçük)":
                            mesaj += "\n Küçük tansiyonunuz önerilen değerler dışında, acilen bir uzmana başvurun.\n"
                        elif durum == "Kan Şekeri":
                            mesaj += "\n Kan şekeri seviyeniz önerilen değerler dışında, acilen bir uzmana başvurun.\n"

                    rapor = f"Adı Soyadı: {isim_soyisim} {soyisim} \nYaş: {yas}\n\n Riskli Durumlar: \n"
                    rapor += "\n".join([f"- {durum}" for durum in riskli_durmumlar]) + "\n\n"
                    rapor += mesaj
                    self.raporu_pdf_olarak_kaydet(rapor)
                    QMessageBox.information(self, "Rapor", "Rapor PDF olarak kaydedildi: rapor.pdf")
                else:
                    QMessageBox.information(self, "Rapor", "Herhangi bir riskli durum bulunmamaktadır.")
            else:
                QMessageBox.warning(self, "Uyarı", "Henüz ölçüm yapılmamış.")
        else:
            QMessageBox.warning(self, "Uyarı", "Kullanıcı bilgisi bulunamadı.")

    def raporu_pdf_olarak_kaydet(self, rapor):
        pdfmetrics.registerFont(TTFont('Calibri', 'calibri.ttf'))
        c = canvas.Canvas("rapor.pdf", pagesize=letter)
        c.setFont("Calibri", 12)
        lines = rapor.split('\n')
        y = 720
        for line in lines:
            c.drawString(100, y, line)
            y -= 15  # Alt satıra geçmek için y koordinatını azalt
        c.save()
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnaPage()
    window.show()
    sys.exit(app.exec_())
