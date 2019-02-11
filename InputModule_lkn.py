# URL: https://github.com/WenjieLuo2333/ModuleDesign/blob/master/Input_Module_lkn.py
# Copyright 2019 Kainan Liu liuknan@bu.edu
# Input Module

def read_data(path):
    time = []
    value = []
    try:
        with open(path,'r') as f:
            data = f.readline()
            if data:
                for i in data:
                    i = i.split()
                    for item in i:
                        value.append(float(item))
                print("Read data successfully\n")
                return value
            else:
                print("Empty data file!\n")
                return 2
    except:
        print("Error:No input data\n")
