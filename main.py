from classes.chemical import *
from classes.stream import *
from functions.mixer import *
from functions.opex import *
from functions.reactor import *
from functions.separator import *
from functions.mixer import *
import copy

# data / physical values

# USD / KG
aa_cost = 0.9
co_cost = 1.2
dco_cost = 2

# USD / HR
labour = 250

#operating hours
hours_pa = 8000

# chemical definitions

# chemical("name", carbon n, hydrogen n, oxygen n, moles)
water = chemical("Water", 0, 2, 1)
co = chemical("Caster Oil", 19, 36, 3)
aco = chemical("Acetylated Castor Oil", 21, 38, 4)
dco = chemical("Dehydrated Castor Oil", 19, 34, 2)
aa = chemical("Acetic Acid", 4, 4, 2)
gum = chemical("Gum", 38, 68, 4)

# stream definitions
# stream(number, mass_flow, mol_flow, co_frac, aco_frac, dco_frac, aa_frac, water_frac, gum_frac) 
x = int(1600) # initial flowrate...
stream_1 = stream(1, 5035, 1, 0, 0, 0, 0, 0)
stream_2 = stream(2, 7553, 0, 0, 0, 1, 0, 0)
stream_12 = stream(12, 0, 0, 0, 0, 0, 0, 0)
stream_8 = stream(8, 0, 0, 0, 0, 0, 0, 0)

# plant
n = 1000
i = 0

while i <= n:
    stream2_req = ((stream_8.co_molflow+stream_1.mol_flow)*1.5) - stream_12.aa_molflow
    stream_2 = stream(2, stream2_req, 0, 0, 0, 1, 0, 0)
    stream_3 = stream(3, 0, 0, 0, 0, 0, 0, 0)
    stream_4 = stream(4, 0, 0, 0, 0, 0, 0, 0)
    stream_5 = stream(5, 0, 0, 0, 0, 0, 0, 0)
    stream_6 = stream(6, 0, 0, 0, 0, 0, 0, 0)
    stream_7 = stream(7, 0, 0, 0, 0, 0, 0, 0)
    stream_9 = stream(9, 0, 0, 0, 0, 0, 0, 0)
    stream_10 = stream(10, 0, 0, 0, 0, 0, 0, 0)
    stream_11 = stream(11, 0, 0, 0, 0, 0, 0, 0)
    stream_13 = stream(13, 0, 0, 0, 0, 0, 0, 0)
    # mix
    mixer(stream_1, stream_2, stream_8, stream_12, stream_3)
    stream3_after = copy.deepcopy(stream_3.mol_flow)
    stream_12 = stream(12, 0, 0, 0, 0, 0, 0, 0)
    stream_8 = stream(8, 0, 0, 0, 0, 0, 0, 0)
    # reactor 1
    stream_4 = reactor1(stream_3)
    # reactor 2
    stream_5 = reactor2(stream_4, 300, True)
    # filter
    stream_7 = filter(stream_5, stream_6, gum)
    # column 1
    column1(stream_7, stream_9, stream_8, aa, co, dco, aco, water)
    # column 2 
    column2(stream_9, stream_11, stream_10, aa, water)
    # acid separator
    acid_separator(stream_11, stream_12, stream_13, aa, water)
    i += 1

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
print("$", hours_pa * total_hourly_operating, " per year to operate")

# total material cost/profit
feed_cost = (aa_cost * stream_2.mol_flow * aa.mr_kg) + (co_cost * stream_1.mol_flow * co.mr_kg)
product = stream_10.dco_molflow * dco.mr_kg * dco_cost
material_hour = product - feed_cost
material_year = material_hour * hours_pa

# total operating profit
yearly_profit = material_year - total_yearly_operating
print("Total yearly profit is $", yearly_profit)
dco_pa_ton = int(stream_10.dco_molflow * dco.mr_kg * 8)
print(dco_pa_ton)