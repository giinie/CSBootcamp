class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before:', r0.get_ohms())
r0.set_ohms(10e3)
print('After:', r0.get_ohms())
print('-' * 50)

r0.set_ohms(r0.get_ohms() + 5e3)
print(r0.get_ohms())
print('-' * 50)


class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
print('Before:', r1.ohms)
r1.ohms = 10e3
print('After: {} ohms, {} volts, {} amps'.format(r1.ohms, r1.voltage, r1.current))
print(r1.ohms + 5e3)
print('-' * 50)


class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print('Before: {} amps'.format(r2.current))
r2.voltage = 10
print('After: {} amps'.format(r2.current))
print('-' * 50)


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('{:f} ohms must be > 0'.format(ohms))
        self._ohms = ohms


# r3 = BoundedResistance(1e3)
# r3.ohms = 0
# BoundedResistance(-5)

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super(FixedResistance, self).__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
# r4.ohms = 2e3
print('-' * 50)


class MysteriousResister(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


r7 = MysteriousResister(10)
r7.current = 0.01
print('Before:', r7.voltage)
print(r7.ohms)
print('After:', r7.voltage)
print('-' * 50)

