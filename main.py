from xml.dom.expatbuilder import parseString
from classes.chemical import *
from classes.stream import *

# chemical definitions
# chemical("name", carbon n, hydrogen n, oxygen n)
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