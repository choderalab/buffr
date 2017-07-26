import buffr
import numpy as np

Kinase_Binding_Assay_Buffer = buffr.Tris_buffer

volume = buffr.u.Quantity(1, 'liter')
concentration = buffr.u.Quantity(20, 'millimole/liter')

# No TCEP kinase assay buffer
print("Kinase Assay Buffer acid/base component recipe for pH")
for pH in np.linspace(7.0, 9.0, 21):
    print(Kinase_Binding_Assay_Buffer.recipe_at_ph(pH, concentration, volume))

# Carbonic anhydrase II ITC buffer
CAII_ITC_Buffer = buffr.Sodium_Phosphate_buffer
CAII_ITC_Buffer.add_extra_dry_component(buffr.chemicals.Sodium_Chloride, buffr.u.Quantity(150, 'millimole/liter'))

volume = buffr.u.Quantity(1, 'liter')
concentration = buffr.u.Quantity(20, 'millimole/liter')
print("\n\nCAII buffer acid/base component recipe for pH")
for pH in np.linspace(6.2, 8.2, 21):
    print(CAII_ITC_Buffer.recipe_at_ph(pH, concentration, volume))

# CB7 recipe
CB7_Host_Guest_Buffer = buffr.Sodium_Phosphate_buffer
volume = buffr.u.Quantity(1, 'liter')
concentration = buffr.u.Quantity(100, 'millimole/liter')
print("\n\nCB7 Host Guest acid/base component recipe for pH")
for pH in np.linspace(6.2, 8.2, 21):
    print(CB7_Host_Guest_Buffer.recipe_at_ph(pH, concentration, volume))
