import sys

from pyroll import RollPassProfile
from pyroll.utils import hookutils
from ..coefficients_lib import temperature_coefficient_high_alloyed


@RollPassProfile.hookimpl
@hookutils.applies_to_materials("C45")
def freiberg_spreading_material_coefficient(profile):
    return 1


@RollPassProfile.hookimpl
@hookutils.applies_to_materials("C45")
def freiberg_spreading_temperature_coefficient(roll_pass, profile):
    return temperature_coefficient_high_alloyed(
        roll_pass,
        a=-1.47e-5,
        b=7.108e-3,
        c=1.0216
    )


RollPassProfile.plugin_manager.register(sys.modules[__name__])
