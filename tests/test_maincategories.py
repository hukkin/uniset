import uniset


def test_c():
    assert "\t" in uniset.C  # From Cc subcategory
    assert "\u0603" in uniset.C  # From Cf subcategory
    assert "\U000c8550" in uniset.C  # From Cn subcategory
    assert "\ue855" in uniset.C  # From Co subcategory
    assert "\ude34" in uniset.C  # From Cs subcategory
