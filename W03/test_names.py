from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    # tests for checking if the full name function returns the right output

    assert make_full_name('Sally', 'Brown') == 'Brown; Sally'
    assert make_full_name('Kobina', 'Otchere') == 'Otchere; Kobina'
    assert make_full_name('Jerry', 'Osborn') == 'Osborn; Jerry'

def test_extract_family_name():
    # tests for checking if the family name function returns the right output
    
    assert extract_family_name('Brown; Sally') == 'Brown'
    assert extract_family_name('Otchere; Kobina') == 'Otchere'
    assert extract_family_name('Osborn; Jerry') == 'Osborn'

def test_extract_given_name():
    # tests for checking if the family name function returns the right output
    
    assert extract_given_name('Brown; Sally') == 'Sally'
    assert extract_given_name('Otchere; Kobina') == 'Kobina'
    assert extract_given_name('Osborn; Jerry') == 'Jerry'

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])