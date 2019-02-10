import InputModule
import StorageModule
import AiModule
import AlertModule
import UserInterfaceModule


def main():
    path = '/'
    time = []
    valuse = []
    time, value = InputModule.InputModule.read(path)
    bo = value[0][1]
    bp = value[0][2]
    pul = value[0][3]

    with (StorageModule.storage) as storage:
        storage.__init__(bo, bp, pul)
        storage.read()

    AlertModule.Alert_for_three_categories_input(value)
    AlertModule.Alert_Output()
    ai = AiModule.AiModule()
    ai.input_check(bo, bp, pul)
    predBloodOxygen, predBloodPressure, prePulse = ai.predict()
    UserInterfaceModule.Userinterface_Input(predBloodOxygen, predBloodPressure, prePulse)


if __name__ == '__main__':
    main()
