import serial.tools.list_ports
import serial


class SerialService:
    ListaBaudRate = [11520, 9600]
    conexion = None
    def __init__(self):
        pass
    def GetConexion(self):
        return self.conexion

    def GetListaCOMS(self):
        listaCOMS = []
        lista = list(serial.tools.list_ports.comports())
        for item in lista:
            listaCOMS.append(item[0])
        return listaCOMS

    def Conectar(self,ComPort,BaudRate):
        if self.conexion is None:
            Com = ComPort[3]
            Conexion = serial.Serial()
            Conexion.baudrate = BaudRate
            Conexion.port = int(Com)-1
            Conexion.timeout = 100
            Conexion.open()
            self.conexion = Conexion

    def Desconectar(self):
        if self.conexion is not None:
            if self.conexion.isOpen():
                self.conexion.close()
                self.conexion = None


    def Enviar(self,Texto):
        if self.conexion is not None:
            if self.conexion.isOpen():
                self.conexion.write(str(Texto))

    def Leer(self):
        if self.conexion is not None:
            while self.conexion.isOpen():
                return self.conexion.read()