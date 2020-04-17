from pessoa import Person

class Student(Person):
    def __init__(self,name,phone,email,ar,course):
        super().__init__(name,phone,email)
        self.ar = ar
        self.course = course

    def monthtly_payment(self):
        if self.course == 'Engenharia':
            return {
                'name': self.name,
                'course': self.course,
                'mensalidade': 'R$ 2000,00'
                }
        elif self.course == 'Direito':
            return {
                'name': self.name,
                'course': self.course,
                'mensalidade': 'R$ 1500,00'
                }
        else:
            return {
                'name': self.name,
                'course': self.course,
                'mensalidade': 'R$ 550,00'
                }

    def show_info(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'ar': self.ar,
            'course': self.course
            }