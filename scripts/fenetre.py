from ursina import Ursina, window, Entity, camera, color, Button, Text, destroy

from scripts.buttons import Start_Button
from scripts.main_terminal import Terminal
class Fenetre:
    """Formulate a basic windows XP UI"""
    
    def __init__(self, title=" ", width=1920, height=1080, color=color.azure):
        self.app = Ursina()
        window.title = title
        window.size = (width, height)
        # self.window = WindowPanel(title=title, width=width, height=height, color=color)
        self.background = None

    def load_wallpaper(self, image_path):
        """Load a wallpaper image as the window background."""
        # Create a fullscreen quad for the background
        self.background = Entity(
            model='quad',
            texture=image_path,
            parent=camera.ui,
            scale=(2, 2),  # Cover entire screen in UI space
            z=100,  # Put it far in the background
            color=color.white
        )
    
    def load_application_icon(self, icon_path):
        """Load an application icon into the window."""
        
        # Create an icon in UI space
        self.app_icon = Entity(
            model='quad',
            texture=icon_path,
            parent=camera.ui,
            scale=(0.1, 0.1),  # Small icon size
            position=(-0.8, 0.45),  # Top-left corner in UI space
            z=-1  # Bring it in front of the background
        )
        
        #add application icon name under the icon
        self.app_icon_name = Text(
            text="Alimi Gil",
            parent=camera.ui,
            position=(-0.85, 0.4),
            scale=0.9,
            color=color.white,
            z=-1
        )
    
    def delete_application_icon(self):
        """Delete the application icon from the window."""
        if hasattr(self, 'app_icon'):
            destroy(self.app_icon)
        if hasattr(self, 'app_icon_name'):
            destroy(self.app_icon_name)
    
    def delete_wallpaper(self):
        """Delete the wallpaper from the window."""
        if hasattr(self, 'background'):
            destroy(self.background)
    
    def open_terminal_and_close_fenetre(self):
        """Open terminal window and destroy fenetre elements."""
        # Create and open terminal
        self.terminal.create_terminal_window()
        self.terminal.text_generate()
        # Destroy fenetre elements
        self.delete_application_icon()
        self.delete_wallpaper()
        
        # Destroy the start button
        if hasattr(self, 'start_button'):
            destroy(self.start_button)
        
        
    def close(self):
        self.app.quit()    
        
    def run(self):
        # self.window.enabled = True
        self.load_wallpaper('../assets/WinXp/Wallpapers/Bliss.png')
        self.load_application_icon('../assets/WinXp/Logo/alimi-gil.png')
        self.start_button = Start_Button().create_start_button()
        self.terminal = Terminal()
        self.start_button.parent = camera.ui
        
        self.start_button.on_click = self.open_terminal_and_close_fenetre
        
        self.app.run()
