import warnings
from . import u

Q = u.Quantity

class DryChemical:
    """Respresents one chemical component."""
    def __init__(self, name: str, mw: u.Quantity, purity: float =100.0):
        """
        Instantiate a chemical

        Parameters
        ----------
        name - str, name of the chemical component
        mw - Quantity, Molecular weight (in units compatible with gram/mol)
        purity - float, Purity of a substance in percent: default 100.0
        """

        self.name = name
        self.mw = mw.to('gram/mole')
        if purity > 100.0 or purity < 0.0:
            raise ValueError("Purity ({}), should be between 0.0 and 100.0.".format(purity))
        if 1.0 >= purity > 0:
            raise warnings.warn("Purity needs to be a percentage, but it looks like a fraction was specified.")

        self.purity = purity


TRIS_base = DryChemical('TRIS (Base), Ultrapure Bioreagent', Q(121.14, 'gram/mole') )
Trizma_hydrochloride = DryChemical('Trizma Hydrochloride Reagent Grade 99.0%', Q(157.6, 'gram/mole'), 99.0)
Sodium_Phosphate_Monobasic_Dihydrate = DryChemical('Sodium Phosphate Monobasic Dihydrate BioUltra', Q(156.01, 'gram/mole'), 99.0)
Sodium_Phosphate_Dibasic = DryChemical('Sodium Phosphate Dibasic Puriss', Q(141.96, 'gram/mol'), 99.0)
Sodium_Chloride = DryChemical('Sodium Chloride ReagentPlus 99.0%', Q(58.44, 'gram/mole'), 99.0)