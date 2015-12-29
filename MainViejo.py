from PyQt4 import  QtGui
from PyQt4 import  QtCore
import sys
import UserInterface
from Services import SerialService

class SerialConsole(QtGui.QMainWindow, UserInterface.Ui_Form):
    def __init__(self):
        super(self.__class__,self).__init__()
        self.setupUi(self)
        self.setFixedSize(552,462)
#-----------------  Declaro Una Conexion Vacia ----------------------------
        self.Conexion = None
#-----------------  Inicio el Servicio ------------------------------------
        self.Servicio = SerialService()
#-----------------  Relleno La Lista de COMS ------------------------------
        for item in self.Servicio.GetListaCOMS():
            self.CboCOMPorts.addItem(item)
#-----------------  Relleno La Lista de Baudrate --------------------------
        for item in self.Servicio.ListaBaudRate:
            self.CboBaudRate.addItem(str(item))
#-----------------  Instancio la Conexion  --------------------------------
        self.BtnConectar.clicked.connect(self.Conectar)
#-----------------  Cierro la Conexion  -----------------------------------
        self.BtnDesconectar.clicked.connect(self.Desconectar)
#-----------------  Envio de Datos  ---------------------------------------
        self.BtnEnviar.clicked.connect(self.EnviarDatos)

    def Conectar(self):
        COM = str(self.CboCOMPorts.currentText())
        BR = int(self.CboBaudRate.currentText())
        self.Servicio.Conectar(COM,BR)
        self.HiloLectura = ThreadLectura(self.Servicio.GetConexion())
        self.HiloLectura.start()
        self.connect(self.HiloLectura,QtCore.SIGNAL('LEER_DATOS'), self.ActualizarTxtRx)

    def Desconectar(self):
        if self.Conexion is not None:
            if self.Conexion.isOpen():
                self.Servicio.Desconectar()
                self.HiloLectura.quit()

    def EnviarDatos(self):
        Texto = self.TxtEnviar.text()
        Enviar = []
        for char in Texto:
            Enviar.append(str(char))
        if self.ChkNuevaLinea.checkState():
            Enviar.append('\n')
        if self.ChkRetornoCarro.checkState():
            Enviar.append('\r')
        self.Servicio.Enviar(''.join(Enviar))
        self.TxtEnviar.setText("")

    def ActualizarTxtRx(self,val):
        print val
        self.TxtDatosRecibidos.insertPlainText(str(val))



class ThreadLectura(QtCore.QThread):

    def __init__(self,Conexion,parent = None):
        super(ThreadLectura,self).__init__(parent)
        self.conexion = Conexion
    def run(self):
        while self.conexion.isOpen():
            var = self.conexion.read()
            self.emit(QtCore.SIGNAL('LEER_DATOS'),var)
            #time.sleep(0.1)
def main():
    app = QtGui.QApplication(sys.argv)
    form = SerialConsole()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()