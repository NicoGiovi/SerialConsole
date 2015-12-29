from PySide.QtCore import *
from PySide.QtGui import *
import sys
import UI
from Services import SerialService
class MainWindow(QDialog,UI.Ui_Form):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
    #-----------------  Inicio el Servicio ------------------------------------
        self.Servicio = SerialService()
    #-----------------  Relleno La Lista de COMS ------------------------------
        for item in self.Servicio.GetListaCOMS():
            self.CboCOMPorts.addItem(item)
    #-----------------  Relleno La Lista de Baudrate --------------------------
        for item in self.Servicio.ListaBaudRate:
            self.CboBaudRate.addItem(str(item))
    #-----------------  Instancio la Conexion  --------------------------------
        self.connect(self.BtnConectar,SIGNAL("clicked()"),self.Conectar)
    #-----------------  Cierro la Conexion  -----------------------------------
        self.connect(self.BtnDesconectar,SIGNAL("clicked()"),self.Desconectar)
    #-----------------  Envio de Datos  ---------------------------------------
        self.connect(self.BtnEnviar,SIGNAL("clicked()"),self.EnviarDatos)


    def Conectar(self):
        COM = str(self.CboCOMPorts.currentText())
        BR = int(self.CboBaudRate.currentText())
        self.Servicio.Conectar(COM,BR)

    def Desconectar(self):
        if self.Conexion is not None:
            if self.Conexion.isOpen():
                self.Servicio.Desconectar()

    def EnviarDatos(self):
        if self.Servicio.conexion.isOpen():
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

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()