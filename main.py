from pytube import YouTube
from PyQt5 import uic, QtWidgets
import pafy

def funcao_principal():
    linha1 = entrada.lineEdit.text()

    if entrada.radioButton.isChecked():
        print("Música selecionada")
        link = " " + linha1
        DOWNLOAD_FOLDER = "C:/Users/Usuario/Desktop"
        video= pafy.new(link)
        audiostreams = video.audiostreams
        for i in audiostreams:
            print("bitrate: %s, ext: %s, size: %ds0,2fMb" % (i.bitrate, i.extension, i.get_filesize()/1024/1024))
        audiostreams[1].download(filepath = DOWNLOAD_FOLDER)


    elif entrada.radioButton_2.isChecked():
        print("Vídeo selecionado")
        minha_url = " " + linha1
        print(minha_url)

        yt = YouTube(minha_url)
        video = yt.streams.first()
        video.download("C:/Users/Usuario/Desktop")


app = QtWidgets.QApplication([])
entrada = uic.loadUi("entrada.ui")
entrada.pushButton_login.clicked.connect(funcao_principal)



entrada.show()
app.exec()
