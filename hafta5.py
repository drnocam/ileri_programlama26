
kurallar = {
    "ömer":"öğrenci",
    "öğrenci":"insan",
    "insan":"canlı",
}

def is_canli(cat):
    global kurallar
    c = kurallar[cat] 
    if c=="canlı" or is_canli(c):
        return True
    return False
        

print( is_canli("ömer") )