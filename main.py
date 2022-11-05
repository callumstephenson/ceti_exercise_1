from functions.opex import *
from functions.plant import *

def run():
    'returns a list of tuples of form [profit, operating, material, dca tonnage'
    master_list = []
    for i in range(250, 340, 10):
        true_index = [True, False]
        for j in range(0, 2):
            stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13 = plant(1000, true_index[j], i)
            # [(profit, operating, materials, dca_tonnage), large_reactor, t]
            master_list.append((yearly_finance(stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13), true_index[j], i))
    profit = []
    dca_tonnage = []
    for i in range(0, len(master_list)):
        profit.append(master_list[i][0][0])
        dca_tonnage.append(master_list[i][0][3])
    best_cond_index = profit.index(max(profit))
    print(master_list[best_cond_index])
    return None
if __name__ == "__main__":
    print("CASTOR OIL PLANT SIM")
    run()