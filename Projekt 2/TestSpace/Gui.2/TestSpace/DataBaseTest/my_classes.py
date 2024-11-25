class ThreeDPrinting:
    def __init__(self, material_id: str, machine: str, process: str, cost: float, unit: str, density: str):
        self.material_id = material_id
        self.machine = machine
        self.process = process
        self.cost = cost
        self.unit = unit
        self.density = density
    
    def validate_cost(self, cost):
        try:
            return float(cost)
        except ValueError:
            raise ValueError("Cost must be a decimal number.")
        
    def __str__(self):
        return f"{self.material_id} is a {self.process} material that costs {self.cost} per {self.unit} and has a density of {self.density} g/cm^3, created in a {self.machine} machine."
    
class Worker:
    def __init__(self, process:str, job_title:str, salary:float):
        self.process = process
        self.job_title = job_title
        self.salary = salary
    
    def validate_salary(self):
        try:
            return float(self.salary)
        except ValueError:
            raise "Salary must be an integer."
    
    def __str__(self):
        return f"{self.job_title.capitalize()}'s working in {self.process} process earn {self.salary}$ per hour."