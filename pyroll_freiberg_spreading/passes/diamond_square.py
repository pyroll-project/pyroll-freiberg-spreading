import sys

from pyroll.core import RollPass, grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves
from .. import coefficients_lib


@RollPass.hookimpl
@applies_to_in_grooves(grooves.DiamondGroove)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_velocity_coefficient(roll_pass: RollPass):
    return coefficients_lib.velocity_coefficient(
        roll_pass,
        a=-0.014,
        b=1.018,
        n=0.69,
        c=0.0024,
        v_min=0.09e3,
        v_crit=1.5e3
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.DiamondGroove)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.roll_gap_ratio_coefficient(
        roll_pass,
        a=0.9179,
        n=0.0546
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.DiamondGroove)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_filling_coefficient(roll_pass: RollPass):
    return coefficients_lib.filling_coefficient(
        roll_pass,
        a1=0.05813,
        b1=0.95787,
        n1=16.92486,
        a2=0,
        b2=1,
        n2=0,
        critical_ratio=0.96,
        min_ratio=0.88
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.DiamondGroove)
@applies_to_out_grooves(grooves.SquareGroove)
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.diagonals_ratio_coefficient(
        roll_pass,
        a=1.025,
        n=0.22
    )


RollPass.plugin_manager.register(sys.modules[__name__])
