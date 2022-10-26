from classes.chemical import *
from classes.stream import *

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
stream_1 = stream(1, 0, 0, 1, 0, 0, 0, 0, 0)
stream_2 = stream(2, 0, 0, 0, 0, 0, 1, 0, 0)
stream_3 = stream(3)
stream_4 = stream(4)
stream_5 = stream(5)
stream_6 = stream(6, 0, 0, 0, 0, 0, 0, 0, 1)
stream_7 = stream(7)
stream_8 = stream(8)
stream_9 = stream(9)
stream_10 = stream(10)
stream_11 = stream(11)
stream_12 = stream(12, 0, 0, 0, 0, 0, 0.99, 0.01, 0)
stream_13 = stream(13, 0, 0, 0, 0, 0, 0.08, 0.92, 0)
