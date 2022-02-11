import numpy as np

from pyroll import RollPass


def filling_coefficient(
        roll_pass: RollPass,
        a1,
        b1,
        n1,
        a2,
        b2,
        n2,
        critical_ratio,
        min_ratio
):
    filling_ratio = roll_pass.out_profile.filling_ratio

    if filling_ratio > critical_ratio:
        return a2 * filling_ratio ** n2 + b2

    return a1 * filling_ratio ** n1 + b1


def roll_gap_ratio_coefficient(
        roll_pass: RollPass,
        a,
        n
):
    return a * (roll_pass.roll_radius / roll_pass.height) ** n


def tension_coefficient(
        roll_pass: RollPass,
        a,
        b
):
    if roll_pass.velocity < roll_pass.tension_less_velocity:
        c = a
    else:
        c = b
    return 1 - c * (roll_pass.velocity - roll_pass.tension_less_velocity) / roll_pass.tension_less_velocity


def velocity_coefficient(
        roll_pass: RollPass,
        a,
        b,
        c,
        n,
        v_min,
        v_crit
):
    if roll_pass.velocity < v_crit:
        return a * ((roll_pass.velocity - v_min) / 1e3) ** n + b

    return 1 - c * (roll_pass.velocity - v_crit) / 1e3


def diagonals_ratio_coefficient(
        roll_pass: RollPass,
        a,
        n
):
    profile_diagonals_ratio = roll_pass.in_profile.rotated.height / roll_pass.in_profile.rotated.width
    pass_diagonals_ratio = roll_pass.groove.usable_width / roll_pass.height
    diagonals_ratio = profile_diagonals_ratio if profile_diagonals_ratio > pass_diagonals_ratio else pass_diagonals_ratio
    diagonals_ratio = diagonals_ratio if diagonals_ratio > 1 else 1 / diagonals_ratio
    return a * diagonals_ratio ** n


def temperature_coefficient_low_alloyed(
        roll_pass: RollPass,
        a,
        b,
):
    return a + b * (roll_pass.mean_temperature - 273.15)


def temperature_coefficient_high_alloyed(
        roll_pass: RollPass,
        a,
        b,
        c,
):
    return a * np.exp(b * (roll_pass.mean_temperature - 273.15)) + c
