from ursina import *
from scripts.fenetre import Fenetre
from scripts.buttons import Start_Button
from scripts.main_terminal import Terminal
# create a window
fenetre = Fenetre(title=" ", width=800, height=600)


fenetre.run()
start_button = Start_Button().create_start_button()
start_button.parent = camera.ui
start_button.on_click = fenetre.close()
start_button.on_click = Terminal().create_terminal_window()

fenetre.close()
