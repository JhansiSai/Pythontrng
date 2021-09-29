class Time_sheet:
    def __init__(self,date,hours,activity,status):
        self.dates=date
        self.hours=hours
        self.activity=activity
        self.status=status
    def timesheet(self):
        print("this is the my first time sheet")
    def display(self):
        print(self.dates,self.hours,self.activity)
p=Time_sheet("12/3/12,","20,","done the front end,","on going")
p.timesheet()
p.display()
