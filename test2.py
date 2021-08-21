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
    def __init__(self):
        super().__init__()
        self.sprite_list = arcade.SpriteList()
        self.ui_manager = UIManager()

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_BLUE)
        self.on_draw()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def on_draw(self):
        arcade.start_render()
        y = 635
        #arcade.draw_rectangle_filled(width / 2, 0, 400, 150, arcade.color.LIGHT_GRAY)
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
            arcade.draw_rectangle_filled(width / 2, 500, 340, 200, arcade.color.BLACK)
            arcade.draw_text("Click the '+' to add", width / 2, 510, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
            arcade.draw_text("your first password", width / 2, 465, arcade.color.WHITE, 24,
                             anchor_x="center", font_name='Verdana')
        else:
            for x in range(len(passwordlistname)):
                arcade.draw_rectangle_filled(width / 2, 575 - (80*x), 350, 70, arcade.color.BLACK)
                self.remove_list: arcade.SpriteList = arcade.SpriteList()
                remove = Icon("Images/3.png", 0.1)
                remove.position = 200, 575 - (80*x)
                self.remove_list.append(remove)
                arcade.draw_text(passwordlistname[x], 50, 572 - (80*x), arcade.color.BLACK, 18, font_name='Verdana')
                arcade.draw_text("Username: " + passwordlistusername[x], 50, 550 - (80 * x), arcade.color.BLACK, 12, font_name='Verdana')
                x = MyFlatButton(" ", center_x=160, center_y=575-(80*x), width=270, height = 70)
                self.ui_manager.add_ui_element(x)
            self.remove_list.draw()


class PasswordView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BRIGHT_NAVY_BLUE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("PLEASE", 200, 200, arcade.color.BRIGHT_NAVY_BLUE, 30)


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self):
        print("Clicked")
        password_view = PasswordView()
        password_view.on_show()


def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
