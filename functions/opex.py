from classes.chemical import *
from classes.stream import *


# chemical("name", carbon n, hydrogen n, oxygen n, moles)
water = chemical("Water", 0, 2, 1)
co = chemical("Caster Oil", 19, 36, 3)
aco = chemical("Acetylated Castor Oil", 21, 38, 4)
dco = chemical("Dehydrated Castor Oil", 19, 34, 2)
aa = chemical("Acetic Acid", 4, 4, 2)
gum = chemical("Gum", 38, 68, 4)

# data / physical values

# USD / KG
aa_cost = 0.9
co_cost = 1.2
dco_cost = 2

# USD / HR
labour = 250

#operating hours
hours_pa = 8000

def reactor_cost(in_stream_flowrate, temperature):
    '''
    reactor operating cost per hour in USD.
    input arguments: in_stream_flowrate (kg / hr), temperature (deg C) 
    return: operating cost in USD per hour
    '''
    if in_stream_flowrate < 0 or temperature < -273.15:
        raise Exception("invalid input args")
    return ( in_stream_flowrate * (temperature - 20) ) / 10000

def column_cost(in_stream_flowrate, column_number = 0):
    '''
    column operating cost per hour in USD
    input arguments: in_stream_flowrate (kg / hr)
    return: column operating cost in USD per hour
    '''
    column_factor = [25, 100]
    if in_stream_flowrate < 0:
        raise Exception("invalid input args")
    return in_stream_flowrate / column_factor[column_number]

def acid_sep_cost(in_stream_flowrate):
    ''' returns the cost of running the acid separator
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate*0.15

def filter_cost(in_stream_flowrate):
    ''' returns the cost of running the filter
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate*40

def recycle_cost(in_stream_flowrate):
    ''' returns the cost of running the recycle
    inputs: in_stream_flowrate kg / hr
    outputs: cost per hour in USD '''
    return in_stream_flowrate / 10000

def yearly_finance(stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13):
    'returns profit, operating, material, dca tonnage'
    #calculate mass flow rates and opex
    # aa, co, aco, dco, water
    stream3_massflow = (stream_3.aa_molflow * aa.mr_kg) + (stream_3.co_molflow * co.mr_kg ) + (stream_3.aco_molflow * aco.mr_kg) + (stream_3.dco_molflow * dco.mr_kg) + (stream_3.water_molflow * water.mr_kg)
    stream7_massflow = (stream_7.aa_molflow * aa.mr_kg) + (stream_7.co_molflow * co.mr_kg ) + (stream_7.aco_molflow * aco.mr_kg) + (stream_7.dco_molflow * dco.mr_kg) + (stream_7.water_molflow * water.mr_kg)
    stream9_massflow = (stream_9.aa_molflow * aa.mr_kg) + (stream_9.co_molflow * co.mr_kg ) + (stream_9.aco_molflow * aco.mr_kg) + (stream_9.dco_molflow * dco.mr_kg) + (stream_9.water_molflow * water.mr_kg)
    stream11_massflow = (stream_11.aa_molflow * aa.mr_kg) + (stream_11.co_molflow * co.mr_kg ) + (stream_11.aco_molflow * aco.mr_kg) + (stream_11.dco_molflow * dco.mr_kg) + (stream_11.water_molflow * water.mr_kg)
    stream6_massflow = (stream_6.aa_molflow * aa.mr_kg) + (stream_6.co_molflow * co.mr_kg ) + (stream_6.aco_molflow * aco.mr_kg) + (stream_6.dco_molflow * dco.mr_kg) + (stream_6.water_molflow * water.mr_kg)
    stream8_massflow = (stream_8.aa_molflow * aa.mr_kg) + (stream_8.co_molflow * co.mr_kg ) + (stream_8.aco_molflow * aco.mr_kg) + (stream_8.dco_molflow * dco.mr_kg) + (stream_8.water_molflow * water.mr_kg)
    stream12_massflow = (stream_12.aa_molflow * aa.mr_kg) + (stream_12.co_molflow * co.mr_kg ) + (stream_12.aco_molflow * aco.mr_kg) + (stream_12.dco_molflow * dco.mr_kg) + (stream_12.water_molflow * water.mr_kg)
    reactors_per_hour = reactor_cost(stream3_massflow, 300)
    columns_per_hour = column_cost(stream7_massflow, 0) + column_cost(stream9_massflow, 1)
    acid_sep_per_hour = acid_sep_cost(stream11_massflow)
    filter_per_hour = filter_cost(stream6_massflow)
    recyclers_per_hour = recycle_cost(stream8_massflow) + recycle_cost(stream12_massflow)
    total_hourly_operating = reactors_per_hour + columns_per_hour + acid_sep_per_hour + filter_per_hour + recyclers_per_hour + labour
    total_yearly_operating = hours_pa * total_hourly_operating

    # total material cost/profit
    feed_cost = (aa_cost * stream_2.mol_flow * aa.mr_kg) + (co_cost * stream_1.mol_flow * co.mr_kg)
    product = stream_10.dco_molflow * dco.mr_kg * dco_cost
    material_hour = product - feed_cost
    material_year = material_hour * hours_pa

    # total operating profit
    yearly_profit = material_year - total_yearly_operating
    dco_pa_ton = int(stream_10.dco_molflow * dco.mr_kg * 8)
    return yearly_profit, total_yearly_operating, material_year, dco_pa_ton