class Triangulo:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def retangulo(self):
        if (self.a**2+self.b**2==self.c**2) or (self.a**2+self.c**2==self.b**2) or (self.c**2+self.b**2==self.a**2):
            return True
        else:
            return False

    def semelhantes(self,triangulo):
        listt1=sorted([self.a,self.b,self.c])
        listt2=sorted([triangulo.a,triangulo.b,triangulo.c])
        if listt1[0]%listt2[0]==0 and listt1[1]%listt2[1]==0 and listt1[2]%listt2[2]==0:
            return True
        if listt2[0]%listt1[0]==0 and listt2[1]%listt1[1]==0 and listt2[2]%listt1[2]==0:
            return True
        else:
              return False