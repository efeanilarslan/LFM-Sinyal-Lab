import numpy as np
import matplotlib.pyplot as plt

f0 = 100
f1 = 3000
f_ornek = f1*6
dalga_suresi  = 0.3
B = f1 - f0
gecikme = 0.2
azalma = 0.009
ornek_nokta = int(f_ornek*dalga_suresi)
t = np.arange(ornek_nokta)/f_ornek
q  = 2*np.pi * ( f0*t + 1/2 *(B/dalga_suresi)*t**2 )
tx = np.cos(q)

gecikme_ornek = int(round(gecikme * f_ornek))
rx = np.zeros(ornek_nokta + gecikme_ornek)
rx[gecikme_ornek:gecikme_ornek + ornek_nokta] += azalma * tx

korelasyon = np.correlate(rx, tx, mode='full')
kaymalar = np.arange(-(len(tx)-1), len(rx))
abs_korelasyon = np.abs(korelasyon)

maske_pozitif = kaymalar >= 0
kaymalar_pozitif = kaymalar[maske_pozitif]
korelasyon_pozitif = abs_korelasyon[maske_pozitif]

tepe_indeks = np.argmax(korelasyon_pozitif)
tepe_gecikme = kaymalar_pozitif[tepe_indeks] / f_ornek

c = 300000000
R_m  = c * tepe_gecikme / 2.0
R_km = R_m / 1000.0

plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(t*1e3, tx)
plt.title("Gönderilen LFM")
plt.xlabel("Zaman (ms)"); plt.ylabel("Genlik"); plt.grid(True)

plt.subplot(3,1,2)
time_rx = np.arange(len(rx))/f_ornek
plt.plot(time_rx*1e3, rx)
plt.title("Alınan Sinyal")
plt.xlabel("Zaman (ms)"); plt.ylabel("Genlik"); plt.grid(True)

plt.subplot(3,1,3)
plt.plot(kaymalar/f_ornek*1e3, abs_korelasyon)
plt.title("Matched Filter Çıkışı")
plt.xlabel("Gecikme (ms)"); plt.ylabel("|Korelasyon|"); plt.grid(True)
plt.axvline(tepe_gecikme*1e3, color='r', linestyle='--', label="Tespit edilen gecikme")
plt.legend()

text_str = f"Mesafe (c≈3e8 m/s):\n{R_m:.1f} m  (~{R_km:.3f} km)"
plt.gca().text(0.98, 0.02, text_str, transform=plt.gca().transAxes,
               ha='right', va='bottom', fontsize=10,
               bbox=dict(boxstyle="round,pad=0.3", fc="w", ec="k", alpha=0.7))

plt.tight_layout();plt.show()
