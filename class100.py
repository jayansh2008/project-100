class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.company=company
        self.model=model
        self.speed_limit=speed_limit
     
    def start(self):
        print("started")

    def stop(self):
        print("stop")


    def acceletrate(self):
        print("accelerating")


    def changegear(self,gear_type):
        print("gear changed")

Oddi = Car ("A6","cyan","Oddi","1000")
print(Oddi.changegear(4))