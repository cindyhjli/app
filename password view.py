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
        arcade.draw_text("Instagram", width / 2, 650, arcade.color.BRIGHT_NAVY_BLUE, 20,
                         anchor_x="center", font_name='Verdana Bold')
        arcade.draw_text("< Back", 15, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Edit", 325, 652, arcade.color.BLACK, 16, font_name='Verdana Bold')
        arcade.draw_text("Username", 30, 570, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("@cd_tech", 30, 540, arcade.color.BLACK, 18)
        arcade.draw_text("Password", 30, 480, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("••••••••••", 30, 450, arcade.color.BLACK, 25)
        arcade.draw_text("Url", 30, 400, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("www.instagram.com", 30, 370, arcade.color.BLACK, 18)
        arcade.draw_text("Tag", 30, 310, arcade.color.BRIGHT_NAVY_BLUE, 18, font_name='Verdana Bold')
        arcade.draw_text("Social Media", 30, 280, arcade.color.PURPLE, 18)

def main():
    window = arcade.Window(width, height, title)
    main_view = MainView()
    window.show_view(main_view)
    arcade.run()


main()
