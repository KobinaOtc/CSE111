from weather import wind_chill, cels_from_fahr
from pytest import approx
import pytest 

def test_wind_chill():
    chill = wind_chill(0, 3)
    assert chill == approx(-6.9)

    chill = wind_chill(-5, 5)
    assert chill == approx(-16.4)

    chill = wind_chill(-10, 3)
    assert chill == approx(-18.2)

# def test_heat_index():
#     assert heat_index(80, 80) == approx(84.2)
#     assert heat_index(85, 80) == approx(96.8)
#     assert heat_index(96, 70) == approx(126.4)

def test_cels_from_fahr():
    """Test the cels_from_fahr function by calling it and
    comparing the values it returns to the expected values.
    Notice this test function uses pytest.approx to compare
    floating-point numbers.
    """
    assert cels_from_fahr(-25) == approx(-31.66667)
    assert cels_from_fahr(0) == approx(-17.77778)
    assert cels_from_fahr(32) == approx(0)
    assert cels_from_fahr(70) == approx(21.1111)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(['-v', '--tb=line', '-rN', __file__])