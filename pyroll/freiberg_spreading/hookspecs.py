import sys

from pyroll.core import RollPass


@RollPass.Profile.hookspec
def freiberg_spreading_material_coefficient(roll_pass, profile):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.Profile.hookspec
def freiberg_spreading_temperature_coefficient(roll_pass, profile):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def freiberg_spreading_tension_coefficient(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def freiberg_spreading_filling_coefficient(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def freiberg_spreading_diagonals_ratio_coefficient(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def freiberg_spreading_roll_gap_ratio_coefficient(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def freiberg_spreading_velocity_coefficient(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


@RollPass.hookspec
def tension_less_velocity(roll_pass):
    """Get a FreibergSpreadModelTensionCoefficient object suitable for the given roll pass.
    Return None if the implementation cannot serve this.
    The first not None result is taken."""


RollPass.plugin_manager.add_hookspecs(sys.modules[__name__])
RollPass.Profile.plugin_manager.add_hookspecs(sys.modules[__name__])
