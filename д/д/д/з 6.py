#1
from time import sleep


class Trafficlight:
    _color  = None
    def running(self):
        def out_red(text):
            print(\)

#2
class Road:
    def_init_(self):
    self_lenght = input("Enter lenght of the road:")
    self._width = input("Enter width of the road: ")

    def mass_count(self):
         try:
             mass = int(self_length * int(self_width * 25 * 5))
             return f"mass of the road is {mass}"
         except VallueError as k:
             print(k)
 road_1 = road
print(road_1.mass_count)


#3
class Worker:
    def_init_(self):
    self.name = input("Enter name:")
    self.surname = input(Enter surname:)
    self.posiyion = input("Enter position")
    self.income = {"wage": input("enter wage:")}


class Position(Worker):
    def get full_name(self):
    print(f"Full_name of {self.position} is {self.name} {self.surname}")


def get_total_income(self):
    try:
        total_income = int(self._income.get("wage")) + int(self._income.get("bonus"))
        print(f"Total income of {self.name} {self.surname} is {total_income}")
    except VallueError as k:
        print(k)


worker_1 = Possition()
worker_1.get_full_name()
worker_1.get_total_income()


#4
class Car:
    is_police = False

    def_init_(self):
      self.speed = input("Speed of the car is")
      self.color = input("Color is")
      self.name = input("My name is")
    def go(self):
        print(f"Car {self.name} started movement.")

    def stop (self)
        print(f"Car{self.name} stopped.")

    def turn (self, direction):
        print (f"Car {self.name} turned {direction}")

    def show_speed(self):
        print(f"Car {self.name} has speed {self.speed}")

class Town Car(Car):
    def show_speed(self):
        try:
            self.speed = int(self.speed)
            if self.speed < 60
                print(f"Car{self.name} has speed {self.speed}")
            else:
        print(f"Car {self.name} has exceeded speed limit of 60 km/h!!!"
              f"Your speed is {self.speed}. Reduce speed!")
        except ValueError as k:
        print(k)

class WopkCar(Car):
    def show.speed(self):
    try:
        self.speed = int(self.speed)
        if self.speed < 40
            print (f"Car {self.name has execeeded speed limit of 40 km/h}")
            f"Your speed is {self.speed}. Reduse speed")
    except VallueError as k:
        print(k)

class PoliseCar(Car:
    is_police = True

    def chase (self):
       print(f"Police car {self.name} is chasing {SportCar}")

rider = SportCar()
kia = Workcar()
robocar_Poly = PoliceCar()
skoda = TownCar()
ridder.show_speed()
robocar_Poly.chase()
print(robocar_Poly_is_pollise)
skoda.show_speed()
print(skoda.color)
kia.go()
kia.turn("left")
kia.show_speed()
kia.stop()

#5
class Stationery:
    def_init_(self):
    self.title = input("Type title of stationery item:")

    def draw(self):
        return f"Запуск отрисовки с помощью {self.title}"

class Pen(Stayionery):
    pentype = "ball pen"

    def draw(self):
        return f"This pensil {self.title} is perfect for hatching"

class Handle(Stationery):
    def draw(self):
        return f"{self.title} is highligting important point in the text"

Parker = Pen()
print(Parker.draw())
print(Parker.pen_type)
Silverhof = Pensil
print(Silverhof.draw)
LightMark = Handle()
print(LightMark.draw)