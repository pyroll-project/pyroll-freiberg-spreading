import sys

from pyroll.core import RollPass
from pyroll.utils.hookutils import for_in_profile_types, for_out_profile_types
from .. import coefficients_lib


@RollPass.hookimpl
@for_in_profile_types("square")
@for_out_profile_types("diamond")
def freiberg_spreading_velocity_coefficient(roll_pass: RollPass):
    return coefficients_lib.velocity_coefficient(
        roll_pass,
        a=-0.014,
        b=1.018,
        n=0.69,
        c=0.0024,
        v_min=0.09,
        v_crit=1.5
    )


@RollPass.hookimpl
@for_in_profile_types("square")
@for_out_profile_types("diamond")
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.roll_gap_ratio_coefficient(
        roll_pass,
        a=0.908,
        n=0.06
    )


@RollPass.hookimpl
@for_in_profile_types("square")
@for_out_profile_types("diamond")
def freiberg_spreading_filling_coefficient(roll_pass: RollPass):
    return coefficients_lib.filling_coefficient(
        roll_pass,
        a1=0.271,
        b1=0.74,
        n1=0.998,
        a2=0,
        b2=1,
        n2=0,
        critical_ratio=0.96,
        min_ratio=0.88
    )


@RollPass.hookimpl
@for_in_profile_types("square")
@for_out_profile_types("diamond")
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass: RollPass):
    return coefficients_lib.diagonals_ratio_coefficient(
        roll_pass,
        a=1.02,
        n=0.17
    )


RollPass.plugin_manager.register(sys.modules[__name__])
