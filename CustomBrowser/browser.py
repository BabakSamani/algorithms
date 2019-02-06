#!/usr/bin/env python2

# import sys
# from PySide.QtGui import QApplication
# from PySide.QtCore import QUrl
# from PySide.QtWebKit import QWebView

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

gi.require_version('WebKit', '3.0')
from gi.repository import WebKit

# import WebKit

# window = Gtk.Window(title="Hello World")
# window.show()
# window.connect("destroy", Gtk.main_quit)
# Gtk.main()


def get_address(widget):
    address = addressbar.get_text()
    if address.startswith("https://www."):
        web.open(address)
    else:
        address = "https://www." + address
        addressbar.set_text(address)
        web.open(address)


win = Gtk.Window()
win.set_position(Gtk.WindowPosition.CENTER)
win.set_size_request(1200, 600)
win.connect('destroy', lambda w: Gtk.main_quit())

box1 = Gtk.VBox()
box2 = Gtk.HBox()

win.add(box1)
box1.pack_start(child=box2, expand=False, fill=False, padding=0)

addressbar = Gtk.Entry()

box2.pack_start(child=addressbar, expand=True, fill=True, padding=0)

goButton = Gtk.Button(label='GO')

box2.pack_start(child=goButton, expand=False, fill=True, padding=0)
goButton.connect('clicked', get_address)

scroller = Gtk.ScrolledWindow()

box1.pack_start(child=scroller, expand=True, fill=True, padding=0)

web = WebKit.WebView()
scroller.add(web)

win.show_all()
Gtk.main()
