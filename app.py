##################### --> INGRESSO DISPONÍVEL <-- #####################

# Este bot será criado para informar quando estiver ingresso disponível
# e aparecerá um alerta na tela dizendo INGRESSO DISPONÍVEL.

#---------------------------------------------------------------------#

import webbrowser
import pyautogui
from time import sleep

#### PASSOS ####

# 1 - Entrar no site
webbrowser.open('https://www.eventim.com.br/artist/backstreet-boys-00/backstreet-boys-curitiba-3148055/')
sleep(3)

# 2 - Dar um scroll ou pegar a barra lateral até a parte dos ingressos
teclaBar = pyautogui.locateCenterOnScreen('barLat.png')
pyautogui.click(teclaBar[0],teclaBar[1],duration=2)
sleep(2)

#3 Descer até a parte dos ingressos (pode mudar a distância/px dependendo do monitor)
pyautogui.dragTo()
pyautogui.scroll(-800)
sleep(2)

ingresso = pyautogui.locateCenterOnScreen('ingrDisp.png')
while ():
    # Verificar se a imagem é disponível ou insisponível
    ingresso = pyautogui.locateCenterOnScreen('ingrDisp.png')
    sleep(3)
    # Se não estiver disponível, recomeçar com F5
    if ingresso == True:
        pyautogui.hotkey('F5')
        # Se ele não estiver disponível, reiniciar.
    elif ingresso is not True:
        pyautogui.alert('TEM INGRESSO DISPONÍVEL!')