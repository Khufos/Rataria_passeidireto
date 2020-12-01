
import requests
from PyQt5 import uic, QtWidgets, QtCore
from bs4 import BeautifulSoup
from PyQt5.QtCore import Qt


def listar_dados():
    try:
        texto = listar.lineEdit.text()
        page = requests.get(texto)
        sopa = BeautifulSoup(page.content, 'html.parser')
        sumary = sopa.find('pre')
        texto = sumary.text.upper()
        listar.segura.setText(texto)
    except:
        listar.segura.setText(
            "COLOQUE O LINK IGUAL DO EXEMPLO PARA FUNCIONAR:BY KHUFOSS")


def sair():
    listar.close()


def deletar():
    listar.lineEdit.clear()


app = QtWidgets.QApplication([])
listar = uic.loadUi("listar.ui")
listar.pushButton.clicked.connect(listar_dados)
listar.pushButton_2.clicked.connect(deletar)
listar.pushButton_3.clicked.connect(sair)


listar.show()
app.exec()
