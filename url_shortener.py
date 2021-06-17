from tkinter import * 
from tkinter import ttk
import pyshorteners
import clipboard

# main window
root = Tk()
root.title('Url Shortener')
root.geometry('400x200')
root.wm_iconbitmap('url_shortener.ico')
root.resizable(False, False)

# entry and label

url_entry = ttk.Entry(root, font='Helvetica, 12', width=42)
url_entry.grid(row=0, column=0, padx=10, pady=10)

str_url = StringVar()

shortened_url = ttk.Label(root, textvariable=str_url, foreground='blue', background='grey')
shortened_url.grid(row=2, columnspan=2, padx=10, pady=10)

# shorten button

def short_url():
    try:
        s = pyshorteners.Shortener()
        url = url_entry.get()
        new_url = s.tinyurl.short(url)
        str_url.set(new_url)
        url_entry.delete(0, END)
    except:
        str_url.set('Error! Please enter the url again.')

btn = ttk.Button(root, text='Short Url', command=short_url)
btn.grid(row=1, columnspan=2, padx=10, pady=10)

# copy button

def copy_url():
    try:
        clipboard.copy(str_url.get())
        print('Url Copied Successfully!')
    except:
        str_url.set('Something went wrong!!')

copy_btn = ttk.Button(root, text='Copy', command=copy_url)
copy_btn.grid(row=3, columnspan=2, padx=10, pady=10)


root.mainloop()