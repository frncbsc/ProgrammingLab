Programmazione ad oggetti 
gli oggetti sono definiti con le classi
-le funzioni negli oggetti/classi si chiamano metodi
-le variabili negli oggetti/classi si chiamano attributi

una volta inizializzati diventano /istanze/

Gli oggetti si usano principalmente per:
-Permettono di rappresentare bene delle gerarchie(e sfruttare le caratteristiche in comune)
-Una volta istanziati, permettono di mantenere facilmente lo stato(senza diventare matti con strutture dati di appoggio)
 CONvenzioni
 -caratteri minuscoli e underscore per le variabili e le istanze degli oggetti
 -notazione CamelCase per il nome delle classi
 Inoltre, doppi underscore prima e dopo il nome in un metodo indicano un metodo ad uso esclusivamente interno(esempio:__str__,oppure__doc__)
 Gli apici valgono sia singoli che doppi, ma conviene usarli singoli,........

 dir indicat tutto quello contenuto in un oggetto.
DEFINire oggetti
class Person():
    pass
person=Person()
print(person)

class Person():
    def __init__(self, name, surname):
        #set name and surname
        self.name= name
        self.surname= surname

person=Person('Mario','Rossi')
print(person)
print(person.name)
print(person.surname) 

