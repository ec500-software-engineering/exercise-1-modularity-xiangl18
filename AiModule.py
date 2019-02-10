import random


class AiModule():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pulse = []

    def input_check(self, bloodOxygen, bloodPressure, pulse):
        """
        check the input type from the database in case there are some mistake data.
        """
        try:
            while True:
                if (type(bloodOxygen) != float) or (type(bloodPressure) != float) or (type(pulse) != float):
                    raise AttributeError
                else:
                    self.bo.extend(bloodOxygen)
                    self.bp.extend(bloodPressure)
                    self.pulse.extend(pulse)
                break

        except AttributeError:
            print('input type false')

    def predict(self):
        """
        predict blood oxygen, blood pressure, pulse for each type from database.
        format:
        	(float value)
        """
        rand = random.randint(1, len(self.bo))
        predBloodOxygen = 0
        predBloodPressure = 0
        prePulse = 0
        for i in range(rand):
            predBloodOxygen += self.bo[i]/rand
            predBloodPressure += self.bp[i]/rand
            prePulse += self.pulse[i]/rand
        return predBloodOxygen, predBloodPressure, prePulse
