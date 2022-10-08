"""
Etape 1 :
Faire un ensemble avec des sous ensemble et manipuler

A.issubset(B) = Si tout les elements de A sont dans B
A.issuperset(B) = SI tout les elements de B sont dans A

Etape 2 :
Faire Fonction Ouvrir() et Fermer()

Ouvrir() : le Sous-ensemble Fille devient l'Ensemble Mére

Fermer() : L'Ensemble précedent devient l'ensemble Mere


"""

def ouvrir(mere):
    fille=list()
    for i in range(1,len(list(mere))):
        fille.append(list(mere)[i])
    return set(fille)



a={1,2,3}
b={2,3}
c={3}
print(b.issubset(a))
print(c.issubset(b))

print(ouvrir(a))





