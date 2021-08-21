import arcade


width = 400
height = 700
title = "passwordapp"


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


class Icon(arcade.Sprite):
    def __init__(self, filename, scale):
        super().__init__(filename=filename, scale=scale)


def main():
    window = Main()
    window.setup()
    arcade.run()


main()
