class Furniture:
    def __init__(self, height, length, width, thickness, front_thickness, back_thickness):
        self.height = height
        self.length = length
        self.width = width
        self.thickness = thickness
        self.front_thickness = front_thickness
        self.back_thickness = back_thickness

    def calculate_sides(self, top_between_sides, bottom_between_sides):
        # Adjust height for top and bottom parts
        if not top_between_sides:
            height_with_top = self.height - self.thickness["Top"]
        else:
            height_with_top = self.height

        if not bottom_between_sides:
            height_with_bottom = height_with_top - self.thickness["Bottom"]
        else:
            height_with_bottom = height_with_top

        # Adjust width for front and back parts
        width_adjusted = self.width - self.back_thickness - self.front_thickness

        sides = {
            "Top/Bottom": (self.length, self.width),
            "Front/Back": (height_with_bottom, self.length),
            "Left/Right": (height_with_bottom, width_adjusted)
        }
        return sides

    def calculate_material_needed(self, sides):
        total_area = 0
        for dimensions in sides.values():
            total_area += dimensions[0] * dimensions[1]
        return total_area
