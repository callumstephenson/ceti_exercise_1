from classes.chemical import *
from classes.stream import *
from functions.mixer import *
from functions.reactor import *
from functions.separator import *


def plant(n, large_reactor, T):
    'returns streams at steady state'
    # chemical("name", carbon n, hydrogen n, oxygen n, moles)
    water = chemical("Water", 0, 2, 1)
    co = chemical("Castor Oil", 19, 36, 3)
    aco = chemical("Acetylated Castor Oil", 21, 38, 4)
    dco = chemical("Dehydrated Castor Oil", 19, 34, 2)
    aa = chemical("Acetic Acid", 2, 4, 2)
    gum = chemical("Gum", 38, 68, 4)

    # stream(number, mass_flow, mol_flow, co_frac, aco_frac, dco_frac, aa_frac, water_frac, gum_frac) 
    stream_12 = stream(12, 0, 0, 0, 0, 0, 0, 0)
    stream_8 = stream(8, 0, 0, 0, 0, 0, 0, 0)

    # plant
    i = 0
    temperature = T

    while i <= n:
        stream_1 = stream(1, 5920 - stream_8.co_molflow, 1, 0, 0, 0, 0, 0)
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
        stream_12 = stream(12, 0, 0, 0, 0, 0, 0, 0)
        stream_8 = stream(8, 0, 0, 0, 0, 0, 0, 0)
        # reactor 1
        stream_4 = reactor1(stream_3)
        # reactor 2
        stream_5 = reactor2(stream_4, temperature, large_reactor)
        # filter
        stream_7 = filter(stream_5, stream_6)
        # column 1
        column1(stream_7, stream_9, stream_8)
        # column 2 
        column2(stream_9, stream_11, stream_10)
        # acid separator
        acid_separator(stream_11, stream_12, stream_13)
        i += 1
    return stream_1, stream_2, stream_3, stream_4, stream_5, stream_6, stream_7, stream_8, stream_9, stream_10, stream_11, stream_12, stream_13, temperature
