RUN_AS = 'excel'    # options = 'excel', 'terminal'(TODO)
FLUID_PROPERTY_LIBRARY = "GPA_2145" # options = 'GPA_2145', 'DWSIM'(TODO)
USE_LEE_KESLER_COMPRESSIBILITY_FACTOR = False
FLOAT_COMPARE_TOLERANCE = 1.0E-4
# Default is to use 60/30/10 nC6/nC7/nC8 split per GPA Standard 2261-00
HEXANE_PLUS_N_HEXANE_FRACTION = 0.6
HEXANE_PLUS_N_HEPTANE_FRACTION = 0.3
HEXANE_PLUS_N_OCTANE_FRACTION = 0.1
FT3_PER_MCF = 1.0E3
BTU_PER_MMBTU = 1.0E6
UNIVERSAL_GAS_CONSTANT = 10.7316    # ft3-psia/lbmol-R
FAHRENHEIT_TO_RANKINE = 459.67
CELSIUS_TO_KELVIN = 273.15
DWSIM_PROPERTY_PACKAGE = "Peng-Robinson (PR)"
PSIA_TO_PA = 6894.76
M3_TO_MCF = 0.0353147
M3_TO_BBL = 6.29
FT3_TO_BBL = 0.17811
FT2_PER_S_TO_M2_PER_S = 0.092903
KG_PER_M3_TO_LBM_PER_FT3 = 0.062428
LBMOL_TO_MOL = 453.59237
KMOL_TO_MOL = 1000.0
REFERENCE_DENSITY_OF_WATER = 62.366 # lbm/ft3 at 60 F and 1 atm
OIL_CHARACTERIZATION_TC_CORR = "Riazi-Daubert (1985)"
OIL_CHARACTERIZATION_PC_CORR = "Riazi-Daubert (1985)"
OIL_CHARACTERIZATION_AF_CORR = "Lee-Kesler (1976)"
OIL_CHARACTERIZATION_MW_CORR = "Winn (1956)"
OIL_CHARACTERIZATION_MW_LIGHTEST_PSEUDOCOMPONENT = 80.0
OIL_CHARACTERIZATION_SG_LIGHTEST_PSEUDOCOMPONENT = 0.7
OIL_CHARACTERIZATION_NBP_LIGHTEST_PSEUDOCOMPONENT = 139.73  # F = 333.0 K
OIL_CHARACTERIZATION_NUMBER_OF_PSEUDOCOMPONENTS = 10
OIL_CHARACTERIZATION_ADJUST_ACENTRIC_FACTORS = True
OIL_CHARACTERIZATION_ADJUST_RACKETT_PARAMETERS = True
OIL_CHARACTERIZATION_ASSAY_NAME = "Oil"
DEFAULT_STANDARD_PRESSURE = 14.65   # psia
DEFAULT_STANDARD_TEMPERATURE = 60.0   # F