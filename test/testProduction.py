import pytest
import productionCode

def test_good_list():
    test_data = ["Hi Hi Hi there you%%",
                 "There Hi RTRE$^%$  $#%$#FGF %$^Hi"]
    counts = productionCode.count_words(test_data)
    assert "Hi" in counts
    assert counts["Hi"] ==5