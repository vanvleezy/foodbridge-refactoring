import unittest

from services.inventory_service import InventoryService
from utils.helpers import safe_int


class InventoryRefactoringTests(unittest.TestCase):
    def setUp(self):
        self.service = InventoryService()

    def test_food_box_thresholds(self):
        self.assertEqual(self.service._required_food_boxes({"household_size": 2}), 1)
        self.assertEqual(self.service._required_food_boxes({"household_size": 4}), 2)
        self.assertEqual(self.service._required_food_boxes({"household_size": 7}), 3)

    def test_fulfillment_and_reservation_use_same_quantity(self):
        request = {"household_size": 5, "needs_baby_items": False, "needs_hygiene": False}
        inventory = {"food_box": 2}
        self.assertTrue(self.service.can_fulfill(request, inventory))
        self.service.reserve_items(request, inventory)
        self.assertEqual(inventory["food_box"], 0)

    def test_safe_int_conversion_and_default(self):
        self.assertEqual(safe_int("12"), 12)
        self.assertEqual(safe_int("not-a-number", 9), 9)
        self.assertEqual(safe_int(None, 4), 4)


    def test_safe_int_handles_whitespace_and_negative_numbers(self):
        self.assertEqual(safe_int(" 15 "), 15)
        self.assertEqual(safe_int("-8"), -8)

    def test_safe_int_preserves_default_for_invalid_values(self):
        self.assertEqual(safe_int("invalid", 25), 25)
        self.assertEqual(safe_int(None, -1), -1)

    def test_zero_and_small_households_require_one_box(self):
        self.assertEqual(self.service._required_food_boxes({"household_size": 0}), 1)
        self.assertEqual(self.service._required_food_boxes({"household_size": 3}), 1)

    def test_household_boundary_requires_two_boxes(self):
        self.assertEqual(self.service._required_food_boxes({"household_size": 6}), 2)

if __name__ == "__main__":
    unittest.main()
