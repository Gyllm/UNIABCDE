from pessoa import Person
import datetime

class Employee(Person):
    def __init__(self,name,phone,email,salary,start_date):
        super().__init__(name,phone,email)
        self.salary = float(salary)
        self.start_date = start_date
        
    def work_days(self):
        d2 = datetime.datetime.today()
        d1 = datetime.datetime.strptime(self.start_date,'%d-%m-%Y')
        difer = (d2-d1).days
        return {
            'name': self.name,
            'start date': self.start_date,
            'dias passados após a admissão': difer,
            }