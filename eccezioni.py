Le eccezioni
In python gli errori si chiamano eccezioni. Il traceback  traccia dove è stao originato l errore. Le eccezioni sono oggetti; estendono la calsse base "Exception".
Il costruutto try-except permette di gestire le eccezioni.
try:
    my_var=float(my_var)
except:
    print('Non posso convertire "my_var" a valore numerico!')

try:
    my_var=float(my_var)
except Exception as e:
    print('Non posso convertire "my_var" a valore numerico!')
    print('La variabile "my_var" valeva:"{}"'.format(my_var))
    print('Ed ho avuto questo errore:"{}"'.format(e))
 
 try:
     my_var=float(my_var)
except ValueError:
     print('Non posso convertire "my_var" a valore numerico!')
     print('Ho avuto errore di VALORE. "my_var" valeva "{}".'.format(my_var))
except TypeError:
     print('Non posso convertire "my_var" a valore numerico!')
     print('Ho avuto errore di TIPO. "my_var" era di tipo "{}".'.format(type(my_var)))
except Exception:
     print('Non posso convertire "my_var" a valore numerico!')
    print('Ho avuto un valore generico:"{}"'.format(e))



