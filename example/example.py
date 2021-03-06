'''
Created on 10/06/2016

@author: George
'''

import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

import pygame

from PygameGtkCanvas import PygameGtkCanvas

class Example(Gtk.Window):
    def __init__(self):
        super().__init__(title="Pygame multiwindow example")

        self.set_size_request(650, 450)

        new_button = Gtk.Button.new_with_label("New window")
        new_button.connect("clicked", lambda win: Example())

        self.pygtkcanvas = PygameGtkCanvas(650, 400)
        self.pygtkcanvas.surf_draw = self.surf_draw
        self.font = pygame.font.SysFont("monospace", 16)
        self.image = self.pygtkcanvas.load_image("python_logo.png")

        vbox = Gtk.VBox(False, 1)
        vbox.pack_start(new_button, False, False, 0)
        vbox.pack_start(self.pygtkcanvas, True, True, 0)
        self.add(vbox)


        self.show_all()

    def surf_draw(self, surface):
        surface.fill((0, 0, 0))
        fps_label = self.font.render("{:.02f}".format(self.pygtkcanvas.fps), 0, (255, 255, 255))

        surface.blit(fps_label, (15, 15))
        surface.blit(self.image, (15, 30))


if __name__ == "__main__":
    win = Example()
    win.connect("delete-event", Gtk.main_quit)
    Gtk.main()