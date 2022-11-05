from functions.opex import *
from functions.plant import *

def run():
    'returns a list of tuples of form [profit, operating, material, dca tonnage'
    cost_list = []
    for i in range(250, 340, 10):
        true_index = [True, False]
        for j in range(0, 2):
            stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13 = plant(5000, 1000, true_index[j], i)
            cost_list.append(yearly_finance(stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13))
    return cost_list

if __name__ == "__main__":
    print("CASTOR OIL PLANT SIM")
    cost_list = run()
    print(cost_list)