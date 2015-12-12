from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(562, 452)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(562, 452))
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Form.setAcceptDrops(True)
        Form.setStyleSheet(_fromUtf8(""))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 261, 80))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.BtnConectar = QtGui.QPushButton(self.groupBox)
        self.BtnConectar.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.BtnConectar.setObjectName(_fromUtf8("BtnConectar"))
        self.BtnDesconectar = QtGui.QPushButton(self.groupBox)
        self.BtnDesconectar.setGeometry(QtCore.QRect(180, 50, 75, 23))
        self.BtnDesconectar.setObjectName(_fromUtf8("BtnDesconectar"))
        self.CboCOMPorts = QtGui.QComboBox(self.groupBox)
        self.CboCOMPorts.setGeometry(QtCore.QRect(10, 20, 161, 22))
        self.CboCOMPorts.setObjectName(_fromUtf8("CboCOMPorts"))
        self.CboBaudRate = QtGui.QComboBox(self.groupBox)
        self.CboBaudRate.setGeometry(QtCore.QRect(10, 50, 161, 22))
        self.CboBaudRate.setObjectName(_fromUtf8("CboBaudRate"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(290, 10, 261, 80))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.BtnEnviar = QtGui.QPushButton(self.groupBox_2)
        self.BtnEnviar.setGeometry(QtCore.QRect(180, 20, 75, 23))
        self.BtnEnviar.setObjectName(_fromUtf8("BtnEnviar"))
        self.ChkNuevaLinea = QtGui.QCheckBox(self.groupBox_2)
        self.ChkNuevaLinea.setGeometry(QtCore.QRect(10, 50, 81, 17))
        self.ChkNuevaLinea.setObjectName(_fromUtf8("ChkNuevaLinea"))
        self.ChkRetornoCarro = QtGui.QCheckBox(self.groupBox_2)
        self.ChkRetornoCarro.setGeometry(QtCore.QRect(90, 50, 81, 17))
        self.ChkRetornoCarro.setObjectName(_fromUtf8("ChkRetornoCarro"))
        self.TxtEnviar = QtGui.QLineEdit(self.groupBox_2)
        self.TxtEnviar.setGeometry(QtCore.QRect(10, 20, 161, 20))
        self.TxtEnviar.setObjectName(_fromUtf8("TxtEnviar"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 90, 541, 351))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.TxtDatosRecibidos = QtGui.QTextEdit(self.groupBox_3)
        self.TxtDatosRecibidos.setGeometry(QtCore.QRect(10, 20, 521, 321))
        self.TxtDatosRecibidos.setObjectName(_fromUtf8("TxtDatosRecibidos"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Serial Console", None))
        self.groupBox.setTitle(_translate("Form", "Conexion", None))
        self.BtnConectar.setText(_translate("Form", "Conectar", None))
        self.BtnDesconectar.setText(_translate("Form", "Desconectar", None))
        self.groupBox_2.setTitle(_translate("Form", "Enviar Datos", None))
        self.BtnEnviar.setText(_translate("Form", "Enviar", None))
        self.ChkNuevaLinea.setText(_translate("Form", "Agregar NL", None))
        self.ChkRetornoCarro.setText(_translate("Form", "Agregar RC", None))
        self.groupBox_3.setTitle(_translate("Form", "Datos Recibidos", None))

