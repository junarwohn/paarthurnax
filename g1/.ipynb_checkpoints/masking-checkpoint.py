#!/usr/bin/python

'''
ZetCode PyCairo tutorial 

This program demonstrates masking.

author: Jan Bodnar
website: zetcode.com
'''


from gi.repository import Gtk
import cairo
import cv2

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        self.load_image()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Masking")
        self.resize(310, 100)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
        
    def load_image(self):    
        # self.ims = cairo.ImageSurface.create_for_data(cv2.imread('penguin.png'))  
        self.ims = cairo.ImageSurface.create_from_png("penguin.png")
        
    
    def on_draw(self, wid, cr):

        cr.mask_surface(self.ims, 100, 100)
        cr.fill()

        
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()
