from pyroll.core import RollPass


@RollPass.hookimpl
def freiberg_spreading_material_coefficient(roll_pass):
    return 1


@RollPass.hookimpl
def freiberg_spreading_temperature_coefficient(roll_pass):
    return 1
