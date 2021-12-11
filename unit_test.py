'''
Unit testing for the sorting functions in VisualSort

Testing procedure goes like this
1. Create VisualSort class with 1000 elements (must include unit_test=True to stop class from drawing)
2. Call .reset() class to shuffle contents in self.array
3. Call their respective sorting functions
4. Check if the elements are sorted
5. Repeat from step 2 for 500 times

If nothing goes wrong, the unit testing will show 5 test cases passing

This process took around 4 minutes to run so don't panic
'''
import unittest
from main import VisualSort

class TestSortingMethods(unittest.TestCase):
    def test_insertion_sort(self):
        test_class = VisualSort(None, size=1000, unit_test=True)
        for _ in range(500):
            test_class.reset()
            test_class.insertion_sort()
            self.assertTrue(test_class._is_sorted())


    def test_selection_sort(self):
        test_class = VisualSort(None, size=1000, unit_test=True)
        for _ in range(500):
            test_class.reset()
            test_class.selection_sort()
            self.assertTrue(test_class._is_sorted())

    def test_quicksort(self):
        test_class = VisualSort(None, size=1000, unit_test=True)
        for _ in range(500):
            test_class.reset()
            test_class.quicksort()
            self.assertTrue(test_class._is_sorted())
    
    def test_bubble_sort(self):
        test_class = VisualSort(None, size=1000, unit_test=True)
        for _ in range(500):
            test_class.reset()
            test_class.bubble_sort()
            self.assertTrue(test_class._is_sorted())

    def test_merge_sort(self):
        test_class = VisualSort(None, size=1000, unit_test=True)
        for _ in range(500):
            test_class.reset()
            test_class.merge_sort()
            self.assertTrue(test_class._is_sorted())

if __name__ == '__main__':
    unittest.main()