import psutil
class Control:
    def __init__(self):
        self.battery = psutil.sensors_battery()
    def battery_percentage(self):
        print(self.battery.percent)
    
    def advice(self):
        if(self.battery.percent <= 25):
            if(self.battery.power_plugged != True):
                print("please plugged it")
    
    def temperature(self):
        print(psutil.sensors_temperatures())

c = Control()
c.battery_percentage()
c.advice()
c.temperature()