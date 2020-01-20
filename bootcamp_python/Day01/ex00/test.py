import unittest
from book import Book
from recipe import Recipe


class TestBookInstances(unittest.TestCase):
    def test_no_name(self):
        with self.assertRaises(Exception) as e:
            b = Book()

    def test_name_assignation(self):
        b = Book(name='Test')
        self.assertEqual(b.name, 'Test')
        
    def test_get_recipe(self):
        r = Recipe(
            name='Pain',
            cooking_lvl=1,
            cooking_time=15,
            ingredients=['menfou'],
            recipe_type='starter'
        )
        b = Book(name='Test')
        b.add_recipe(r)
        self.assertIn(r, b.recipe_list[r.recipe_type])


if __name__ == "__main__":
    unittest.main()