class Hokage:
    def func1(self):
        print("Strongest Ninja in Konohagakure")

class Shinobi(Hokage):
    def func2(self):
        print("Ninja of Konohagakure")

object = Shinobi()
object.func1()
object.func2()