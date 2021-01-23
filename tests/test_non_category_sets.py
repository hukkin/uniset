import uniset


def test_whitespace():
    assert "\t" in uniset.WHITESPACE


def test_punctuation():
    assert "." in uniset.PUNCTUATION
