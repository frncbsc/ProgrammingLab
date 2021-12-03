#scrivere una funzione che sommi tutti gli elementi di una lista
def letturaparti():
    my_file=open('shampoo_sales.txt','r')
    lista=list()
    for riga in my_file:
        parte=riga.split(',')
        if parte[0]=='Date':
            pass
        else:
            parte1=parte[1].split('\n')
            lista.append(float(parte1[0]))
    return lista

 
print(letturaparti())



def sommalista():
    res=0
    for i in letturaparti():
        res=res+i
    return res

print(sommalista()) 


class CSVFile():
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        try:
            file=open(self.name,'r')
            lista=list()
            for riga in file:
                parte=riga.split(',')
                if(parte[0]=='Date'):
                    pass
                else:
                    parte1def=parte[1].split('\n')
                    parte[1]=parte1def[0]
                    lista.append(parte)
            return lista
        except Exception as e:
            print('Non posso aprire un file vuoto')
            print('Ho avuto questo errore: "{}"'.format(e)) 

class ErrorestringaCSVFile():
        
        def __init__(self,name):
            self.name=name
        
        def get_data(self):
            if not(isinstance(self.name,str)):
                raise Exception('Il nome del file non è una stringa')

            file=open(self.name,'r')
            lista=list()
            for riga in file:                
                parte=riga.split(',')
                if(parte[0]=='Date'):
                    pass    
                else:
                    parte1def=parte[1].split('\n')
                    parte[1]=parte1def[0]
                    lista.append(parte)
            return lista
            




class NumericalCSVFile():
    def __init__(self,name):
        self.name=name
    
    def get_data(self):
        file=open(self.name,'r')
        lista=list()
        for riga in file:
            parte=riga.split(',')
            if(parte[0]=='Date'):
                pass
           
            else:
                try:
                    parte1def=parte[1].split('\n')   
                    parte1def[0]=float(parte1def[0])
                    parte[1]=parte1def[0]
                    lista.append(parte[1])
                except:
                    lista.append(parte[1])    
        return lista 





my_file=ErrorestringaCSVFile('shampoo_sales.txt')
print(my_file.get_data())