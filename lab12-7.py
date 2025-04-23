class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

weather = Weather(["temperature", "humidity", "wind", "pressure"])
print("temperature" in weather)  
print("rainfall" in weather)    