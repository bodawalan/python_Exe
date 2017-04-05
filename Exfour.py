cars=100 # intialize value 100 to car
space_in_car = 4.0 # intialize float vale to the variable
drivers = 30
passenges = 90

cars_not_driven = cars - drivers

cars_driven = drivers
carpool_capacity = cars_driven * space_in_car

average_passengers_per_car = passenges / cars_driven

print("there are {} cars avilable".format(cars))

print("There are only {} drivers avilable ".format(drivers))

print("There will be {} empty cars".format(cars_not_driven))

print("we can transport {} people today in ".format(carpool_capacity))

print("we have {} to carpool today".format(passenges))

print("we need to put about {} in each car".format(average_passengers_per_car))