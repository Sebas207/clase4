from indicadores import Indicadores

class Nomina(indicadores):

    def __init__(self):
        self.__salarioBasico = 0
        self.__diasLiquidados = 0
        self.__auxilio_Transporte = 97032
        self.__smlv = self.salariominimo() 
 
    def setSalario(self, salarioBasico:int):
        if str(type(salarioBasico)) == "<class 'float'>" or str(type(salarioBasico)) == "<class 'int'>":
            if self.salariominimo() <= salarioBasico:
                self.__salarioBasico = salarioBasico
            else:
                print('el salario basico no puede ser inderior al SLMV ')
        else:
            print("Error")        

        
        
    def getSalario(self):
        return self.__salarioBasico

    def setDiasLiquidados(self, diasLiquidados:int):
        self.__diasLiquidados = diasLiquidados

    def getDiasLiquidados(self):
        return self.__diasLiquidados    

    def salarioDevengado(self):
        try:
            return (self._salarioBasico/30) * self._diasLiquidados
        except:
            print("error en alguna de las variables")

    def auxilioTransporte(self):
        if self.__salarioBasico > (self.__smlv * 2):
            return 0
        else:
            return (self.__auxilio_Transporte/30 * self.__diasLiquidados)

    def totalDevengado(self):
        return self.salarioDevengado() + self.auxilioTransporte()

    def __str__(self):
        return str("salario Basico: {} \n"
                   "dias liquidados: {} \n"
                   "salario devengado: {} \n"
                   "auxilio de transporte: {} \n"
                   "Total devengado: {} \n").format(
                       self.__salarioBasico,
                       self.__diasLiquidados,
                       self.salarioDevengado(),
                       self.auxilioTransporte(),
                       self.totalDevengado())
                       
             