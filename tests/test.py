from mypackage import myModule

def test_top_n():
    """
    make sure top_n works correctly
    """
    assert myModule.top_n([4,5,3,8,4], 2) == [8,5], 'incorrect'
    assert myModule.top_n([10, 1, 12, 9, 2], 2) == [12,10], 'incorrect'
    assert myModule.top_n([1,2,3,4,5],5) == [5,4,3,2,1], 'incorrect'