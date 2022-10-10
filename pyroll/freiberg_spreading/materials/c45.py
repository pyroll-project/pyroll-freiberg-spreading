import sys

from pyroll.core import RollPass
from pyroll.utils import hookutils
from ..coefficients_lib import temperature_coefficient_high_alloyed


@RollPass.Profile.hookimpl
@hookutils.for_materials("C45")
def freiberg_spreading_material_coefficient(profile):
    return 1


@RollPass.Profile.hookimpl
@hookutils.for_materials("C45")
def freiberg_spreading_temperature_coefficient(roll_pass, profile):
    return temperature_coefficient_high_alloyed(
        profile,
        a=-1.47e-5,
        b=7.108e-3,
        c=1.0216
    )


RollPass.Profile.plugin_manager.register(sys.modules[__name__])
