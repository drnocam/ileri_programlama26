"""
Matris Carpimi Tutorial

Bu dosya, matris carpimi kavramini gunluk hayattan bir ornek uzerinde anlatmaktadir.
Ornek: Haftanin gunlerinde 5 farkli urunun satislari

Matris Carpimi Nedir?
---------------------
Iki matrisin carpimi, birinci matrisin satirlari ile ikinci matrisin sutunlari arasinda
yapilan skaler carpim islemidir. Sonuc matrisinin boyutu:
(m x n) * (n x p) = (m x p)

Bu tutorialda ogrenecegimiz:
1. Matris veri yapisi ve temel kavramlar
2. Matris carpimi nasil yapilir
3. Gercek hayattan ornek: Gunler ve urunler
4. Genel matris carpimi fonksiyonu
"""

import pprint

print("=" * 70)
print("MATRIS CARPIMI TUTORIAL - Haftalik Satis Analizi")
print("=" * 70)

print("\n[1] MATRIS KAVRAMI VE ORNEK VERI")
print("-" * 50)
print("""
Matris, satir ve sutunlardan olusan dikdortgen bir sayi dizisidir.
Bizim ornegimizde:
- Satirlar: Haftanin 7 gunu (Pazartesi - Pazar)
- Sutunlar: 5 farkli urun (Urun A, B, C, D, E)

Satislar matrisimiz (7 gun x 5 urun):
Her hucre, o gunde o urunden satilan adet sayisini gosterir.
""")

print("\n[2] VERI TANIMLAMA")
print("-" * 50)

gunler = ["Pazartesi", "Sali", "Carsamba", "Persembe", "Cuma", "Cumartesi", "Pazar"]
urunler = ["Urun A", "Urun B", "Urun C", "Urun D", "Urun E"]

print(f"Gunler: {gunler}")
print(f"Urunler: {urunler}")

satis_matrisi = [
    [120, 85, 90, 45, 30],   # Pazartesi
    [110, 80, 95, 50, 35],  # Sali
    [130, 90, 85, 55, 40],  # Carsamba
    [140, 95, 100, 60, 45], # Persembe
    [160, 110, 120, 70, 55],# Cuma
    [180, 130, 140, 85, 65],# Cumartesi
    [150, 110, 115, 75, 50] # Pazar
]

print("\n[3] SATIS MATRISI (7 gun x 5 urun)")
print("-" * 50)
print("Matrisin her satiri bir gunu, her sutunu bir urunu temsil eder.")
print("Ornegin, 3. satir (Carsamba), 2. sutun (Urun B) degeri 90'dir.")
print("Bu, Carsamba gunu Urun B'den 90 adet satildigini gosterir.\n")

for i, satir in enumerate(satis_matrisi):
    print(f"{gunler[i]:12} -> {satir}")

print("\n[4] URUN FIYATLARI MATRISI")
print("-" * 50)
print("""
Simdi bir senaryo: Her urunun bir birim fiyati var.
Bu fiyatlar matrisini satis matrisiyle carparak toplam geliri hesaplayabiliriz.

Fiyatlar (5 urun x 1 fiyat):
[[25],   # Urun A: 25 TL
 [30],   # Urun B: 30 TL
 [40],   # Urun C: 40 TL
 [50],   # Urun D: 50 TL
 [60]]   # Urun E: 60 TL

(7 x 5) * (5 x 1) = (7 x 1) sonuc matrisi
Her gunun toplam gelirini verecek.
""")

fiyat_matrisi = [25, 30, 40, 50, 60]

for i, fiyat in enumerate(fiyat_matrisi):
    print(f"{urunler[i]}: {fiyat} TL")

print("\n[5] MATRIS CARPIMI NASIL YAPILIR?")
print("-" * 50)
print("""
Adim 1: Ilk matrisin her satiri alinir.
Adim 2: Ikinci matrisin her sutunu alinir.
Adim 3: Ayni pozisyondaki elemanlar carpilip toplanir (skaler carpim).
Adim 4: Sonuc, yeni matrisin ilgili pozisyonuna yazilir.

Formul: C[i][j] = sum(A[i][k] * B[k][j] for k in len(A[0]))

Ornegin (Pazartesi icin):
Satir: [120, 85, 90, 45, 30]
Fiyatlar: [25, 30, 40, 50, 60]

Hesaplama:
120*25 + 85*30 + 90*40 + 45*50 + 60*30
= 3000 + 2550 + 3600 + 2250 + 1800
= 13200 TL
""")

print("\n[6] GENEL MATRIS CARPIMI FONKSIYONU")
print("-" * 50)

def matris_carpimi(matris1, matris2):
    """
    Iki matrisi carpar.
    
    Parametreler:
        matris1: Ilk matris (list of lists) - boyutu m x n
        matris2: Ikinci matris (list of lists) - boyutu n x p
    
    Donus:
        Carpim matris (m x p)
    
    Kurallar:
        - matris1'in sutun sayisi = matris2'nin satir sayisi olmali
        - Bos matris kontrolu yapilir
    """
    
    print("\n--- matris_carpimi() fonksiyonu cagrildi ---")
    print(f"Matris 1 boyutu: {len(matris1)} x {len(matris1[0])}")
    print(f"Matris 2 boyutu: {len(matris2)} x {len(matris2[0])}")
    
    satir1 = len(matris1)
    sutun1 = len(matris1[0])
    satir2 = len(matris2)
    sutun2 = len(matris2[0])
    
    print(f"Uyumluluk kontrolu: matris1[{satir1}x{sutun1}] * matris2[{satir2}x{sutun2}]")
    
    if sutun1 != satir2:
        raise ValueError(f"HATA: Matrisler uyumsuz! {sutun1} != {satir2}")
    
    print(f"Kosul saglandi: {sutun1} == {satir2} -> Sonuc boyutu: {satir1} x {sutun2}")
    
    sonuc = []
    
    for i in range(satir1):
        print(f"\n  Satir {i+1} isleme aliniyor: {matris1[i]}")
        yeni_satir = []
        
        for j in range(sutun2):
            print(f"    Sutun {j+1} hesaplaniyor...", end=" ")
            
            sutun_degerleri = [matris2[k][j] for k in range(sutun1)]
            print(f"sutun degerleri: {sutun_degerleri}")
            
            carpim_toplam = 0
            islem_icerik = []
            
            for k in range(sutun1):
                deger1 = matris1[i][k]
                deger2 = matris2[k][j]
                carpim = deger1 * deger2
                carpim_toplam += carpim
                islem_icerik.append(f"{deger1}*{deger2}")
            
            print(f"      {islem_icerik} = {carpim_toplam}")
            yeni_satir.append(carpim_toplam)
        
        sonuc.append(yeni_satir)
        print(f"  --> Satir {i+1} sonucu: {yeni_satir}")
    
    return sonuc


print("\n[7] ORNEK 1: SATIS MATRISI * FIYAT MATRISI")
print("-" * 50)
print("Hesaplama: Her gunun toplam gelirini bulmak\n")

fiyat_matrisi_2d = [[25], [30], [40], [50], [60]]
print("Fiyat matrisi (5x1):")
for i, f in enumerate(fiyat_matrisi_2d):
    print(f"  {urunler[i]}: {f}")

print("\n>>> matris_carpimi(satis_matrisi, fiyat_matrisi_2d) cagriliyor...")
gelir_matrisi = matris_carpimi(satis_matrisi, fiyat_matrisi_2d)

print("\n" + "=" * 50)
print("HER GUNUN TOPLAM GELIRI:")
print("=" * 50)
for i, gelir in enumerate(gelir_matrisi):
    print(f"{gunler[i]:12}: {gelir[0]:,} TL")

print("\n[8] ORNEK 2: IK LISANS MATRISI")
print("-" * 50)
print("""
Ikinci ornek: Bir sirketin iki farkli magazasindaki urun satislari
ve her urunun kar marji oranlari.

Magaza A ve Magaza B'nin satis miktarlari ile
kar marji yuzdeleri ile toplam kari hesaplayalim.
""")

magaza_urunleri = ["Urun 1", "Urun 2", "Urun 3", "Urun 4"]
magaza_a_satislar = [150, 200, 180, 120]
magaza_b_satislar = [100, 180, 150, 90]

magaza_matrisi = [magaza_a_satislar, magaza_b_satislar]
kar_orani_matrisi = [[0.20], [0.25], [0.30], [0.15]]

print("Magaza Satislari Matrisi (2 magaza x 4 urun):")
print(f"  Magaza A: {magaza_a_satislar}")
print(f"  Magaza B: {magaza_b_satislar}")

print("\nKar Oranlari Matrisi (4 urun x 1):")
for i, oran in enumerate(kar_orani_matrisi):
    print(f"  {magaza_urunleri[i]}: %{oran[0]*100}")

print("\n>>> matris_carpimi(magaza_matrisi, kar_orani_matrisi) cagriliyor...")
kar_matrisi = matris_carpimi(magaza_matrisi, kar_orani_matrisi)

print("\n" + "=" * 50)
print("MAGAZALARIN TOPLAM KARI:")
print("=" * 50)
print(f"Magaza A: {kar_matrisi[0][0]:,.2f} TL")
print(f"Magaza B: {kar_matrisi[1][0]:,.2f} TL")

print("\n[9] ORNEK 3: TAM MATRIS CARPIMI")
print("-" * 50)
print("""
Iki tam matrisin carpimi: 2x3 ile 3x2

A = [[1, 2, 3],
     [4, 5, 6]]    (2x3)

B = [[7, 8],
     [9, 10],
     [11, 12]]    (3x2)

Sonuc: 2x2
""")

matris_a = [
    [1, 2, 3],
    [4, 5, 6]
]

matris_b = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matris A:")
for satir in matris_a:
    print(f"  {satir}")

print("\nMatris B:")
for satir in matris_b:
    print(f"  {satir}")

print("\n>>> matris_carpimi(matris_a, matris_b) cagriliyor...")
sonuc_matrisi = matris_carpimi(matris_a, matris_b)

print("\n" + "=" * 50)
print("SONUC MATRISI:")
print("=" * 50)
pprint.pprint(sonuc_matrisi)

print("\n[10] TUTORIAL OZETI")
print("=" * 50)
print("""
Matris carpimi konseptini ogrendik:

1. Matrisler, verileri tablo seklinde tutmanin etkili bir yoludur
2. Carpim islemi, satir-sutun eslesmeleri uzerinden yapilir
3. Boyutlar uyumlu olmali (m x n) * (n x p) = (m x p)
4. Gercek hayatta: satis * fiyat = gelir, miktar * kar = kar, vb.

Genel matris_carpimi fonksiyonu:
- Herhangi boyuttaki uyumlu matrisleri carpar
- Detayli loglama ile islemi gosterir
- Hata kontrolu yapar

Fonksiyon kullanimi:
    sonuc = matris_carpimi(matris1, matris2)

Not: Buyuk matrisler icin NumPy kutuphanesi daha verimli olabilir.
""")

print("\n" + "=" * 70)
print("TUTORIAL TAMAMLANDI")
print("=" * 70)