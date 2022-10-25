# This module provides the stream class for the calculations

class stream:
    'A class for the stream object, containing mass flowrate, molar flowrate, and molar fractions of each chemical'

    def __init__(self, stream_number, mass_flow, mol_flow, co_frac, aco_frac, dco_frac, aa_frac, water_frac, gum_frac):
        'stream class initialisation with each of the corresponding input arguments being set to self.'

        self.stream_number = stream_number
        self.mass_flow = mass_flow
        self.mol_flow = mol_flow


        if round(co_frac + aco_frac + dco_frac + aa_frac + water_frac + gum_frac, 1) == 1:

            self.valid = True
            self.co_frac = co_frac
            self.aco_frac = aco_frac
            self.dco_frac = dco_frac
            self.aa_frac = aa_frac
            self.water_frac = water_frac
            self.gum_frac = gum_frac

        else:
            
            self.valid = False
            raise Exception("Value Error, sum of mole fractions greater than 1. Incomplete class creation")

    def __repr__(self):

        'Self print statement for the stream object'
        if self.valid:
            d = "Stream Number:     {}\n".format(self.stream_number)
            d += "   Mass Flowrate (kg/hr):     {}\n".format(self.mass_flow)
            d += "   Molar Flowrate (kmol/hr):      {}\n".format(self.mol_flow)
            d += "   CO Mole Fraction    {}\n".format(self.co_frac)
            d += "   ACO Mole Fraction:    {}\n".format(self.aco_frac)
            d += "   DCO Mole Fraction:          {}\n".format(self.dco_frac)
            d += "   AA Mole Fraction:         {}\n".format(self.aa_frac)
            d += "   Water Mole Fraction: {}".format(self.water_frac)
            d += "   Gum Mole Fraction:  {}".format(self.gum_frac)
            return d