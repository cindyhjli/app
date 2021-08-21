import arcade
import arcade.gui
from arcade.gui import UIManager


class MyFlatButton(arcade.gui.UIFlatButton):
    def on_click(self):
        print("Clicked")


class MyView(arcade.View):
    def __init__(self):
        super().__init__()
        self.ui_manager = UIManager()

    def on_draw(self):
        arcade.start_render()

    def on_show_view(self):
        self.setup()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()
        button = MyFlatButton("FLATBUTTON", center_x=200, center_y=200, width=200)
        self.ui_manager.add_ui_element(button)

window = arcade.Window(title="Test")
view = MyView()
window.show_view(view)
arcade.run()