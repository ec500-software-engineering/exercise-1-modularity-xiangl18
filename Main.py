import InputModule_lxc
from Storage import Storage
from AiModule import AiModule
import Alert_module
import UserInterface_module


def main():
    pathbo = './examplebo.txt'
    pathbp = './examplebp.txt'
    pathpul = './examplepul.txt'
    bo = InputModule_lxc.input(pathbo)
    bp = InputModule_lxc.input(pathbp)
    pul = InputModule_lxc.input(pathpul)
    Storage(bo, bp, pul)
    s, j, k = Storage.read()
    print(s, j, k)


    ai = AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()
    alt = Alert_module.Alert()
    for k in range(len(bo)):
        boi = bo[k], 0
        bpi = bp[k], 1
        puli = pul[k], 2
        alt.Alert_for_three_categories_input(boi)
        alt.Alert_for_three_categories_input(bpi)
        alt.Alert_for_three_categories_input(puli)
    UserInterface_module.userinterface_input(bo, bp, pul, predBloodOxygen, predBloodPressure, prePulse)
    UserInterface_module.userinterface_output(bo, bp, pul, predBloodOxygen, predBloodPressure, prePulse)


if __name__ == '__main__':
    main()
