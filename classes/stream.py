# This module provides the stream class for the calculations

class stream:
    'A class for the stream object, containing mass flowrate, molar flowrate, and molar fractions of each chemical'

    def __init__(self, stream_number, mol_flow, co_frac, aco_frac, dco_frac, aa_frac, water_frac, gum_frac, initialised=True):
        'stream class initialisation with each of the corresponding input arguments being set to self.'

        self.stream_number = stream_number
        self.mol_flow = mol_flow
        self.initialised = initialised

        if round(co_frac + aco_frac + dco_frac + aa_frac + water_frac + gum_frac, 1) == 1 or initialised:

            # define fractions
            self.valid = True
            self.co_frac = co_frac
            self.aco_frac = aco_frac
            self.dco_frac = dco_frac
            self.aa_frac = aa_frac
            self.water_frac = water_frac
            self.gum_frac = gum_frac

            # auto-define molar flow rate
            self.co_molflow = self.co_frac * self.mol_flow
            self.aco_molflow = self.aco_frac * self.mol_flow
            self.dco_molflow = self.dco_frac * self.mol_flow
            self.aa_molflow = self.aa_frac * self.mol_flow
            self.water_molflow = self.water_frac * self.mol_flow 
            self.gum_molflow =  self.gum_frac * self.mol_flow

        else:
            
            self.valid = False
            raise Exception("Value Error, sum of mole fractions greater than 1. Incomplete class creation")

    def __repr__(self):

        'Self print statement for the stream object'
        if self.valid:
            d = "Stream Number:     {}\n".format(self.stream_number)
            d += "   Molar Flowrate (kmol/hr):      {}\n".format(self.mol_flow)
            d += "   CO Mole Fraction    {}\n".format(self.co_frac)
            d += "   ACO Mole Fraction:    {}\n".format(self.aco_frac)
            d += "   DCO Mole Fraction:          {}\n".format(self.dco_frac)
            d += "   AA Mole Fraction:         {}\n".format(self.aa_frac)
            d += "   Water Mole Fraction: {}".format(self.water_frac)
            d += "   Gum Mole Fraction:  {}".format(self.gum_frac)
            return d

    def update(self, new_molflow, co_delta = 0, aco_delta = 0, dco_delta = 0, aa_delta = 0, water_delta = 0, gum_delta = 0):
        if new_molflow >= 0:
            # update molflows
            self.mol_flow = new_molflow
            self.co_molflow += co_delta
            self.aco_molflow += aco_delta
            self.dco_molflow += dco_delta
            self.aa_molflow += aa_delta
            self.water_molflow += water_delta
            self.gum_molflow += gum_delta
            # update fractions
            if not self.co_molflow == 0:
                self.co_frac = self.co_molflow / self.mol_flow
            if not self.aco_molflow == 0:
                self.aco_frac = self.aco_molflow / self.mol_flow
            if not self.dco_molflow == 0:
                self.dco_frac = self.dco_molflow/ self.mol_flow
            if not self.aa_molflow == 0:
                self.aa_frac = self.aa_molflow / self.mol_flow
            if not self.water_molflow == 0:
                self.water_frac = self.water_molflow / self.mol_flow
            if not self.gum_molflow == 0:
                self.gum_frac = self.gum_molflow / self.mol_flow
        else:
            raise Exception("New molar flowrate defined as negative.")
        return None
