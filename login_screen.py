import arcade
import globalValues
import arcade.gui
from arcade.gui import UIManager

width = 400
height = 700
title = "Password Manager"


class Button(arcade.gui.UIFlatButton):
    def __init__(self, center_x, center_y, str, ui_manager, width):
        super().__init__(center_x=center_x, center_y=center_y, text=str, width=width)
        self.ui_manager = ui_manager

    def on_click(self):
        self.ui_manager.purge_ui_elements()


class EntryScreen(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.ui_manager = UIManager()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Log in to your account", start_x=20, start_y=600, color=arcade.color.WHITE, font_size=30)
        arcade.draw_text(".......................................................", start_x=20, start_y=500, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Username:", start_x=20, start_y=400, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Password:", start_x=20, start_y=300, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Logged in!", start_x=125, start_y=180, color=arcade.color.WHITE, font_size=20)

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        global_values = globalValues.GlobalValues()
        self.ui_manager.purge_ui_elements()
        # add button
        button = Button(str="Log in", center_x=200, center_y=200, ui_manager=self.ui_manager, width=200)
        self.ui_manager.add_ui_element(button)
        # input box username
        input_box = arcade.gui.UIInputBox(center_x=265, center_y=420, width=250)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
        # input box password
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=320, width=260)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)



def main():
    window = arcade.Window(title="Test", width=400, height=700)
    page = EntryScreen()
    window.show_view(page)
    arcade.run()


main()
