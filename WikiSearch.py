from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
from tkinter.messagebox import askokcancel, showinfo
import threading


def search():
    global lang_dict
    search_data = ent.get()
    if search_entry:
        val = lang.get()
        text.delete(0.0, END)
        text.insert(END, f'Searching for {search_data}...')
        try:
            wiki.set_lang(lang_dict[val])
            data = wiki.summary(search_data, sentences=6)
        except Exception as e:
            data = e

        ent.set('')
        text.delete(0.0, END)
        # insert data
        text.insert(END, data)
        search_label['text'] = f'Search for: {search_data}'


def call_search(*args):
    x = threading.Thread(target=search())
    x.start()


def call_back_for_root():
    if askokcancel('Quit', 'Do you really want to quit?'):
        root.quit()


def copy_data(*args):
    data = text.get(0.0, END)
    if data:
        root.clipboard_clear()
        root.clipboard_append(data)
        showinfo('Copy', 'Data is copied to the clipdoard')


# main window
root = Tk()
root.title('WikiSearch')
root.geometry('320x480')
root.resizable(0, 0)
root.protocol('WM_DELETE_WINDOW', call_back_for_root)
root.config(bg='white')

lang_dict = {'English': 'en', 'German': 'de', 'Russian': 'ru'}

ent = StringVar()
lang = StringVar()

search_entry = Entry(root, width=21, font=('arial', 14), bd=2, relief=RIDGE, textvariable=ent)
search_entry.bind('<Return>', call_search)
search_entry.place(x=15, y=20)

img = PhotoImage(file='search.png')
search_button = Button(root, image=img, bd=2, relief=GROOVE, command=call_search)
search_button.place(x=250, y=20)

search_label = Label(root, text='Search For:', font=('arial', 12, 'bold'), bg='white')
search_label.place(x=15, y=70)

text = ScrolledText(root, font=('arial', 12), bd=2, relief=SUNKEN, wrap=WORD, undo=True)
text.bind('<Double-1>', copy_data)
text.place(x=15, y=100, height=300, width=300)

lang_list = list(lang_dict.keys())
lang.set(lang_list[0])

language = OptionMenu(root, lang, *lang_list)
language.place(x=10, y=420)

clear_btn = Button(root, width=10, text='Clear', font=('arial', 10, 'bold'), command=lambda: text.delete(0.0, END))
clear_btn.place(x=100, y=420)

exit_btn = Button(root, width=10, text='Exit', font=('arial', 10, 'bold'), command=root.quit)
exit_btn.place(x=210, y=420)

root.mainloop()
