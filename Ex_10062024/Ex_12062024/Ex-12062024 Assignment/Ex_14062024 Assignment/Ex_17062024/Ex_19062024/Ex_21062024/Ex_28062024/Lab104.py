class car:
    name = None
    make = None
    model = None


    def __init__(self, o_name, o_make, o_model):
                self.name = o_name
                self.make = o_make
                self.model = o_model


    def start_engine(self):
                 print("starting a car with name" + self.name)
                 print("starting a car with make" + self.make)
                 print("starting a car with model" + self.model)


lambo = car("lambo", "v6",  "2024")
lambo.start_engine()
XUV = car("XUV","v4","2023")
XUV.start_engine()

