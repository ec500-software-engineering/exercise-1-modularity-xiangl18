class InputModule():
    def read(self,path):
        try:
            with open(path,'r') as f:
                data = f.readline().split()
                if data:
                    time = data[0]
                    value = data[1]
                    print("Read data successfully\n")
                else:
                    print("Empty data file!\n")
                    return 2

            return time,value
        except:
            print("Error:No input data\n")
