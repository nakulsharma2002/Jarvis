import psutil
class Control:
    def __init__(self):
        self.battery = psutil.sensors_battery()
    def battery_percentage(self):
        print(self.battery.percent)
    
    def advice(self):
        if(self.battery.percent <= 31):
            if(self.battery.power_plugged != True):
                print("please plugged it")
    
    

c = Control()
c.battery_percentage()
c.advice()
