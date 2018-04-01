import unittest

from allergies import Allergies

# Python 2/3 compatibility
if not hasattr(unittest.TestCase, 'assertCountEqual'):
    unittest.TestCase.assertCountEqual = unittest.TestCase.assertItemsEqual


# test cases adapted from `x-common//canonical-data.json` @ version: 1.0.0

def print_test(name):
    print "test:", name

class AllergiesTests(unittest.TestCase):
    def test_no_allergies_means_not_allergic(self):
        print_test("test_no_allergies_means_not_allergic")
        allergies = Allergies(0)
        self.assertFalse(allergies.is_allergic_to('peanuts'))
        self.assertFalse(allergies.is_allergic_to('cats'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_is_allergic_to_eggs(self):
        print_test("test_is_allergic_to_eggs")
        self.assertTrue(Allergies(1).is_allergic_to('eggs'))

    def test_allergic_to_eggs_in_addition_to_other_stuff(self):
        print_test("test_allergic_to_eggs_in_addition_to_other_stuff")
        allergies = Allergies(5)
        self.assertTrue(allergies.is_allergic_to('eggs'))
        self.assertTrue(allergies.is_allergic_to('shellfish'))
        self.assertFalse(allergies.is_allergic_to('strawberries'))

    def test_no_allergies_at_all(self):
        print_test("test_no_allergies_at_all")
        self.assertEqual(Allergies(0).lst, [])

    def test_allergic_to_just_eggs(self):
        print_test("test_allergic_to_just_eggs")
        self.assertEqual(Allergies(1).lst, ['eggs'])

    def test_allergic_to_just_peanuts(self):
        print_test("test_allergic_to_just_peanuts")
        self.assertEqual(Allergies(2).lst, ['peanuts'])

    def test_allergic_to_just_strawberries(self):
        print_test("test_allergic_to_just_strawberries")
        self.assertEqual(Allergies(8).lst, ['strawberries'])

    def test_allergic_to_eggs_and_peanuts(self):
        print_test("test_allergic_to_eggs_and_peanuts")
        self.assertCountEqual(Allergies(3).lst, ['eggs', 'peanuts'])

    def test_allergic_to_more_than_eggs_but_not_peanuts(self):
        print_test("test_allergic_to_more_than_eggs_but_not_peanuts")
        self.assertCountEqual(Allergies(5).lst, ['eggs', 'shellfish'])

    def test_allergic_to_lots_of_stuff(self):
        print_test("test_allergic_to_lots_of_stuff")
        self.assertCountEqual(
            Allergies(248).lst,
            ['strawberries', 'tomatoes', 'chocolate', 'pollen', 'cats'])

    def test_allergic_to_everything(self):
        print_test("test_allergic_to_everything")
        self.assertCountEqual(
            Allergies(255).lst, [
                'eggs', 'peanuts', 'shellfish', 'strawberries', 'tomatoes',
                'chocolate', 'pollen', 'cats'
            ])

    def test_ignore_non_allergen_score_parts_only_eggs(self):
        print_test("test_ignore_non_allergen_score_parts_only_eggs")
        self.assertEqual(Allergies(257).lst, ['eggs'])

    def test_ignore_non_allergen_score_parts(self):
        print_test("test_ignore_non_allergen_score_parts")
        self.assertCountEqual(
            Allergies(509).lst, [
                'eggs', 'shellfish', 'strawberries', 'tomatoes', 'chocolate',
                'pollen', 'cats'
            ])


if __name__ == '__main__':
    unittest.main()
