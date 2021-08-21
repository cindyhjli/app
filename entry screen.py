import arcade
import globalValues

width = 400
height = 700
title = "Create a new record"


class EntryScreen(arcade.Window):

    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.LIGHT_STEEL_BLUE)

    def setup(self):
       global_values = globalValues.GlobalValues()

    def on_draw(self):
        arcade.start_render()


def main():
    window = EntryScreen()
    window.setup()
    arcade.run()


main()
