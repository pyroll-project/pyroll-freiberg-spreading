import sys

from pyroll.core import RollPass
import pyroll.core.grooves as grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves
from .. import coefficients_lib


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_velocity_coefficient(roll_pass: RollPass):
    return coefficients_lib.velocity_coefficient(
        roll_pass,
        a=0.016,
        b=0.986,
        n=-0.35,
        c=0.0013,
        v_min=0.01,
        v_crit=1.5
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.roll_gap_ratio_coefficient(
        roll_pass,
        a=0.813,
        n=0.09
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_filling_coefficient(roll_pass: RollPass):
    return coefficients_lib.filling_coefficient(
        roll_pass,
        a1=0.355,
        b1=0.65,
        n1=0.9989,
        a2=0,
        b2=1,
        n2=0,
        critical_ratio=0.97,
        min_ratio=0.88
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.OvalGrooveBase)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.diagonals_ratio_coefficient(
        roll_pass,
        a=1.003,
        n=0.42
    )


RollPass.plugin_manager.register(sys.modules[__name__])
