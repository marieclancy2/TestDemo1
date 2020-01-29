import pytest
import productionCode
def test_good_list():
    test_data = ["Hi Hi Hi there you%%",
                 "There Hi RTRE$^%$  $#%$#FGF %$^Hi"]
    counts = productionCode.count_words(test_data)
    assert "Hi" in counts
    assert counts["Hi"] ==5

def test_bad_data1():
    test_data = {}
    counts = productionCode.count_words(test_data)
    assert len(counts) == 0

def test_bad_data2():
    test_data = 1223
    counts = productionCode.count_words(test_data)
    assert len(counts) == 0