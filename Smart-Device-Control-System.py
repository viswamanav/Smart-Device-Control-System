class Device:
    def __init__(self):
        self._is_on = False
    def start(self):
        pass
    def stop(self):
        pass
    def get_status(self):
        return self._is_on
class Motor(Device):
    def start(self):
        if not self._is_on:
            self._is_on = True
            print("fan has started")
        else:
            print("Motor is already running")
    def stop(self):
        if self._is_on:
            self._is_on = False
            print("Motor has stopped")
        else:
            print("Motor is already stopped")
class Light(Device):
    def start(self):
        if not self._is_on:
            self._is_on = True
            print("Light switched on")
        else:
            print("Light is already ON")
    def stop(self):
        if self._is_on:
            self._is_on = False
            print("Light switched off")
        else:
            print("Light is already OFF")
class Controller:
    def operate1(self, device):
        device.start()
    def operate2(self, device):
        device.stop()


motor = Motor()
light = Light()

controller = Controller()

controller.operate1(motor)
controller.operate2(light)
controller.operate1(light)
controller.operate2(motor)


print("\nChecking Status:")
print("Motor ON:", motor.get_status())
print("Light ON:", light.get_status())