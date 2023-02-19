#Zadanie 1 

shops = {
    "piekarnia": ["chleb", "bułki", "pączek"],   
    "warzywniak": ["marchew", "seler", "rukola"]
}

d = 0 

print("Lista zakupów")
for a, b in shops.items():
    a = a.capitalize()
    for c in range(0,len(b)):
        b[c] = b[c].capitalize()
        d = d + 1
    print(f"Idę do {a} i kupuję tam {b}")
    




