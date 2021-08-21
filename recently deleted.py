import arcade
import arcade.gui
from arcade.gui import UIManager

width = 400
height = 700
title = "passwordapp"


class MainView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Recently Deleted", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 18,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Select", 322, 652, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Delete All", 285, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')
        arcade.draw_text("Recover All", 15, 30, arcade.color.BLACK, 14, font_name='Verdana Bold')

        arcade.draw_rectangle_filled(width / 2, 560, 350, 100, arcade.color.DARK_GRAY)
        arcade.draw_text("Passwords will be permanently", width / 2, 565, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')
        arcade.draw_text("deleted after 30 days", width / 2, 535, arcade.color.WHITE, 16,
                         anchor_x="center", font_name='Verdana')

        arcade.draw_rectangle_filled(width / 2, 450, 350, 70, arcade.color.BLACK)
        arcade.draw_text("Instagram", 50, 445, arcade.color.WHITE, 22)
        arcade.draw_text("Username: cd_tech", 50, 425, arcade.color.WHITE, 12)

        self.icon_list: arcade.SpriteList = arcade.SpriteList()
        remove = Icon("Images/3.png", 0.04)
        remove.position = 340, 575
        self.icon_list.append(remove)
        self.icon_list.draw()

class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)

def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
