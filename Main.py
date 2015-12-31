from PySide.QtCore import *
from PySide.QtGui import *
import sys
import UI
from Services import SerialService
import time
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
    #-----------------  Instancio Los Hilos de Lectura y Escritura ------------
        self.HiloLectura = ThreadLectura()
        self.HiloEscritura = ThreadEscritura()
    #-----------------  Señal Para Recivir lo que envia el HiloLectura --------
        self.connect(self.HiloLectura,SIGNAL("LEER_DATOS(QString)"),self.ActualizarTxtRx,Qt.QueuedConnection)

    def Conectar(self):
        COM = str(self.CboCOMPorts.currentText())
        BR = int(self.CboBaudRate.currentText())
        self.Servicio.Conectar(COM,BR)

        if self.Servicio.conexion.isOpen():
            self.HiloLectura.conexion = self.Servicio.GetConexion()
            self.HiloLectura.start()
            print(self.HiloLectura)

    def Desconectar(self):
        if self.HiloLectura.isRunning():
            self.Servicio.Desconectar()
            self.HiloLectura.quit()

    def EnviarDatos(self):
        if self.ChkNuevaLinea.isChecked():
            self.HiloEscritura.nl = True
        if self.ChkRetornoCarro.isChecked():
            self.HiloEscritura.rc = True
        self.HiloEscritura.conexion = self.Servicio.GetConexion()
        self.HiloEscritura.texto = self.TxtEnviar.text()
        self.HiloEscritura.start()
        print(self.HiloEscritura)
        self.TxtEnviar.setText("")

    def ActualizarTxtRx(self,BytesRecibidos):
        self.TxtDatosRecibidos.insertPlainText(str(BytesRecibidos))

    #-----------------  Definicion del Hilo de Lectura ------------------------

class ThreadLectura(QThread):
    conexion = None
    def __init__(self,parent = None):
        super(ThreadLectura,self).__init__(parent)

    def run(self):
         if self.conexion is not None:
            while self.conexion.isOpen():
                BytesRecibidos = self.conexion.read()
                self.emit(SIGNAL("LEER_DATOS(QString)"),BytesRecibidos)

    #-----------------  Definicion del Hilo de Escritura ---------------------

class ThreadEscritura(QThread):
    conexion = None
    texto = None
    nl = False
    rc = False

    def __init__(self,parent = None):
        super(ThreadEscritura,self).__init__(parent)

    def run(self):
        print()
        Enviar = []
        for char in self.texto:
            Enviar.append(str(char))
        if self.nl:
            Enviar.append('\n')
        if self.rc:
            Enviar.append('\r')
        if self.conexion.isOpen():
            print("Conexion Abierta")
            TXDATA = ''.join(Enviar)
            self.conexion.write(TXDATA.encode())


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()