"""
Etape 1 :
Faire un ensemble avec des sous ensemble et manipuler

A.issubset(B) = Si tout les elements de A sont dans B
A.issuperset(B) = SI tout les elements de B sont dans A

Etape 2 :
Faire Fonction Ouvrir() et Fermer()

Ouvrir() : le Sous-ensemble Fille devient l'Ensemble Mére
Ouvrir_end() : Ouvrir la Matroshka, jusqu'a que elle soit Vide

Fermer() : L'Ensemble précedent devient l'ensemble Mere


"""


Matroshka=[1,2,3] # Je vais devoir utiliser une liste pour garder en memoire la matroshka Mere
                    # Pour ensuite faire la fonction Fermer_till

def ouvrir(mere):
    fille=list()

    for i in range(1,len(list(mere))):
        fille.append(list(mere)[i])
    return set(fille)



def ouvrir_end(mere):

    if list(ouvrir(mere)) == []:
        print("Ah Lulu, je suis Vide ")
        return ouvrir(mere)

    else:
        print("Jai encore ",len(list(ouvrir(mere)))," filles dans moi ")
        print(ouvrir(mere))
        return ouvrir_end(ouvrir(mere))



def fermer(mere,fille):
    fille=mere
    return fille

def fermer_till(mere,fille,nb):
    return 0



a={1,2,3}
b={2,3}
c={3}
d={None}

print(b.issubset(a))
print(c.issubset(b))

print("J'ouvre la Matroshka :")
print(a)
print(ouvrir_end(a))

print("Fermer la Matroshka :")
print("AHA, MES FILLES SONT DE RETOURS !")
print(fermer(a,ouvrir(a)))






