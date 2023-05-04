class Ventana:
    __titulo=str
    __izqX=int
    __izqY=int
    __derX=int
    __derY=int
    def __init__(self,func,izqX=0,izqY=0,derX=500,derY=500):
        self.__titulo=func
        self.__izqX=izqX
        self.__izqY=izqY
        self.__derX=derX
        self.__derY=derY
    def mostrar(self):
        print('%s'%self.__titulo)
        print('(%d,%d)'%(self.__izqX,self.__izqY))
        print('(%d,%d)\n'%(self.__derX,self.__derY))
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return self.__derY-self.__derY
    def ancho(self):
        return self.__derX-self.__izqX
    def moverDerecha(self,unidades=1):
        if (self.__derX+unidades)<=500 and (self.__izqX+unidades)<(self.__derX+unidades):
            self.__izqX+=unidades
            self.__derX+=unidades
    def moverIzquierda(self,unidades=1):
        if (self.__izqX-unidades)>=0 and (self.__izqX-unidades)<(self.__derX-unidades):
            self.__izqX-=unidades
            self.__derX-=unidades
    def bajar(self,unidades=1):
        if (self.__derY+unidades)<=500 and (self.__izqY+unidades)<(self.__derY+unidades):
            self.__izqY+=unidades
            self.__derY+=unidades
    def subir(self,unidades=1):
        if (self.__izqY-unidades)>=0 and (self.__izqY-unidades)<(self.__derY-unidades):
            self.__izqY-=unidades
            self.__derY-=unidades
    def __str__(self):
        return('%s %d %d %d %d'%(self.__titulo,self.__izqX,self.__izqY,self.__derX,self.__derY))