class ExoticCar():
    wheels = 4
    top_speed = "255 mph"
    time_travel = True
    def driveFast(self):
        print(f"Driving super fast. Might reach {ExoticCar().top_speed}.")


print(type(ExoticCar))

# Instantiate ExoticCar
my_car = ExoticCar()
print(type(my_car))
# Access the class attribute
print(my_car.wheels)
# Invoke the method
my_car.driveFast()
# Truthy conditional with attribute
if (my_car.time_travel):
    print(f"time_travel is {my_car.time_travel}")