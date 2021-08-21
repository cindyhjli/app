import arcade


width = 400
height = 700
title = "passwordapp"

passwordlistname = ["Instagram", "Snapchat"]
passwordlisturl = ["ig.com"]
passwordlistusername = ["danielwangg"]
passwordlistcode = ["12345"]


class Main(arcade.Window):

    def __init__(self):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.sprite_list = arcade.SpriteList()

    def setup(self):
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
                arcade.draw_rectangle_filled(width / 2, 550 - (60*x), 350, 50, arcade.color.LIGHT_GRAY)
                arcade.draw_text(passwordlistname[x], 60, 538 - (60*x), arcade.color.BLACK, 18, font_name='Verdana')

class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


def main():
    window = Main()
    window.setup()
    arcade.run()


main()
