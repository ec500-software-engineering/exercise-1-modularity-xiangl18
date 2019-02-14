import InputModule
import StorageModule
import AlertModule
import UserInterfaceModule
import AiModule
import queue
# import threading


def main():
    q1 = queue.Queue()
    q2 = queue.Queue()
    q3 = queue.Queue()
    ipt = InputModule.InputModule(q1)
    # input_event = threading.Event()
    # input_event.set()
    storage = StorageModule.Storage(q1)
    storage.getIput("bo")
    alert = AlertModule.Alert(q1, q2)
    ai = AiModule.AIModule(q1, q3)
    ui = UserInterfaceModule.UserInterface(q1, q2, q3)
    ipt.start()
    storage.start()
    alert.start()
    ai.start()
    ui.start()
    ipt.join()
    storage.join()
    alert.join()
    ai.join()
    ui.join()


if __name__ == '__main__':
    main()
