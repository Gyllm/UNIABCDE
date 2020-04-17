from empregado import Employee

class Teacher(Employee):
    def __init__(self,name,phone,email,salary,start_date,course):
        super().__init__(name,phone,email,salary,start_date)
        self.course = course

    def additional_health_hazard(self):
        if self.course == 'Engenharia':
            return {
                'name': self.name,
                'course': self.course,
                'adicional': self.salary * (0.3)
                }
        elif self.course == 'Direito':
            return {
                'name': self.name,
                'course': self.course,
                'adicional': self.salary * (0.05)
                }
        else:
            return {
                'name': self.name,
                'course': self.course,
                'adicional': self.salary * (0.15)
                }

    def show_info(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'salary': self.salary,
            'start_date': self.start_date,
            'course': self.course
            }