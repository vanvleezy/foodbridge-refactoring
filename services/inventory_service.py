import json


class InventoryService:
    def load_inventory(self):
        with open("data/inventory.json", "r") as f:
            return json.load(f)

    def save_inventory(self, inventory):
        with open("data/inventory.json", "w") as f:
            json.dump(inventory, f, indent=2)

    @staticmethod
    def _required_food_boxes(request):
        """Return the food-box quantity required for a household."""
        household_size = request.get("household_size", 0)
        if household_size >= 7:
            return 3
        if household_size >= 4:
            return 2
        return 1

    def can_fulfill(self, request, inventory):
        needed_boxes = self._required_food_boxes(request)

        if inventory.get("food_box", 0) < needed_boxes:
            return False
        if request.get("needs_baby_items") and inventory.get("baby_kit", 0) < 1:
            return False
        if request.get("needs_hygiene") and inventory.get("hygiene_kit", 0) < 1:
            return False
        return True

    def reserve_items(self, request, inventory):
        needed_boxes = self._required_food_boxes(request)
        inventory["food_box"] = inventory.get("food_box", 0) - needed_boxes
        if request.get("needs_baby_items"):
            inventory["baby_kit"] = inventory.get("baby_kit", 0) - 1
        if request.get("needs_hygiene"):
            inventory["hygiene_kit"] = inventory.get("hygiene_kit", 0) - 1

    def restock_if_low(self, inventory):
        if inventory.get("food_box", 0) < 10:
            print("Low food box inventory")
        if inventory.get("baby_kit", 0) < 4:
            print("Low baby kit inventory")
        if inventory.get("hygiene_kit", 0) < 4:
            print("Low hygiene inventory")
