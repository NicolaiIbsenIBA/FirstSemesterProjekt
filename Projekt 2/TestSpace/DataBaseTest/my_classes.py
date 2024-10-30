class ThreeDPrinting:
    def __init__(self, material_id:str, machine:str, process:str, cost:float, unit:str, density:str):
        self.material_id = material_id
        self.machine = machine
        self.process = process
        self.cost = cost
        self.unit = unit
        self.density = density
    
    def __str__(self):
        return f"{self.material_id} is a {self.process} material that costs {self.cost} {self.unit} per {self.density}, created in a {self.machine} machine."