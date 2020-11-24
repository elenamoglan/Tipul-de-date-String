sir=str(input('Sir de caractere: '))
majuscule=0
cifre=0
car_sp=0
for i in sir:
    if i.isupper():
        majuscule+=1
    if i.isnumeric():
        cifre+=1
    if ord(i) in range(32,48) or ord(i) in range(58,65) or ord(i) in range(91,97) or ord(i) in range(123,127):
        car_sp+=1
print(f'a) Numarul de majuscule in sir este {majuscule}')
print(f'b) Numarul de cifre in sir este {cifre}')
print(f'c) Numarul de caractere speciale in sir este {car_sp}')