import numpy as np
import pandas as pd
f = open("titanic.csv","r")

satir = 0
veriler = []
for i in f.readlines():
    i = i.strip()
    if satir==0:
        # sütunlar yazdıırlıyo
        print(i.split(",")) 
    else:
        veriler.append(i.split(","))
    satir += 1
np_age = np.array([float(i[6]) for i in veriler if i[6]!=""])
print( np_age.mean(), np_age.max() , np_age.min()) 

f.close()

# pandas ile titanic.csv'yi yükle ve bilgi al

df = pd.read_csv("titanic.csv")
print("\nPandas veri çerçevesi için genel bilgi:")
print(df.info())
print("\nPandas describe():")
print(df.describe(include='all'))

# pandas ile açılan dataframe'den Age sütununu numpy dizisine ata
np_age = df['Age'].dropna().to_numpy(dtype=float)
print("\nPandas'dan numpy dizisine Age aktarımı:")
# print(np_age)
print("Mean age (numpy):", np_age.mean())
print("Max age (numpy):", np_age.max())
print("Min age (numpy):", np_age.min())

# cinsiyete göre kurtulan oranları ve yaş ortalamaları
pool_total = len(df)

survived_by_sex = df.groupby('Sex')['Survived']

women_survived_rate = survived_by_sex.get_group('female').mean()
men_survived_rate = survived_by_sex.get_group('male').mean()

women_age_mean = df[df['Sex'] == 'female']['Age'].mean()
men_age_mean = df[df['Sex'] == 'male']['Age'].mean()

women_count = len(df[df['Sex'] == 'female'])
men_count = len(df[df['Sex'] == 'male'])

print("\nKadın kurtulan oranı:", women_survived_rate)
print("Erkek kurtulan oranı:", men_survived_rate)
print("Kadın yaş ortalaması:", women_age_mean)
print("Erkek yaş ortalaması:", men_age_mean)
print("Kadın/Erkek oranı:", women_count, "/", men_count)
print("Kadın/Erkek oranı (eksi):", women_count/men_count if men_count > 0 else None)

# sınıf (Pclass) bazında kurtulma oranları
pclass_rates = df.groupby('Pclass')['Survived'].mean()
print("\nSınıf bazında kurtulan oranları:")
print(pclass_rates)

