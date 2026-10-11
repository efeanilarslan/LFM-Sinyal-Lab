import numpy as np
import matplotlib.pyplot as plt

f0 = 100
f1 = 3000
f_ornek = f1*6
dalga_suresi  = 0.5
B = f1 - f0

ornek_noktalar_arasi_zaman = 1/f_ornek
ornek_noktalar = int(f_ornek*dalga_suresi)
t = np.arange(ornek_noktalar)*ornek_noktalar_arasi_zaman

q = 2*np.pi * ( f0*t + (1/2)*(B / dalga_suresi)*t**2)
sinyal = np.cos(q)

fig, axs = plt.subplots(3, 1, figsize=(15,10))

axs[0].plot(t, sinyal, linewidth=0.8)
axs[0].set_title("LFM sinyali")
axs[0].set_xlabel("Zaman (saniye)")
axs[0].set_ylabel("Genlik")
axs[0].grid(True)

axs[1].plot(t[int(0.00*f_ornek):int(0.06*f_ornek)], sinyal[int(0.00*f_ornek):int(0.06*f_ornek)])
axs[1].set_title("t=0 ile 0.06 arası frekans değişimi")
axs[1].set_xlabel("Zaman (saniye)")
axs[1].set_ylabel("Genlik")
axs[1].grid(True)

axs[2].plot(t[int(dalga_suresi/2*f_ornek):int(((dalga_suresi/2) + 0.06)*f_ornek)], sinyal[int(dalga_suresi/2*f_ornek):int(((dalga_suresi/2) + 0.06)*f_ornek)])
axs[2].set_title("T/2 ile T/2 + 0.06 saniye arası frekans değişimi")
axs[2].set_xlabel("Zaman (saniye)")
axs[2].set_ylabel("Genlik")
axs[2].grid(True)

plt.tight_layout()
plt.show()