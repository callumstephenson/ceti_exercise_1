from functions.opex import *
from functions.plant import *


def run():
    'returns master list of all running conditions / profit, and prints the most optimum'
    master_list = []
    for i in range(250, 340, 10):
        true_index = [True, False]
        for j in range(0, 2):
            stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13, temperature = plant(1000, true_index[j], i)
            # arr of [(profit, operating, materials, dca_tonnage), large_reactor, t]
            master_list.append((yearly_finance(stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13, temperature), true_index[j], i, int(stream_1.mol_flow), int(stream_2.mol_flow)))
    profit = []
    dca_tonnage = []
    for i in range(0, len(master_list)):
        profit.append(master_list[i][0][0])
        dca_tonnage.append(master_list[i][0][3])
    best_cond_index = profit.index(max(profit))
    print("Best conditions for operation are: \n", 
        "Profit =", master_list[best_cond_index][0][0], "USD$ / year \n",
        "Large reactor =", master_list[best_cond_index][1], "\n",
        "Temperature =", master_list[best_cond_index][2], " *C\n",
        "CO Molflow =", master_list[best_cond_index][3], "mol / hour \n",
        "AA Molflow =", master_list[best_cond_index][4], "mol / hour \n",
        "DCA tonnage =", master_list[best_cond_index][0][3], "ton / year \n",
        )
    stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13, temperature = plant(1000, master_list[best_cond_index][1], master_list[best_cond_index][2])
    stream_1.massflow(), stream_2.massflow(), stream_3.massflow(), stream_4.massflow(), stream_5.massflow(), stream_6.massflow(), stream_7.massflow(), stream_8.massflow(), stream_9.massflow(), stream_10.massflow(), stream_11.massflow(), stream_12.massflow(), stream_13.massflow()
    return None

if __name__ == "__main__":
    print("CASTOR OIL PLANT SIM")
    run()
