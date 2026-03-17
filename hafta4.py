import random 
def bubble_sort(dizi):
    N = len(dizi)
    i=0
    j=0

    while i < N -1 :
        while j < N - i - 1:
            if dizi[j] > dizi[j+1] :
                # takas yap
                tmp = dizi[j]
                dizi[j] = dizi[j+1]
                dizi[j+1] = tmp
            j += 1
        j=0
        i+=1

abc = [random.randrange(0,100) for i in range(50)]

print(abc)