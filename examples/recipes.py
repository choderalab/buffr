import buffr
import numpy as np

Kinase_Binding_Assay_Buffer = buffr.Tris_buffer
CB7_Host_Guest_Buffer = buffr.Sodium_Phosphate_buffer
CAII_ITC_Buffer = buffr.Sodium_Phosphate_buffer

volume = buffr.u.Quantity(1, 'liter')
concentration = buffr.u.Quantity(20, 'millimole/liter')


print("Kinase Assay Buffer acid/base component recipe for pH")
for pH in np.linspace(7.0,9.0,21):
    print(Kinase_Binding_Assay_Buffer.recipe_at_ph(pH, concentration, volume))


print("CB7 Host Guest acid/base acid/base component recipe for pH")
for pH in np.linspace(6.2,8.2,21):
    print(CB7_Host_Guest_Buffer.recipe_at_ph(pH, concentration, volume))

