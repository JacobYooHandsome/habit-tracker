import pixela_functions as pf
from tkinter import *
import tkcalendar as tkc

window = Tk()
window.title("habit-tracker")
window.config(padx=50, pady=50, bg="#394867")

cal = tkc.Calendar()
cal.grid(row=1, column=0, columnspan=2, pady=10)
cal.configure(background="white", selectforeground="white", headersforeground="red", date_pattern="ymmdd")

title = Label(text="Habit Tracker", font=("Lato", 20, "bold"), background="#394867")
title.grid(row=0, column=0, columnspan=2)

post = Button(text="POST", width=8, highlightbackground="#394867", command=lambda: pf.post_pixel(entry.get(), cal.get_date()))
post.grid(row=3, column=0)

update = Button(text="UPDATE", width=8, highlightbackground="#394867", command=lambda: pf.update_pixel(entry.get(), cal.get_date()))
update.grid(row=4, column=0)

delete = Button(text="DELETE", width=8, highlightbackground="#394867", command=lambda: pf.delete_pixel(cal.get_date()))
delete.grid(row=3, column=1)

show = Button(text="SHOW", width=8, highlightbackground="#394867", bg="#212A3E", command=pf.open_link)
show.grid(row=4, column=1)

text = Label(text="RATING:", highlightbackground="#394867", background="#394867")
text.grid(row=2, column=0, pady=20, sticky="E")
entry = Spinbox(width=3, highlightbackground="#394867", increment=1, from_=1, to=10)
entry.grid(row=2, column=1, sticky="W")

window.mainloop()
