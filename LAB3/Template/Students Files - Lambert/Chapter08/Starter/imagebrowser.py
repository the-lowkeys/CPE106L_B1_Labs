"""
File: imagebrowser.py
Project 8.9

Browser for image (.gif) files.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog

class ImageBrowser(EasyFrame):

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Browser")
        self.setSize(220, 200)

        # self.imageLabel
        # self.addButton(find image button)

    def findImage(self):
        """Pops up an open file dialog, and if a file is selected, displays its image in the label and its pathname in the title bar."""
        # Write your code here

def main():
    """Instantiate and pop up the window."""
    ImageBrowser().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
    
