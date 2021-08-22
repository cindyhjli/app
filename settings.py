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
        arcade.draw_text("Settings", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 20,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_rectangle_filled(width / 2, 615, 350, 40, arcade.color.DARK_GRAY)
        arcade.draw_text("Search", 30, 603, arcade.color.LIGHT_GRAY, 16, font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Profile", 30, 550, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 550, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Manage Tags", 30, 500, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text(">", 340, 500, arcade.color.BLACK, 16, font_name='Verdana Bold')

        arcade.draw_text("Require Login to View", 30, 450, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Passwords", 30, 425, arcade.color.BLACK, 16, font_name='Verdana Bold')



def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
