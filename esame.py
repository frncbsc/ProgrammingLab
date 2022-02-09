class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
        #se la lista è vuota alzo un'eccezzione
        if len(name)==0:
            raise ExamException('Errore, la lista è vuota')
    def get_data(self):
        my_file=open(self.name,'r')
        #creo la lista finale
        lista=list()
        #creo la lista per i mesi
        lista_mesi=list()
        #creo una lista per gli anni
        lista_anni=list()
        #ciclo per ogni riga del file
        for riga in my_file:
            #se la riga è vuota vado avanti
            if riga==['']:
                pass
            else:
            #tolgo \n da anno-mese-passeggeri
                parte=riga.split('\n')
            #divido ann-mese e passeggeri
                parte_1=parte[0].split(',')
                p=parte_1[0].split(',')
            #divido i mesi dagli anni
                f=parte_1[0].split('-')    
            #metto in lista il mese in stringa
                s=f[1:len(f)]
                
            #splitto ann e mese
                anno_split=p[0].split('-')
            #anno_split[0] lo nomino anno per comodità
                anno=anno_split[0]
            #se anno=='date' salto 
                if  parte_1[0]=='date' and parte_1[1]=='passengers':
                    pass
                else:
                #controllo che l'anno sia di 4 cifre
                    if(len(anno)!=4):
                        #se non è di 4 cifre lo traformo in 0 e lo aggiungo alla lista anni
                        anno=0
                        lista_anni.append(anno)
                #provo ad indicizzare l'anno in intero, in caso alzo un'eccezione
                    else:
                        try:
                            anno=int(anno)
                            #controllo l'esistenza degli aerei di linea
                            if(anno<1919):
                                raise ExamException('Errore, gli aerei di linea non esistivano ancora')
                            
                        #aggiungo gli anni nella lista
                            lista_anni.append(anno)
                        except:
                            #trasformo l'anno in 0 e lo aggiungo alla lista anni
                            anno=0
                            lista_anni.append(anno) 
            #lavoro ora sui mesi    
            #salto il primo, s è una lista
                if(s==[]):
                    pass
                else:
                    #controllo la lunghezza dei mesi, dato che s è una lista controllo la lunghezza con l'indice
                    if(len(s[0])<0 or len(s[0])>2):
                        pass
                    else:
                        #attribuisco a mese  la stringa all'interno della lista s
                        mese=s[0]
                        try:
                           #provo a indicizarlo come intero
                            mese=int(mese)
                            
                            #metto tutti i mesi in una lista
                            lista_mesi.append(mese)
                        except:
                            mese=0
             
                #lavoro con gli anni    
                try:
                    if(anno=='date' or anno==0):
                        pass
                    else:
                        #salto se 0 è il primo elemento della lista dei mesi
                        if(len(lista_mesi)==2 and lista_mesi[0]==0):
                            pass
                        else:
                            #se il mese è = a 0 passo
                            if(mese==0):
                                pass
                            else:
                                #provo a indicizzare i passeggeri in interi
                                parte_1[1]=int(parte_1[1])
                                #se è negativo passo avanti
                                if parte_1[1]<0:
                                    pass
                                else:
                                    #aggiungo tutto alla lista
                                    lista.append(parte_1)
                except:
                    pass
        #calcolo la lunghezza dell lista e divido per 12    
        len_lista_mesi=len(lista_mesi)/12
        #lo dichiaro come intero
        len_lista_mesi=int(len_lista_mesi)
        #itero per i 12 mesi
        for i in range(12):
            #itero in base agli anni
            for j in range(1,len_lista_mesi):
                #se il mese è minore di 0 o maggiore di 12 passo       
                if(lista_mesi[i+(12*j)]<=0 or lista_mesi[i+(12*j)]>12) or (lista_mesi[i+(12*(j-1))]<=0 or lista_mesi[i+(12*(j-1))]>12):
                    pass
                else:
                    #se il precedente è 12 e il successivo è 1 passo
                    if(lista_mesi[i+(12*j)]==1 and lista_mesi[i+(12*(j-1))]==12):
                        pass
                    else:
                        #se il mese corrente è 12 e successivo è maggiore alzo un'eccezzione
                        if(lista_mesi[i+(12*j)]==12):
                            if(lista_mesi[i+(12*j)]<lista_mesi[i+(12*(j-1))]):
                                raise ExamException('Errore, i mesi sono in ordine errato')
        #calcolo la lunghezza della lista_anni e poi divido per 12
        l_a=len(lista_anni)/12
        #lo indicizzo a intero
        l_a=int(l_a)
        #variabile d'appoggio
        z=1
        #iterizzo per il numero di anni
        for d in range(l_a):
            #iterizzo per un singolo anno e controllo se sono ordinati a gruppi di dodici
            for z in range(z,z+11):
                if((lista_anni[z-1]==0 and lista_anni[z]==0) or (lista_anni[z-1]==lista_anni[z])):
                    pass
                else:
                    if(lista_anni[z-1]==0 or lista_anni[z]==0):
                        pass
                    else:
                        raise ExamException('Errore, l"ordine temporale degli anni è errato')
            z=z+2
        #ritorno z a 1
        z=1
        #iterizzo per confrontare gli anni passati i 12 mesi
        for i in range(11):
            try:
                if(lista_anni[z-1]+1!=lista_anni[z+11]):
                    if(lista_anni[z-1]==0 or lista_anni[z+11]==0):
                        pass
                    else:   
                        raise ExamException('Errore,l"ordine temporale degli anni è errato')     
                else:
                    pass
            except:
                raise ExamException('Errore, gli anni non sono inseriti correttamente')
        return lista


def compute_avg_monthly_difference(time_series,first_year,last_year):
    my_file=time_series
    if(len(my_file)==0):
        raise ExamException('Errore,il file è vuoto')
    if not (type(first_year)==str or type(last_year)==str):
        raise ExamException('Errore, inserire gli anni di cui si vuole sapere il risultato com stringhe')
    lista=list()
    lista_mesi=list()
    result=list()
    for riga in my_file:
        #passeggeri li indico con la parola passeggeri
        passeggeri=riga[1]
        #separo l'anno dal mese
        anno_ci=riga[0].split('-')
        #lo indico con mese per comodita
        mese=anno_ci[1]
        #lo indico con anno per comodità
        anno=anno_ci[0]
        #li pongo come interi
        anno=int(anno)
        mese=int(mese)
        #trasformo in interi firt e last year
        first_year=int(first_year)
        last_year=int(last_year)
        #controllo che siano in giusto ordine
        if (first_year>last_year):
            raise ExamException('Errore, il primo deve essere minore del secondo')
        else:
            #se l'anno preso in considerazione è >= al first_year o <= al last_year aggiungo i passeggeri in una lista
            if anno>=first_year and anno<=last_year:
                #faccio un try per vedere se i passeggeri sono scritti a numero 
                lista_mesi.append(mese)                
                lista.append(passeggeri)
    #creo una nuova lista
    nuova_lista=list()
    #aggiungo oltre che i mesi vecchi anche i veri tra un mese e l'altro se non sono in ordine temporale corretto
    for t in range(1,len(lista_mesi)):
        #se quello prima è 12 e quello dopo è 1 aggiungo il mese
        if(lista_mesi[t-1]==12 and lista_mesi[t]==1):
            nuova_lista.append(lista_mesi[t-1])
            pass
        else:
            if(lista_mesi[t-1]+1==lista_mesi[t]):
                #se il mese precedente +1 è uguale a quello successivo aggiungo il mese
                nuova_lista.append(lista_mesi[t-1])
                pass
            else:
                #se il precedente è 12 ma il successivo non è 1 aggiungo 0 alla nuova lista
                if(lista_mesi[t-1]==12 and lista_mesi[t]!=1):
                    nuova_lista.append(lista_mesi[t-1])
                    for y in range(2,11):
                        while(y!=lista_mesi[t]):
                            nuova_lista.append(0)
                else:
                    #se il precedente +1 è maggiore del successivo aggiungo 0 alla nuova lista fino a quando non torna in ordine
                    if(lista_mesi[t-1]+1>lista_mesi[t]):
                        nuova_lista.append(lista_mesi[t-1])
                        for m in range(lista_mesi[t-1],12):
                            nuova_lista.append(0)
                        for n in range(1,lista_mesi[t]):
                            nuova_lista.append(0)
                    else:
                        #se il precedente +1 è più piccolo aggiungo 0 alla lista nuova finche non sono uguali
                        if(lista_mesi[t-1]+1<lista_mesi[t]):
                            nuova_lista.append(lista_mesi[t-1])
                            for v in range(lista_mesi[t-1]+1,lista_mesi[t]):
                                nuova_lista.append(0)
    #aggiungo l'ultio elemento della lista vecchia a quella nuova
    nuova_lista.append(lista_mesi[len(lista_mesi)-1])
    #controllo che il primo mese della vecchia lista sia uno, in caso aggiungo gli 0 d'avanti
    if(nuova_lista[0]!=1):
        for y in range(1,nuova_lista[0]):
            nuova_lista.insert(0,0)
    #aggiungo nella lista passeggeri gli 0
    for y in range(0,len(nuova_lista)):
        if(nuova_lista[y]==0):
            lista.insert(y,0)
    len_list_pass=int(len(lista)/12)
    
    #ciclo for per i 12 mesi
    for i in range(12):
        #variabile d'appoggio dove inserisco le sottrazioni
        summ=0
        # creo e uso c come contatore
        c=0
        #ciclo in base agli anni
        for j in range(1,len_list_pass):
            #se uno dei valori è 0 aggiungo a summ 0
            if(lista[i+(12*j)]==0 or lista[i+(12*(j-1))]==0):
                summ+=0
            else:    
                #aggiungo a summ la differenza dei due valori 
                summ+=(lista[i+(12*j)]-lista[i+(12*(j-1))])
                #aumento c di 1
                c=c+1
        #se summ è == 0 lo aggiunga direttamente al risultato        
        if(summ==0):
            result.append(summ)
        else:
            #divido summ per il contatore c
            s=summ/c
            result.append(s)
    return result
