from . import u
import warnings
import numpy as np
from . import chemicals
from .chemicals import DryChemical


class Buffer:
    """Describes a buffering solution with one acidic and one basic component, made from dry chemicals."""

    def __init__(self, pka: float, acid: DryChemical, base: DryChemical):
        """

        Parameters
        ----------
        pka - the acid constant of the buffer in inverse log units
        acid - Chemical, the acidic component of the buffer
        base - Chemical, the basic component of the buffer
        """

        self.pka = pka
        self.acid = acid
        self.base = base

    def recipe_at_ph(self, ph: float, concentration: u.Quantity, volume: u.Quantity = u.Quantity(1.0, 'liter')):
        """
        Provide a recipe at a given ph, concentration, and volume

        Parameters
        ----------
        ph - the pH for this buffer
        concentration: the concentration of the buffering component in units of mol/liter
        volume: the total volume of the buffer, default 1 liter

        Returns
        -------
        str - recipe
        """

        if ph > self.pka + 1.1:
            warnings.warn("ph {} above presumed buffering range of this buffer".format(ph))
        elif ph < self.pka - 1.1:
            warnings.warn("ph {} below presumed buffering range of this buffer".format(ph))

        total_moles = concentration * volume

        # Henderson-Hasselbalch
        A_HA_ratio = np.power(10.0, ph - self.pka)
        acid_moles = total_moles / (A_HA_ratio + 1)
        base_moles = total_moles - acid_moles

        base_weight = base_moles * self.base.mw * (100.0/self.base.purity)
        acid_weight = acid_moles * self.acid.mw * (100.0/self.acid.purity)

        return ("pH {0:.2f}:\n{1}: {3:.3f};\n{2}: {4:.3f}\nper {5:.3f} \n ".format(ph, self.base.name, self.acid.name, base_weight.to('grams'),
                                                                   acid_weight.to('grams'), volume.to('liter')))


Tris_buffer = Buffer(8.06, chemicals.Trizma_hydrochloride, chemicals.TRIS_base)
Sodium_Phosphate_buffer = Buffer(7.2, chemicals.Sodium_Phosphate_Monobasic_Dihydrate, chemicals.Sodium_Phosphate_Monobasic_Dihydrate)