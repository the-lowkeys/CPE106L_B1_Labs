# Solution File for the Post Lab 2
import tkinter as tk
from tkinter import filedialog as tkfd

main_window = tk.Tk()
main_window.withdraw()
dialog = tkfd.askopenfilename(title='File?',
                              filetypes=[('All Files', '*.*')])

chosen_file = dialog.rsplit('/')
print('Chosen File Name: ', chosen_file[-1])

main_window.destroy() # Close after test