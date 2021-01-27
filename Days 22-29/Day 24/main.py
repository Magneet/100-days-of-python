import tkinter
window = tkinter.Tk()
window.title("yeah a gui")

window.minsize(width = 500, height = 300)

label = tkinter.Label(text = "bla", font =("Arial", 23, "bold "))
label["text"]= "bla2"
label.config(text="bla3")
button = tkinter.Button(text="don't click here")
label.pack()
button.pack()





window.mainloop()


# def my_function(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)


# my_function(1,6,8,5,4)

# def my_function(**kwargs):
#     for key, value in kwargs.items():
#         print(key)
#         print(value)
# my_function(add=3, multiply=7)

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")

# my_car = Car(make="Slopel", model="Brak")
# print(my_car.model)