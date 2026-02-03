# Duck typing
class Pycharm:
    def execute(self):
        print("Code compiling")
        print("Code Running")

class MyEditor:
    def execute(self):
        print("Spells check")
        print("Convention check")
        print("Code compiling")
        print("Code Running")

class Laptop:
    def code(self,ide):
        ide.execute()




# py1=Pycharm()
myed=MyEditor()

lap1=Laptop()
lap1.code(myed)