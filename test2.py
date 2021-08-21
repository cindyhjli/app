import arcade
import arcade.gui
from arcade.gui import UIManager

width = 400
height = 700
title = "passwordapp"

passwordlistname = ["Instagram", "Snapchat"]
passwordlisturl = ["ig.com"]
passwordlistusername = ["danielwangg", "dan"]
passwordlistcode = ["12345"]


class MainView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)
        self.sprite_list = arcade.SpriteList()
        self.ui_manager = UIManager()

    def on_draw(self):
        arcade.start_render()
        y = 635
        arcade.draw_rectangle_filled(width / 2, 0, 400, 150, arcade.color.LIGHT_GRAY)
        arcade.draw_text("PASSWORDS", width / 2, y, arcade.color.BRIGHT_NAVY_BLUE, 28,
                         anchor_x="center", font_name='Verdana Bold')

        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        add = Icon("Images/2.png", 0.04)
        add.position = 35, 657
        self.pile_mat_list.append(add)

        settings = Icon("Images/1.png", 0.04)
        settings.position = 365, 658
        self.pile_mat_list.append(settings)

        self.pile_mat_list.draw()

        if len(passwordlistname) == 0:
            arcade.draw_rectangle_filled(width / 2, 500, 340, 200, arcade.color.LIGHT_GRAY)
            arcade.draw_text("Click the '+' to add", width / 2, 510, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
            arcade.draw_text("your first password", width / 2, 465, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
        else:
            for x in range(len(passwordlistname)):
                arcade.draw_rectangle_filled(width / 2, 575 - (80*x), 350, 70, arcade.color.LIGHT_GRAY)
                self.ui_manager.purge_ui_elements()
                button = MyFlatButton(" ", center_x=0, center_y=0, width=200, height=300)
                self.ui_manager.add_ui_element(button)
                arcade.draw_text(passwordlistname[x], 50, 572 - (80*x), arcade.color.BLACK, 18, font_name='Verdana')
                arcade.draw_text("Username:" + passwordlistusername[x], 50, 550 - (80 * x), arcade.color.BLACK, 12, font_name='Verdana')


class PasswordView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("PLEASE", 200, 200, arcade.color.BRIGHT_NAVY_BLUE, 30)


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)

class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self):
        password_view = PasswordView()
        password_view.setup()
        self.window.show_view(password_view)


def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
