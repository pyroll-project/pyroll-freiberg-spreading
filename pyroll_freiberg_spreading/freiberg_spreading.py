import sys
from logging import getLogger

import numpy as np

from pyroll.roll_pass import RollPass
from . import coefficients_lib

_log = getLogger(__name__)


@RollPass.hookimpl
def freiberg_spreading_tension_coefficient(roll_pass):
    return coefficients_lib.tension_coefficient(
        roll_pass,
        a=0.76,
        b=0.12
    )


@RollPass.hookimpl
def tension_less_velocity(roll_pass):
    return roll_pass.velocity


@RollPass.hookimpl
def width_change(roll_pass: RollPass):
    parts = np.array([
        roll_pass.in_profile.freiberg_spreading_material_coefficient,
        roll_pass.in_profile.freiberg_spreading_temperature_coefficient,
        roll_pass.freiberg_spreading_tension_coefficient,
        roll_pass.freiberg_spreading_filling_coefficient,
        roll_pass.freiberg_spreading_diagonals_ratio_coefficient,
        roll_pass.freiberg_spreading_roll_gap_ratio_coefficient,
        roll_pass.freiberg_spreading_velocity_coefficient
    ])

    if not np.all(parts):
        return None

    _log.debug(f"Used Freiberg spreading model for roll pass {roll_pass.label}.")
    spreading = np.prod(parts)
    return (spreading - 1) * roll_pass.in_profile.rotated.width


RollPass.plugin_manager.register(sys.modules[__name__])
