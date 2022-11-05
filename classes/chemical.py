# This module provides the chemical class for use in the main script

class chemical:
    'A class for creating chemicals with set properties, relative mass'

    def __init__(self, name, carbon_atoms, hydrogen_atoms, oxygen_atoms):
        'class initialisation of name, carbon atom amount, hydrogen atom amount, oxygen atom amount (per molecule)'
        
        self.name = name
        if hydrogen_atoms >= 0 and carbon_atoms >= 0 and oxygen_atoms >= 0:
            self.valid = True
            self.carbon_atoms = carbon_atoms
            self.hydrogen_atoms = hydrogen_atoms
            self.oxygen_atoms = oxygen_atoms
            self.mr = (carbon_atoms * 12) + hydrogen_atoms + (oxygen_atoms * 16)
            self.mr_kg = self.mr / 1000
        else:
            self.valid = False
            raise Exception("One or more values of atoms per molecule is negative.")

    def __repr__(self):
        'self calling print function to print the properties of the chemical'
        d = "Chemical name:     {}\n".format(self.name)
        if self.valid:
            d += "   Chemical Mr (g/mol):     {}\n".format(self.mr)
            d += "   Carbon atoms per molecule:      {}\n".format(self.carbon_atoms)
            d += "   Hydrogen atoms per molecule    {}\n".format(self.hydrogen_atoms)
            d += "   Oxygen atoms per molecule:    {}\n".format(self.oxygen_atoms)
            return d
