import arcade
import globalValues
import arcade.gui
from arcade.gui import UIManager

width = 400
height = 700
title = "Create a new record"


class Button(arcade.gui.UIFlatButton):
    def __init__(self, center_x, center_y, str, ui_manager):
        super().__init__(center_x=center_x, center_y=center_y, text=str)
        self.ui_manager = ui_manager

    def on_click(self):
        self.ui_manager.purge_ui_elements()



class GeneratePasswordButton(arcade.gui.UIFlatButton):
    def __init__(self, str, center_x, center_y, ui_manager):
        super().__init__(str, center_x=center_x, center_y=center_y)
        self.ui_manager = ui_manager

    def on_click(self):
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=320, width=260)
        input_box.text = 's3nHyU%ank#Kl'
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)


class EntryScreen(arcade.View):

    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BLACK)
        self.ui_manager = UIManager()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Nickname:", start_x=20, start_y=600, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("URL:", start_x=20, start_y=500, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Username:", start_x=20, start_y=400, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Password:", start_x=20, start_y=300, color=arcade.color.WHITE, font_size=20)
        arcade.draw_text("Entry added!", start_x=125, start_y=180, color=arcade.color.WHITE, font_size=20)

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        global_values = globalValues.GlobalValues()
        self.ui_manager.purge_ui_elements()
        # add button
        button = Button(str="Create entry", center_x=200, center_y=200, ui_manager=self.ui_manager)
        self.ui_manager.add_ui_element(button)
        # input box nickname
        input_box = arcade.gui.UIInputBox(center_x=260, center_y=620, width=255)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
        # input box url
        input_box = arcade.gui.UIInputBox(center_x=230, center_y=520, width=320)
        input_box.text = ''
        input_box.cursor_index = len(input_box.text)
        self.ui_manager.add_ui_element(input_box)
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
        # generate password
        generate_password = GeneratePasswordButton(str="Generate password", center_x=260, center_y=280,
                                                   ui_manager=self.ui_manager)
        self.ui_manager.add_ui_element(generate_password)


def main():
    window = arcade.Window(title="Test", width=400, height=700)
    page = EntryScreen()
    window.show_view(page)
    arcade.run()


main()
