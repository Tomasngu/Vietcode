class Debilek:
    def __init__(self,name):
        self.name = name
    def napis(self):
        if self.name == "Emma":
            print(f"{self.name} je pouhy debilek")
        else:
            print(f"{self.name} debilek")
    
e = Debilek("Emma")
t = Debilek("Tom")
print(e.napis())


