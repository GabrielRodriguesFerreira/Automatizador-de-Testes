import pyautogui
import time

def exibir_coordenadas_mouse():
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Coordenadas do mouse: x={x}, y={y}")

            time.sleep(5)
    except KeyboardInterrupt:
        print("Programa interrompido pelo usuário.")

if __name__ == "__main__":
    exibir_coordenadas_mouse()
