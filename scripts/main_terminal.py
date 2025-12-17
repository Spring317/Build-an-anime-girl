from ursina import Entity, camera, color, Text

class Terminal: 
    """Create a basic terminal window"""
    
    def __init__(self):
        pass
    
    def create_terminal_window(self, title="Terminal", width=800, height=600, color=color.black):
        """Create a terminal window with given title, width, height and color."""
        self.terminal_window = Entity(
                model='quad',
                parent=camera.ui,
                scale=(2, 2),  # Cover entire screen in UI space
                z=100,  # Put it far in the background
                color = color
            )
        
        return self.terminal_window
    
    def text_generate(self, content="Welcome to the Terminal", position=(-0.65,0.45), scale=1, color=color.white):
        """Generate text in the terminal window."""
        terminal_text = Text(
            text=content,
            parent=camera.ui,
            position=position,
            scale=scale,
            color=color,
            z=-1
        )
        return terminal_text
    
    