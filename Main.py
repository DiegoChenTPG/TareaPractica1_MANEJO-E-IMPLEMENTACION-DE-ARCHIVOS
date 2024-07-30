import random 

class nodo:
    def __init__(self):
        self.tamaño = 0
        self.siguiente = None
    
    def cambiarTamaño(self, tamaño):
        self.tamaño = tamaño

class lista_enlazada: 
    def __init__(self):
        self.cabeza = None 
        self.contador = 0

    def insertar(self, tamaño):
        nuevoNodo = nodo()
        nuevoNodo.cambiarTamaño(tamaño)
        if self.cabeza == None: 
            self.cabeza = nuevoNodo
        else:
            auxiliar = nodo()
            auxiliar = self.cabeza
            while auxiliar.siguiente != None: 
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevoNodo
        self.contador += 1

    def eliminarUltimo(self):
        if self.contador == 0 or self.contador == 1 : 
            self.cabeza = None
        else:
            auxiliar = nodo()
            auxiliar = self.cabeza.siguiente
            anterior = nodo()
            anterior = self.cabeza
            while auxiliar.siguiente != None: 
                anterior = auxiliar
                auxiliar = auxiliar.siguiente
            anterior.siguiente = None
        self.contador -= 1
            
    def eliminarIndice(self, indice):
        i = 1
        if indice <= self.contador:
            if indice == 1 :
                if self.contador == 1:  
                    self.cabeza = None
                else: 
                    self.cabeza = self.cabeza.siguiente
            else:
                auxiliar = nodo()
                auxiliar = self.cabeza.siguiente
                anterior = nodo()
                anterior = self.cabeza
                while i < indice - 1:
                    auxiliar = auxiliar.siguiente
                    anterior = anterior.siguiente
                    i += 1
                if auxiliar.siguiente == None:
                    anterior.siguiente = None
                else: 
                    anterior.siguiente = auxiliar.siguiente
                
            self.contador -= 1
    
    def imprimirLista(self):
        counter = 1
        auxiliar = nodo()
        auxiliar = self.cabeza
        if self.contador != 0:
            print (str(counter) + ". " + "tamaño: " + str(auxiliar.tamaño))
            counter += 1
            while auxiliar.siguiente != None:
                auxiliar = auxiliar.siguiente
                print (str(counter) + ". " + "tamaño: " + str(auxiliar.tamaño))
                counter += 1
        else: 
            print("Lista vacía")




Lista = lista_enlazada()


"""print ("Prueba 1 Asignacion de memoria")
tamaño = random.randint(1,9)
Lista.insertar(tamaño)
Lista.imprimirLista()"""

#tiempo de ejecución 1.78 seg

"""print ("Prueba 2 Asignacion y liberación de memoria")
tamaño = random.randint(1,9)
Lista.insertar(tamaño)
Lista.imprimirLista()
Lista.eliminarUltimo()
Lista.imprimirLista()"""

#tiempo de ejecucion 1.90 seg 

"""print ("Prueba 3 Asignacion de memoria en 10 espacios")
for n in range(1, 11, 1):
    tamaño = random.randint(1,9)
    Lista.insertar(tamaño)
Lista.imprimirLista()"""

#tiempo de ejecución 1.85 seg

"""print ("Prueba 5 Asignacion y liberacion de memoria en 10 espacios")
for n in range(1, 11, 1):
    tamaño = random.randint(1,9)
    Lista.insertar(tamaño)
Lista.imprimirLista()
Lista.eliminarIndice(5)
Lista.imprimirLista()"""

#tiempo de ejecución 2.11 seg

"""print ("Prueba 6 Asignacion de memoria en 100 espacios")
for n in range(1, 101, 1):
    tamaño = random.randint(1,9)
    Lista.insertar(tamaño)
Lista.imprimirLista()"""

#tiempo de ejecución 2.12 seg

"""print ("Prueba 7 Asignacion y liberacion de memoria en 100 espacios")
for n in range(1, 101, 1):
    tamaño = random.randint(1,9)
    Lista.insertar(tamaño)
Lista.imprimirLista()
Lista.eliminarIndice(50)
Lista.imprimirLista()"""

#tiempo de ejecución 2.76 seg