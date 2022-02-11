import sys

from pyroll.core import RollPass
import pyroll.core.grooves as grooves
from pyroll.utils.hookutils import applies_to_in_grooves, applies_to_out_grooves
from .. import coefficients_lib


@RollPass.hookimpl
@applies_to_in_grooves(grooves.SquareGroove)
@applies_to_out_grooves(grooves.FlattenedOvalGroove, grooves.CircularOvalGroove)
def freiberg_spreading_velocity_coefficient(roll_pass: RollPass):
    return coefficients_lib.velocity_coefficient(
        roll_pass,
        a=0.025,
        b=0.979,
        n=-0.47,
        c=0.0013,
        v_min=0.01e3,
        v_crit=1.5e3
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.SquareGroove)
@applies_to_out_grooves(grooves.FlattenedOvalGroove, grooves.CircularOvalGroove)
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.roll_gap_ratio_coefficient(
        roll_pass,
        a=0.7805,
        n=0.1076
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.SquareGroove)
@applies_to_out_grooves(grooves.FlattenedOvalGroove, grooves.CircularOvalGroove)
def freiberg_spreading_filling_coefficient(roll_pass: RollPass):
    return coefficients_lib.filling_coefficient(
        roll_pass,
        a1=0.131,
        b1=0.9001,
        n1=9.42,
        a2=0,
        b2=1,
        n2=0,
        critical_ratio=0.98,
        min_ratio=0.88
    )


@RollPass.hookimpl
@applies_to_in_grooves(grooves.SquareGroove)
@applies_to_out_grooves(grooves.FlattenedOvalGroove, grooves.CircularOvalGroove)
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.diagonals_ratio_coefficient(
        roll_pass,
        a=1.03,
        n=0.38
    )


RollPass.plugin_manager.register(sys.modules[__name__])
