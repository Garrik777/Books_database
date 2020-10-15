'''
User GUI with Tkinter
Grid method is used
'''

from tkinter import *
import Database.backend as backend

selected_tuple = ()


def view_command():
    list_box.delete(0, END)
    for row in backend.view_table():
        list_box.insert(END, row)


def search_command():
    list_box.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)


def add_command():
    backend.add_record(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list_box.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    title_text.set('')
    author_text.set('')
    year_text.set('')
    isbn_text.set('')


def get_selected_row(event):
    global selected_tuple
    if list_box.get(0):
        index = list_box.curselection()[0]
        selected_tuple = list_box.get(index)
        title_entry.delete(0, END)
        title_entry.insert(END, selected_tuple[1])
        author_entry.delete(0, END)
        author_entry.insert(END, selected_tuple[2])
        year_entry.delete(0, END)
        year_entry.insert(END, selected_tuple[3])
        isbn_entry.delete(0, END)
        isbn_entry.insert(END, selected_tuple[4])


def delete_command():
    backend.delete_record(selected_tuple[0])
    view_command()


def update_command():
    backend.update_record(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    view_command()


main_window = Tk()
main_window.title('Books DB')

title_label = Label(main_window, text='Title')
title_label.grid(row=0, column=0)
title_text = StringVar()
title_entry = Entry(main_window, textvariable=title_text)
title_entry.grid(row=0, column=1)

author_label = Label(main_window, text='Author')
author_label.grid(row=0, column=2)
author_text = StringVar()
author_entry = Entry(main_window, textvariable=author_text)
author_entry.grid(row=0, column=3)

year_label = Label(main_window, text='Year')
year_label.grid(row=1, column=0)
year_text = StringVar()
year_entry = Entry(main_window, textvariable=year_text)
year_entry.grid(row=1, column=1)

isbn_label = Label(main_window, text='ISBN')
isbn_label.grid(row=1, column=2)
isbn_text = StringVar()
isbn_entry = Entry(main_window, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3)

list_box = Listbox(main_window, height=6, width=35)
list_box.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(main_window)
scrollbar.grid(row=2, column=2, rowspan=6)

list_box.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=list_box.yview)

list_box.bind('<<ListboxSelect>>', get_selected_row)

view_all_button = Button(text='View all', width=12, command=view_command)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(text='Search entry', width=12, command=search_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(text='Add entry', width=12, command=add_command)
add_entry_button.grid(row=4, column=3)

update_button = Button(text='Update selected', width=12, command=update_command)
update_button.grid(row=5, column=3)

delete_button = Button(text='Delete selected', width=12, command=delete_command)
delete_button.grid(row=6, column=3)

close_button = Button(text='Close', width=12, command=main_window.destroy)
close_button.grid(row=7, column=3)

main_window.mainloop()
