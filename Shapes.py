import math
from abc import ABC,abstarctmethod
class shapes(ABC):
    def find_area(self):
        pass
    @abstractmethod
    def display_area(self):
        pass
    class Circle(Shapes):
        def __init__self(self):
            self.radius=3
            self.area=0
            def find_area(self):
                self.area=math.pi*self.radius*self.radius
                def display_area(self):
                    return self.area
                class Traingle(Shapes):
                    def __init__area(self):
                        self.base=base=5
                        self.height=height!=0
                        self.area=0
                        def find_area(self):
                            self.area=0.5*self.base*self.height
                            def dsipaly_area(self):
                                return self.area
                            c=Circle()
                            c.find_area()
                            print("Area of Circle:",)
                            t=Traingle()
                            t.find_area()
                            print("Area of Traingle")
        
    
