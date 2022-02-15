import sys

from pyroll.core import RollPass
import pyroll.core.grooves as grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves
from .. import coefficients_lib


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.RoundGrooveBase)
def freiberg_spreading_velocity_coefficient(roll_pass: RollPass):
    return coefficients_lib.velocity_coefficient(
        roll_pass,
        a=0.016,
        b=0.986,
        n=-0.35,
        c=0.001,
        v_min=0.01e3,
        v_crit=1.5e3
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.RoundGrooveBase)
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.roll_gap_ratio_coefficient(
        roll_pass,
        a=0.8317,
        n=0.08
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.RoundGrooveBase)
def freiberg_spreading_filling_coefficient(roll_pass: RollPass):
    return coefficients_lib.filling_coefficient(
        roll_pass,
        a1=0.19579019,
        b1=0.82420981,
        n1=5.1507655,
        a2=0,
        b2=1,
        n2=0,
        critical_ratio=0.98,
        min_ratio=0.88
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.RoundGrooveBase)
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.diagonals_ratio_coefficient(
        roll_pass,
        a=1.03,
        n=0.28
    )


RollPass.plugin_manager.register(sys.modules[__name__])
