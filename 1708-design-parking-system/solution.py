class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.bCap = big
        self.mCap = medium
        self.sCap = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.bCap > 0:
            self.bCap -= 1
            return True
        elif carType == 2 and self.mCap > 0:
            self.mCap -= 1
            return True
        elif carType == 3 and self.sCap > 0:
            self.sCap -= 1
            return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
