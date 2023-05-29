class Empleado:
    def __init__(self,nombre,sueldo):
        self.nombre=nombre
        self.sueldo=sueldo
    def CalcularBono(self):
        pass
class Programador(Empleado):
    def CalcularBono(self,sueldo):
        bono=sueldo*2
        print(bono)
class Gerente(Empleado):
    def CalcularBono(self,sueldo):
        bono=sueldo*15
        print(bono)
programador=Programador("Luis",1000)
programador.CalcularBono(1000)
gerente=Gerente("Tony",1500)
gerente.CalcularBono(1500)
#kkkkkkkk