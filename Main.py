#Copyright 2019 Xiang Li xiangl18@bu.edu

import InputModule_lxc
from StorageModule import Storage
from AiModule import AiModule
import AlertModule
import UserInterfaceModule


def main():
#   Input Module   
    pathbo = './example/examplebo.txt'
    pathbp = './example/examplebp.txt'
    pathpul = './example/examplepul.txt'
    bo = InputModule_lxc.input(pathbo)
    bp = InputModule_lxc.input(pathbp)
    pul = InputModule_lxc.input(pathpul)
    
#   Storage Module  
    for b1, b2, p1 in zip(bo, bp, pul):
        Storage(b1, b2, p1)
    
#   AI Module       
    ai = AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()
    
#   Alert Module, 0-blood oxygen, 1-blood pressure, 2-pulse
    alt = AlertModule.Alert()
    for k in range(len(bo)):
        boi = bo[k], 0
        bpi = bp[k], 1
        puli = pul[k], 2
        dic = {0: 'Blood Oxygen', 1: 'Blood Pressure', 2: 'Pulse'}
        alt.Alert_for_three_categories_input(boi)
        alt.Alert_for_three_categories_input(bpi)
        alt.Alert_for_three_categories_input(puli)
        alert = alt.Alert_Output()
        if alert != -1:
            print("Alert", dic[alert])
        else:
            print("All good.")
        
#   User Interface Module         
    UserInterfaceModule.Userinterface_Input(bo, bp, pul, predBloodOxygen, predBloodPressure, prePulse)
    UserInterfaceModule.Userinterface_Output(bo, bp, pul, predBloodOxygen, predBloodPressure, prePulse)


if __name__ == '__main__':
    main()
