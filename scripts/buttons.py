from ursina import *

class Start_Button:
    """Create basic buttons for the UI"""
    
    def __init__(self):
        pass
    
    def _button(self, text, position=(0,0), scale=(0.2,0.1), color=color.azure):
        """Create a button with given text, position, scale and color."""
        button = Button(
            text=text,
            position=position,
            scale=scale,
            color=color
        )
        return button
    
    def create_start_button(self):
        """Create a Start button for the UI."""
        start_button = self._button(
            text="Start",
            position=(-0.8, 0.45),
            scale=(0.15, 0.1),
            color=color.yellow
        )
        return start_button
    
    # def create_close_button(self):
    #     """Create a Close button for the UI."""
    #     close_button = self._button(
    #         text="Close",
    #         position=(0.9, 0.45),
    #         scale=(0.1, 0.05),
    #         color=color.red
    #     )
    #     return close_button
    
    # def create_minimize_button(self):
    #     """Create a Minimize button for the UI."""
    #     minimize_button = self._button(
    #         text="Minimize",
    #         position=(0.75, 0.45),
    #         scale=(0.1, 0.05),
    #         color=color.yellow
    #     )
    #     return minimize_button
    
    # def create_maximize_button(self):
    #     """Create a Maximize button for the UI."""
    #     maximize_button = self._button(
    #         text="Maximize",
    #         position=(0.6, 0.45),
    #         scale=(0.1, 0.05),
    #         color=color.blue
    #     )
    #     return maximize_button
    
    # def create_custom_button(self, text, position, scale, color):
    #     """Create a custom button with specified parameters."""
    #     custom_button = self._button(
    #         text=text,
    #         position=position,
    #         scale=scale,
    #         color=color
    #     )
    #     return custom_button

    