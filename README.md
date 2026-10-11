# LFM (Chirp) Radar Sinyali Simülasyonu & Uyumlu Filtre (Matched Filter) ile Hedef Tespiti

Bu proje; modern radar ve sonar sistemlerinde yaygın olarak kullanılan **Doğrusal Frekans Modülasyonlu (LFM - Linear Frequency Modulation / Chirp)** sinyallerin matematiksel modellemesini ve hedeften dönen zayıflatılmış/gecikmiş yankı (Echo) sinyalinin **Uyumlu Filtre (Matched Filter - Çapraz Korelasyon)** tekniği ile tespit edilerek hedef mesafesinin hesaplanmasını konu almaktadır.

---

## Projenin Amacı ve Temel Konseptler

- **Darbe Sıkıştırma (Pulse Compression):** Geleneksel darbe radarlarında menzil çözünürlüğü darbe genişliğine bağlıyken, LFM sinyallerinde çözünürlük sinyalin **bant genişliğine ($B$)** bağlıdır. Bu sayede uzun darbeler kullanılarak yüksek enerji iletimi sağlanırken aynı zamanda yüksek menzil çözünürlüğü elde edilir.
- **LFM / Chirp Dalgası Üretimi:** Belirli bir darbe süresi ($T$) boyunca frekansı $f_0$'dan $f_1$'e doğrusal olarak artan sinüzoidal dalga formunun modellenmesi.
- **Radar Yankısı (Echo) Simülasyonu:** Gönderilen sinyalin hedefe çarpıp gecikmeli ($\tau$) ve genliği ciddi oranda zayıflamış ($\alpha$) olarak geri dönmesi durumunun modellenmesi.
- **Uyumlu Filtre (Matched Filter) & Menzil Tespiti:** Gelen gürültülü/zayıf yankı sinyali ile referans şablon sinyali (Tx) arasındaki çapraz korelasyonun hesaplanması, tepe noktasından (Peak) uçuş süresinin ($\tau$) bulunması ve radar menzil formülü ($R = \frac{c \cdot \tau}{2}$) ile hedefin mesafesinin saptanması.

---

## Matematiksel Altyapı

### 1. LFM (Chirp) Sinyal Denklemi
Sinyalin anlık frekansı zamanla doğrusal olarak artar:
$$f(t) = f_0 + \mu t, \quad \mu = \frac{B}{T} = \frac{f_1 - f_0}{T}$$

Faz açısı frekansın integrali alınarak bulunur:
$$\theta(t) = 2\pi \int_0^t f(\tau) d\tau = 2\pi \left(f_0 t + \frac{1}{2} \mu t^2\right)$$

Gönderilen sinyal:
$$s(t) = \cos(\theta(t)) = \cos\left(2\pi \left(f_0 t + \frac{1}{2} \frac{B}{T} t^2\right)\right)$$

### 2. Radar Yankısı (Echo / Rx)
Hedef mesafesi $R$ olduğunda sinyalin hedefe gidip dönmesi için geçen gecikme $\tau = \frac{2R}{c}$ kadardır. Yansıma katsayısı ve yol kaybı $\alpha$ olmak üzere alınan sinyal:
$$r(t) = \alpha \cdot s(t - \tau)$$

### 3. Uyumlu Filtre (Matched Filter / Çapraz Korelasyon)
Alınan sinyal ile gönderilen referans sinyalin çapraz korelasyonu (Cross-Correlation):
$$R_{rx, tx}(\tau') = \int_{-\infty}^{\infty} r(t) \cdot s(t - \tau') dt$$

Korelasyon fonksiyonunun maksimum olduğu gecikme değeri ($\tau_{tepe}$), hedefin gidiş-dönüş süresini verir. Hedef mesafesi ($c \approx 3 \times 10^8 \text{ m/s}$):
$$R = \frac{c \cdot \tau_{tepe}}{2}$$

---

## Proje Dosyaları

- [`LFM sinyal kod.py`](file:///Users/oneo/Desktop/Projeler/Kod/LFM%20sinyal/LFM%20sinyal%20kod.py):
  - $f_0 = 100\text{ Hz}$, $f_1 = 3000\text{ Hz}$ frekans aralığında LFM sinyalini üretir.
  - Sinyalin başındaki ($t = 0 - 0.06\text{ s}$) düşük frekanslı bölge ile ortasındaki ($T/2 - T/2 + 0.06\text{ s}$) yüksek frekanslı bölgeyi karşılaştırmalı olarak çizdirir.
- [`LFM sinyali ve ECHO (Kolerasyon).py`](file:///Users/oneo/Desktop/Projeler/Kod/LFM%20sinyal/LFM%20sinyali%20ve%20ECHO%20%28Kolerasyon%29.py):
  - Gönderilen sinyal ($Tx$) ile zayıflatılmış gecikmeli yankı sinyalini ($Rx$) simüle eder.
  - `numpy.correlate` kullanarak Uyumlu Filtre çıkışını hesaplar.
  - Tepe noktasını tespit ederek hedef mesafesini metre ve kilometre cinsinden görsel üzerinde raporlar.

---

## Çıktılar ve Görselleştirme

### 1. Frekans Değişim Analizi
- Dalganın başlangıcında periyot uzun (düşük frekans), zaman ilerledikçe dalgalar sıklaşmakta ve periyot kısalmaktadır (yüksek frekans).

### 2. Matched Filter & Radar Menzil Grafiği
- Alınan sinyal çok zayıf olsa dahi, korelasyon işleminden sonra hedefin bulunduğu gecikme anında çok keskin bir **tepe (Dirac delta benzeri sıkıştırılmış darbe)** oluşur.
- Simülasyonda belirlenen $0.2\text{ s}$ gecikme değeri üzerinden:
$$R = \frac{3 \times 10^8 \times 0.2}{2} = 30,000,000 \text{ m} = 30,000 \text{ km}$$
olarak hedefin konumu kusursuz şekilde doğrulanır.

---

## Kurulum ve Çalıştırma

### Gereksinimler
- Python 3.8+
- `numpy`
- `matplotlib`

```bash
pip install numpy matplotlib
```

### Çalıştırma

1. LFM sinyali ve frekans değişimini görmek için:
```bash
python "LFM sinyal kod.py"
```

2. Radar yankısı ve hedef mesafe tespitini görmek için:
```bash
python "LFM sinyali ve ECHO (Kolerasyon).py"
```

---

## Hazırlayan

- **Efe Anıl Arslan**
- Radar & Haberleşme Sistemleri Sinyal İşleme Çalışması
