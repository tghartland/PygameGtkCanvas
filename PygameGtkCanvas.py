'''
Created on 10/06/2016

@author: George
'''

import gi
import pygame
gi.require_version('Gtk', '3.0')
gi.require_version('GdkX11', '3.0')
from gi.repository import Gtk, GObject, GdkX11, Gdk, GdkPixbuf, GLib

import time

class PygameGtkCanvas(Gtk.Image):
    def __init__(self, width, height):
        super().__init__()

        pygame.display.init()

        self.last_tick_time = time.perf_counter()

        self.surface = pygame.Surface((width, height))

        self.fps = 0

        self.pixbuf = GdkPixbuf.Pixbuf()

        GObject.timeout_add(16, self.on_draw)

    def on_draw(self):
        """
        Draws surface to the Gtk.Image
        :return: None
        """
        self.surf_draw(self.surface)

        cur_time = time.perf_counter()
        self.fps = 1/(cur_time-self.last_tick_time)
        self.last_tick_time = cur_time

        surface_data = GLib.Bytes(pygame.image.tostring(self.surface, "RGB"))

        pix = self.pixbuf.new_from_bytes(surface_data, GdkPixbuf.Colorspace.RGB, False, 8,
                                         self.surface.get_width(),
                                         self.surface.get_height(),
                                         self.surface.get_width()*3)

        self.set_from_pixbuf(pix.copy()) # Massive memory leak without .copy()
        self.queue_draw_area(0, 0, self.surface.get_width(), self.surface.get_height())

        # return True to continue the ticking
        return True

    def surf_draw(self, surface):
        """
        Replace this method to blit to the surface before each draw tick
        :param surface: surface to draw to
        :return: None
        """
        pass