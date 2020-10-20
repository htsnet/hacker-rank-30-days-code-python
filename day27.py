# Testing

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx
class TestDataEmptyArray(object):
    
    @staticmethod
    def get_array():
        return []

class TestDataUniqueValues(object):
    values = []
    # from 8 to 2 integers in order reverse
    for i in range(8,1,-1):
        values.append(i)
    @staticmethod
    def get_array():
        return TestDataUniqueValues.values

    @staticmethod
    def get_expected_result():
        values = TestDataUniqueValues.get_array()
        return values.index(min(values))

class TestDataExactlyTwoDifferentMinimums(object):
    values = [4, 3, 5, 6, 3, 8]
    @staticmethod
    def get_array():
        return TestDataExactlyTwoDifferentMinimums.values

    @staticmethod
    def get_expected_result():
        values = TestDataExactlyTwoDifferentMinimums.get_array()
        return 1


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")

