#!/usr/bin/python
import os, gi, subprocess
gi.require_version("Gtk", "3.0")
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk, AppIndicator3 as appindicator

def main():
  indicator = appindicator.Indicator.new("customtray", "weather-clear", appindicator.IndicatorCategory.APPLICATION_STATUS)
  indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu())
  gtk.main()

def menu():
  menu = gtk.Menu()
  
  command_one = gtk.MenuItem('Toggle')
  command_one.connect('activate', toggle)
  menu.append(command_one)

  exittray = gtk.MenuItem('Exit Tray')
  exittray.connect('activate', quit)
  menu.append(exittray)
  
  menu.show_all()
  return menu
  
def toggle(_):
    x = subprocess.Popen(["darkman", "toggle"], stdout=subprocess.PIPE).communicate()[0]

def quit(_):
  gtk.main_quit()

if (__name__ == "__main__"):
  main()
