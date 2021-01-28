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