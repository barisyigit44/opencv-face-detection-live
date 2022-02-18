# Opencv kütüphanesini import eder.
import cv2


# Casecade dosyamızı tanımlar.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Kameramızı okuyup bir değişkene atadık
cap = cv2.VideoCapture(0)

# Fps değerini verir.
fps = cap.get(cv2.CAP_PROP_FPS)
while True:
    # Görüntünün o anki fotoğrafını çekip img'e aktarır
    ret,img = cap.read()

    # Fps değerini ekrana yazar.
    cv2.putText(img,str(fps) + " fps", (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255,2)
    
    # Fotoğrafımızı gri formata çevirir.
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Fotoğraftaki yüzleri bulur. Bulduğu yüzlerin sol üstünden kordinatı alıp (x,y) olarak atar.
    # Yüzün büyüklüğü (w,h) olarak saklar.
    # Yani faces değişkeninde dört ayrı değerin listesi tutulmakta.
    # scaleFactor verilen görüntünün %10 oranında boyutunun azaltılması anlamına gelmektedir.
    # Diğer parametreler için https://docs.opencv.org/2.4.13.2/modules/objdetect/doc/cascade_classification.html#cv2.CascadeClassifier.detectMultiScale
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.06, minNeighbors=4)

    # Tüm kordinat ve büyüklük verilerini döngüye alıyoruz.
    for (x,y,w,h) in faces:
        # rectangle fonksiyonu dikdörtgen çizmek için kullanılır.()
        # (fotoğrafın ismi, koordinatları, karşı kordinatları, rengi, kalınlığı, (istenirse lineType = LINE_8 ile çizgi tipi eklenebilir))
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,255,0), 5)

    # İlk argüman pencerenin ismi, İkinci argüman pencerede gösterilecek olan resmin ismi.
    cv2.imshow('Face Detection', img) 

    # Esc ile programı sonlandırır.
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()



