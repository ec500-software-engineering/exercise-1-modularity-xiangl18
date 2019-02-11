# URL: https://github.com/WenjieLuo2333/ModuleDesign/blob/master/UserInterface_module.py
# Copyright 2019 Qinmei Du duqinmei@bu.edu
# User Interface Module


#copyright @Qinmei Du
#It's the I/O documentation for the User_Interface_system
#User Interface

class userInterface():
    def __init__(self):
        self.bo = []
        self.bp = []
        self.pul = []
        self.boalert = []
        self.bpalert = []
        self.pulalert = []
        self.operation = []

    def getFromAlert(self, boalert, bpalert, pulalert):
        self.boalert = boalert
        self.bpalert = bpalert
        self.pulalert = pulalert

    def getFromData(self, bo, bp, pul):
        self.bo = bo
        self.bp = bp
        self.pul = pul

    def getFromUser(self, operation):
        self.operation = operation

    def sendToShow(self):
        send_data = {
            self
        }
        print(send_data)
        return send_data
