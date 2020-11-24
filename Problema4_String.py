cuvant1=str(input('Introduceti cuvantul 1: '))
cuvant2=str(input('Introduceti cuvantul 2: '))
cuvant3=str(input('Introduceti cuvantul 3: '))
cuvant4=str(input('Introduceti cuvantul 4: '))
if len(cuvant1)>3 and len(cuvant2)>3 and len(cuvant3)>3 and len(cuvant4)>3:
    c_nou = cuvant1[0]+cuvant1[1]+cuvant2[0]
    for i in range(3):
        c_nou += cuvant3[i] 
    for i in range(len(cuvant4)//2):
        c_nou += cuvant4[i]
    print(f'Cuvintele introduse: {cuvant1}, {cuvant2}, {cuvant3}, {cuvant4}')
    print("Cuvantul nou = ", c_nou)
else:
    print('Eroare')

