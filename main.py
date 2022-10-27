from classes.chemical import *
from classes.stream import *
from functions.mixer import *
from functions.opex import *
from functions.reactor import *
from functions.separator import *

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
stream_1 = stream(1, 0, 0, 1, 0, 0, 0, 0, 0)
stream_2 = stream(2, 0, 0, 0, 0, 0, 1, 0, 0)
stream_3 = stream(3, 0, 0, 0, 0, 0, 0, 0, 0)
stream_4 = stream(4, 0, 0, 0, 0, 0, 0, 0, 0)
stream_5 = stream(5, 0, 0, 0, 0, 0, 0, 0, 0)
stream_6 = stream(6, 0, 0, 0, 0, 0, 0, 0, 1)
stream_7 = stream(7, 0, 0, 0, 0, 0, 0, 0, 0)
stream_8 = stream(8, 0, 0, 0, 0, 0, 0, 0, 0)
stream_9 = stream(9, 0, 0, 0, 0, 0, 0, 0, 0)
stream_10 = stream(10, 0, 0, 0, 0, 0, 0, 0)
stream_11 = stream(11, 0, 0, 0, 0, 0, 0, 0)
stream_12 = stream(12, 0, 0, 0, 0, 0, 0, 0, 0)
stream_13 = stream(13, 0, 0, 0, 0, 0, 0, 0, 0)

# plant linear

# total operating cost

reactors_per_hour = reactor_cost(stream_3.mass_flow, T)
columns_per_hour = column_cost(stream_7.mass_flow, 0) + column_cost(stream_9.mass_flow, 1)
acid_sep_per_hour = acid_sep_cost(stream_11.mass_flow)
filter_per_hour = filter_cost(stream_6.mass_flow)
recyclers_per_hour = recycle_cost(stream_8.mass_flow) + recycle_cost(stream_12.mass_flow)
total_hourly_operating = reactors_per_hour + columns_per_hour + acid_sep_per_hour + filter_per_hour + recyclers_per_hour + labour
total_yearly_operating = print("$" + hours_pa * total_hourly_operating + " per year to operate")

# total material cost/profit
feed_cost = (aa_cost * stream_2.mass_flow) + (co_cost * stream_1.mass_flow)
product = stream_10.dco_molflow * dco.mr_kg * dco_cost
material_hour = product - feed_cost
material_year = material_hour * hours_pa

# total operating profit
yearly_profit = material_year - total_yearly_operating