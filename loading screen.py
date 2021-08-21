import arcade

width = 400
height = 700
title = "passwordapp"

class LoadingView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("PM", width/2, 440, arcade.color.BRIGHT_NAVY_BLUE, 100, anchor_x="center", anchor_y="center", font_name='Verdana Bold')
        arcade.draw_text("Password Manager", width/2, 360, arcade.color.BRIGHT_NAVY_BLUE, 25, anchor_x="center", anchor_y="center", font_name='Verdana Bold')
        arcade.draw_text("CD Tech", width/2, 185, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", font_name='Verdana Bold')
        arcade.draw_text("2021", width/2, 150, arcade.color.BLACK, 20, anchor_x="center", anchor_y="center", font_name='Verdana Bold')

def main():
    window = arcade.Window(width, height, title)
    loading_view = LoadingView()
    window.show_view(loading_view)
    arcade.run()


main()
