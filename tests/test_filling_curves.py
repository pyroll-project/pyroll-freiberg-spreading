import matplotlib.pyplot as plt
import numpy as np
import pytest

import pyroll.core as pr
import pyroll.freiberg_spreading


class MockProfile:
    def __init__(self, classifier: str):
        self.classifiers = [classifier]
        self.filling_ratio = 1.0


class MockRollPass:
    def __init__(self, in_cls: str, out_cls: str):
        self.in_profile = MockProfile(in_cls)
        self.out_profile = MockProfile(out_cls)
        self.classifiers = [out_cls]


@pytest.mark.parametrize(
    "rp",
    [
        MockRollPass("diamond", "diamond"),
        MockRollPass("diamond", "square"),
        MockRollPass("oval", "round"),
        MockRollPass("oval", "square"),
        MockRollPass("round", "oval"),
        MockRollPass("square", "diamond"),
        MockRollPass("square", "oval"),
    ],
)
def test_filling_curve(rp: MockRollPass):
    def get_coeff(filling_ratio: float) -> float:
        rp.out_profile.filling_ratio = filling_ratio
        return pr.RollPass.freiberg_spreading_filling_coefficient.get_result(rp)

    filling_ratios = np.linspace(0, 1.2, 500)
    coeffs = np.vectorize(get_coeff)(filling_ratios)

    plt.figure()
    plt.plot(filling_ratios, coeffs)
    plt.title(f"{rp.in_profile.classifiers}->{rp.classifiers}")
    plt.show()
    plt.close()
