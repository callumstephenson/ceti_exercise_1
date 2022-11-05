from classes.chemical import *
# This module provides the stream class for the calculations

# chemical("name", carbon n, hydrogen n, oxygen)
water = chemical("Water", 0, 2, 1)
co = chemical("Castor Oil", 19, 36, 3)
aco = chemical("Acetylated Castor Oil", 21, 38, 4)
dco = chemical("Dehydrated Castor Oil", 19, 34, 2)
aa = chemical("Acetic Acid", 2, 4, 2)
gum = chemical("Gum", 38, 68, 4)
class stream:
    'A class for the stream object, containing, molar flowrate, and molar fractions of each chemical'

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
            d += "   Molar Flowrate (mol/hr):      {}\n".format(self.mol_flow)
            d += "   CO Mole Fraction:    {}\n".format(self.co_frac)
            d += "   ACO Mole Fraction:    {}\n".format(self.aco_frac)
            d += "   DCO Mole Fraction:          {}\n".format(self.dco_frac)
            d += "   AA Mole Fraction:         {}\n".format(self.aa_frac)
            d += "   Water Mole Fraction: {}\n".format(self.water_frac)
            d += "   Gum Mole Fraction:   {}\n".format(self.gum_frac)
            d += "   CO Mass Flowrate:    {}\n".format(self.co_massflow)
            d += "   ACO Mass Flowrate:    {}\n".format(self.aco_massflow)
            d += "   DCO Mass Flowrate:          {}\n".format(self.dco_massflow)
            d += "   AA Mass Flowrate:         {}\n".format(self.aa_massflow)
            d += "   Water Mass Flowrate: {}\n".format(self.water_massflow)
            d += "   Gum Mass Flowrate:  {}\n".format(self.gum_massflow)
            d += "   Total Mass Flowrate:   {}\n".format(self.mass_flow)
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
    
    def massflow(self):
        self.co_massflow = self.co_molflow * co.mr_kg
        self.aco_massflow = self.aco_molflow * aco.mr_kg
        self.dco_massflow = self.dco_molflow * dco.mr_kg
        self.aa_massflow = self.aa_molflow * aa.mr_kg
        self.water_massflow = self.water_molflow * water.mr_kg
        self.gum_massflow = self.gum_molflow * gum.mr_kg
        self.mass_flow = self.co_massflow + self.aco_massflow + self.dco_massflow + self.aa_massflow + self.water_massflow + self.gum_massflow
        return None