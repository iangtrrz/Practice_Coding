class Owner:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Business(Owner):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.establishedyear = year

x = Business("Adrian", "Gutierrez", 2019)
print(x.establishedyear)
