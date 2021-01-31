import tkinter
window = tkinter.Tk()

def button_clicked():
    new_label = input_field.get()
    label.config(text = new_label)

def break_clicked():
    window.destroy()

def change_pulldown(event):
    new_label.config(text = variable.get())

window.title("yeah a gui")

window.minsize(width = 500, height = 300)
window.config(padx=10,pady=10)
OPTIONS = [
"Jan",
"Feb",
"Mar"
]
variable = tkinter.StringVar(window)
variable.set(OPTIONS[0]) # default value


label = tkinter.Label(text = "bla", font =("Arial", 23, "bold "))
label["text"]= "bla2"
label.config(text="bla3")

new_label = tkinter.Label(text=variable.get())
button = tkinter.Button(text="don't click here", command=button_clicked)
option_menu = tkinter.OptionMenu(window, variable, *OPTIONS, command=change_pulldown)

end = tkinter.Button(text="Exit", command=break_clicked)

input_field = tkinter.Entry()
input_field.config(width=20)

label.grid(column = 1, row = 1)
button.grid(column = 2, row = 2)
input_field.grid(column = 3, row = 3)
option_menu.grid(column = 4, row = 4)
new_label.grid(column = 5, row = 5)
end.grid(column = 6, row = 6)





window.mainloop()


