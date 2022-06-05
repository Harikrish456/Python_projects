class Car(object):
   def __init__(self,color, model, company, speedlimit, horsepower):
       self.color = color
       self.model = model
       self.company = company
       self.speedlimit = speedlimit
       self.horsepower = horsepower

   def start(self):
        print('Car started')

   def accelerate(self):
       print('Car accelerated! Its going vroom now!')

   def stop(self):
       print('Your journey has come to a halt')

   def changeGear(self, value):
       print('Switched gear to', value)

car = Car('blue', 'Ertiga', 'Suzuki', 250, 500)       
car.start()
car.changeGear(3)
car.accelerate()
car.stop()

print(car.model)
print(car.speedlimit)
print(car.color)
print(car.company)
print(car.horsepower)