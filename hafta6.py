# import numpy as np
# x = [5,2,7,9,4,8,2,1]
# # x'in mod, medyan ve ortalamasını bulun.
# sayilar = {} 
# for i in x:
#     try :
#         sayilar[i] += 1
#     except:
#         sayilar[i]=1
# encok,anahtar = -1,-1
# for i in sayilar:
#     if encok < sayilar[i]:
#         encok = sayilar[i]
#         anahtar = i

# print(f"mod:{anahtar}, değeri:{encok}")
# x = [5,2,7,9,4,8,2,1]
# #medyan bul.
# siralanmis_x = sorted(x)
# # print(siralanmis_x)
# n = len(siralanmis_x) # liste uzunluğunu bul!
# if n%2==0: # liste uzunluğu 2'nin katı ise ortadaki iksinin ortalamasını al.
#     print(  (siralanmis_x[n//2] + siralanmis_x[n//2-1])/2  )
# else :
#     print(  siralanmis_x[n//2]   )

# # ortalama bul
# print(x)
# toplam  = 0
# for i in x:
#     toplam += i
# ortalama = toplam/len(x)
# print(f"Toplam: {toplam} , ortalama: {ortalama}")

# #varyans bulma :  Σ (x-xort)^2
# varyans = 0
# for i in x:
#     varyans += (i-ortalama)**2
# varyans = varyans/len(x)
# print(f"Varyans:{varyans}")

# #standart sapma = varyansın karekökü
# std_dev = varyans**0.5
# print(f"Standart Sapma: {std_dev:.2f}")
import numpy as np

x = [5,6,7,9,4,8,6,1]
np_x = np.array(x)
# print(type(x))
# print(type(np_x))
# print(np_x)
x_toplam = np.sum(np_x)
x_ort = np.mean(np_x)
x_medyan = np.median(np_x)
x_shp = np.shape(np_x)
x_mod = np.bincount(np_x).argmax()

print(f"{x_toplam} , {x_ort} , {x_medyan}, {x_shp} , {x_mod}")