class Animals:
    def __init__(self) :
        self.num_eye = 2

    def breathe(self):
        print("Inhale,Exhale")
    
class Fish(Animals):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("under the water")
    
    def swim(self):
        print("Moving in Water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eye)


