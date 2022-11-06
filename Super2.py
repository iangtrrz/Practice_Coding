class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

class Freelance(Emp):
    def __init__(self, id, name, Add, Email):
        super().__init__(id, name, Add)
        self.Email = Email

Emp_1 = Freelance(100217, "Adrian", "San Jose", "Iangtrrz02@gmail.com")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is', Emp_1.Add)
print('The Emails is:', Emp_1.Email)