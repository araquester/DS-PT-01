def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    listbin = []
    if numero < 0:
        print('Debe ingresar un número mayor que cero')
        return None
    if type(numero) != int:
        print('Debe ingresar un número entero')
        return None
    if numero == 0 or numero == 1:
        return numero
    while(numero>1):
        listbin.append(numero%2)
        numero = numero//2
    listbin.append(numero)
    listbin.reverse()    
    for i in range(0,len(listbin)):
        print(listbin[i],end="")