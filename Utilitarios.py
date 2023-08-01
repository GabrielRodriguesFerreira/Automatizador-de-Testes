import subprocess
import time
import pyautogui
import psutil
import pygetwindow as gw
import win32gui
from pynput.mouse import Button, Controller


class Utilitarios:
    def __init__(self):
        self.x_coord = 50
        self.y_coord = 64
        self.tempoAplicativoSpoon = 35
        self.tempoAplicativoAbrir = 5
        self.tempoAplicativoSpoonUpdate = 5
        self.caminho_aplicativo = "C:/data-integration-Oracle/Spoon.bat"
        self.texto_pesquisa = "sourceUpdate.kjb"
        self.nome_aplicativoSpoon = "Spoon - [no name]"
        self.nome_aplicativoSpoon_Abrir = "Abrir"
        self.nome_aplicativoSpoonUpdate = "Spoon - sourceUpdate"
        self.x_coord_pesq = 1257
        self.y_coord_pesq = 57
        self.x_coord_src = 316
        self.y_coord_src = 649
        self.x_coord_open = 1184
        self.y_coord_open = 710
        self.x_coord_dtfim = 701
        self.y_coord_dtfim = 410
        self.x_coord_dtini = 719
        self.y_coord_dtini = 424
        self.numeroRodadas = 2
        self.dtfim_padrao = "2100-01-01"
        self.dtini_padrao = "1900-01-01"
        self.x_clicarRun = 919
        self.y_clicarRun = 622
        self.x_abrirIntegration = 926
        self.y_abrirIntegration = 378

    def abrir_aplicativo(self):
        try:
            subprocess.Popen(self.caminho_aplicativo)
            return True
        except Exception as e:
            print(f"Erro ao abrir o aplicativo: {e}")
            return False

    def aguardar_abrir_aplicativo(self):
        tempo_passado = 0
        while self.nome_aplicativoSpoon not in pyautogui.getActiveWindowTitle():
            time.sleep(1)
            tempo_passado += 1
            if tempo_passado > self.tempoAplicativoSpoon:
                print("Tempo limite excedido. O aplicativo não foi aberto.")
                return False
        return True

    def aguardar_abrir_aplicativo_Update(self):
        tempo_passado = 0
        while self.nome_aplicativoSpoonUpdate not in pyautogui.getActiveWindowTitle():
            time.sleep(1)
            tempo_passado += 1
            if tempo_passado > self.tempoAplicativoSpoonUpdate:
                print("Tempo limite excedido. O aplicativo não foi aberto.")
                return False
        return True

    def aguardar_abrir_aplicativo_abrir(self):
        tempo_passado = 0
        while self.nome_aplicativoSpoon_Abrir not in pyautogui.getActiveWindowTitle():
            time.sleep(1)
            tempo_passado += 1
            if tempo_passado > self.tempoAplicativoAbrir:
                print("Tempo limite excedido. O aplicativo não foi aberto.")
                return False
        return True

    @staticmethod
    def valida_spoon_aberto(nome_aplicativo):
        janelas_abertas = gw.getWindowsWithTitle(nome_aplicativo)
        if janelas_abertas:
            print(f"O aplicativo {nome_aplicativo} está aberto.")
            return True
        else:
            print(f"O aplicativo {nome_aplicativo} não está aberto.")
            return False

    @staticmethod
    def valida_source_aberto(nome_aplicativo):
        janelas_abertas = gw.getWindowsWithTitle(nome_aplicativo)
        if janelas_abertas:
            print(f"O aplicativo {nome_aplicativo} está aberto.")
            return True
        else:
            print(f"O aplicativo {nome_aplicativo} não está aberto.")
            return False

    @staticmethod
    def valida_integration_aberto(nome_aplicativo):
        janelas_abertas = gw.getWindowsWithTitle(nome_aplicativo)
        if janelas_abertas:
            print(f"O aplicativo {nome_aplicativo} está aberto.")
            return True
        else:
            print(f"O aplicativo {nome_aplicativo} não está aberto.")
            return False

    def clicar_em_local_pastas(self, x_coord, y_coord):
        pyautogui.click(x_coord, y_coord)
        pyautogui.sleep(1)

    def clicar_em_local_arquivo_pesquisar(self, x_coord_pesq, y_coord_pesq):
        pyautogui.click(x_coord_pesq, y_coord_pesq)
        pyautogui.sleep(1)

    def clicar_em_local_arquivo_source(self, x_coord_src, y_coord_src):
        pyautogui.click(x_coord_src, y_coord_src)
        pyautogui.sleep(1)

    def clicar_em_local_arquivo_source_open(self, x_coord_open, y_coord_open):
        pyautogui.click(x_coord_open, y_coord_open)
        pyautogui.sleep(1)

    def rolar_pesquisa (self):
        for _ in range(self.numeroRodadas):
            pyautogui.hotkey('ctrl', 'pagedown')
        pyautogui.sleep(1)

    def clicar_executar(self):
        pyautogui.hotkey('F9')
        pyautogui.sleep(1)
    
    def clicar_dtfim(self, x_coord_dtfim, y_coord_dtfim):
        pyautogui.click(x_coord_dtfim, y_coord_dtfim)
        pyautogui.sleep(1)

    def clicar_dtini(self, x_coord_dtini, y_coord_dtini):
        pyautogui.click(x_coord_dtini, y_coord_dtini)
        pyautogui.sleep(1)

    @staticmethod
    def escrever_data(dtpadrao):
        pyautogui.write(dtpadrao)

    def clicar_run(self, x_clicarRun, y_clicarRun):
            pyautogui.click(x_clicarRun, y_clicarRun)
            pyautogui.sleep(1)

    def clicar_scroll_mouse(self):
        mouse = Controller()
        mouse.click(Button.middle)
