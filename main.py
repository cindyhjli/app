import arcade

width = 400
height = 700
title = "passwordapp"


class Main(arcade.Window):

    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(200, 0, 400, 150, arcade.color.LIGHT_GRAY)


def main():
    window = Main()
    window.setup()
    arcade.run()


main()
