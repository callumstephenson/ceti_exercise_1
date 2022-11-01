# reactors


def reactor1(in_stream):
    'returns the out_stream composition and flowrate given a well defined in_stream'
    conversion = 0.9
    if in_stream.aa_molflow >= 1.5 * in_stream.co_molflow:
        aco_delta_r1 = in_stream.co_molflow * conversion
        water_delta_r1 = aco_delta_r1
        aa_delta_r1 = -1 * aco_delta_r1
        co_delta_r1 = -1 * aco_delta_r1
        # for every mole reacted, 1 mole is produced so moles are conserved over this reaction vessel.
        # update(new_massflow, new_molflow, co_delta, aco_delta, dco_delta, aa_delta, water_delta, gum_delta)
        in_stream.update(new_molflow = in_stream.mol_flow, co_delta = co_delta_r1, aco_delta = aco_delta_r1, aa_delta = aa_delta_r1,  water_delta = water_delta_r1)
    else:
        raise Exception("AA not in 0.5 excess")
    return in_stream

def reactor2(in_stream, temperature, large_reactor):
    'returns out_stream composition and flowrate given a temperature and reactor size'
    temp_condition_dict_small = {
         250 : [0.107, 1.43*10**8],
         260 : [0.161, 9.51*10**6],
         270 : [0.218, 1.68*10**6],
         280 : [0.283, 3.87*10**5],
         290 : [0.345, 1.09*10**5],
         300 : [0.413, 3.58*10**4],
         310 : [0.475, 1.21*10**4],
         320 : [0.528, 4.15*10**3],
         330 : [0.574, 1.6*10**3],
    }

    temp_condition_dict_large = {
        250 : [0.184, 2.49*10**6],
        260 : [0.245, 4.59*10**5],
        270 : [0.314, 1.19*10**5],
        280 : [0.375, 3.54*10**4],
        290 : [0.444, 1.15*10**4],
        300 : [0.513, 4.28*10**3],
        310 : [0.559, 1.69*10**3],
        320 : [0.597, 7.15*10**2],
        330 : [0.635, 2.79*10**2]
    }
    if large_reactor:
        conversion = temp_condition_dict_large[temperature][0]
        selectivity = temp_condition_dict_large[temperature][1]
    else:
        conversion = temp_condition_dict_small[temperature][0]
        selectivity = temp_condition_dict_small[temperature][1]
    #reaction 
    aco_delta_r2 = -1 * (in_stream.aco_molflow * conversion) # aco decreases by conversion
    dco_made = -1 * aco_delta_r2 # dco made = aco used
    aa_delta_r2 = dco_made # 1 mol aa made per dco made, not used in side reaction
    dco_delta_r2 = (selectivity * dco_made) / (selectivity + 2) # simultaneous eqs
    gum_delta_r2 = (2 * dco_made) / (selectivity + 2) # per definition
    mol_flow_r2 = in_stream.mol_flow + aco_delta_r2 + aa_delta_r2 + dco_delta_r2 + gum_delta_r2
    in_stream.update(new_molflow = mol_flow_r2 , aco_delta = aco_delta_r2, aa_delta = aa_delta_r2, dco_delta = dco_delta_r2, gum_delta = gum_delta_r2)
    return in_stream