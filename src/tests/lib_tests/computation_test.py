import pytest
from src.lib.utils.computation import ComputationError, Computation
from src.models.location import Location


class TestComputation:
    @staticmethod
    def test_distance_with_one_location():
        with pytest.raises(ComputationError) as exception_info:
            Computation.compute_distance(Location(51.8856167, -10.4240951), None)
        assert exception_info.value.message == "Two locations are needed to calculate the distance"

    @staticmethod
    def test_distance_with_same_location():
        distance = Computation.compute_distance(Location(51.8856167, -10.4240951), Location(51.8856167, -10.4240951))
        assert distance == 0.0

    @staticmethod
    def test_distance_with_different_location():
        distance = Computation.compute_distance(Location(51.8856167, -10.4240951), Location(53.339428, -6.257664))
        assert distance == 324.37491200828447
