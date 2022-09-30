##################### --> INGRESSO DISPONÍVEL <-- #####################

# Este bot será criado para informar quando estiver ingresso disponível
# e aparecerá um alerta na tela dizendo INGRESSO DISPONÍVEL.

#---------------------------------------------------------------------#

import webbrowser
import pyautogui
from time import sleep

#### PASSOS ####

# 1 - Entrar no site
webbrowser.open('https://www.eventim.com.br/artist/coldplay-0/coldplay-rio-de-janeiro-3117750/')
sleep(3)

# 2 - Dar um scroll ou pegar a barra lateral até a parte dos ingressos
teclaBar = pyautogui.locateCenterOnScreen('barLat.png')
pyautogui.click(teclaBar[0],teclaBar[1],duration=2)
sleep(2)

 #3 Descer até a parte dos ingressos (pode mudar a distância/px dependendo do monitor)
pyautogui.dragTo()
pyautogui.scroll(-800)
sleep(2)

while True:
    # Se não estiver disponível, recomeçar com F5
    if pyautogui.locateCenterOnScreen('ingrDisp.png'):
        pyautogui.alert('TEM INGRESSO DISPONÍVEL!')
        break
    else:
        pyautogui.hotkey('F5')
        sleep(4)