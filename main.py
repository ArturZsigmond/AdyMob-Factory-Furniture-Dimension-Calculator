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
        width_with_back = self.width - self.back_thickness
        width_with_front = width_with_back - self.front_thickness

        sides = {
            "Top/Bottom": (self.length, width_with_front),
            "Front/Back": (height_with_bottom, self.width),
            "Left/Right": (height_with_bottom, self.length)
        }
        return sides

    def calculate_material_needed(self, sides):
        total_area = 0
        for dimensions in sides.values():
            total_area += dimensions[0] * dimensions[1]
        return total_area


def get_thickness(unit):
    use_single_thickness = input(
        "Doriți să utilizați o singură grosime pentru toate părțile? (da/nu): ").strip().lower()
    thickness = {}

    if use_single_thickness == 'da':
        t = float(input(f"Introduceți grosimea ({unit}): "))
        thickness = {"Top": t, "Bottom": t, "Front": t, "Back": t, "Left": t, "Right": t}
    else:
        thickness["Top"] = float(input(f"Introduceți grosimea topului ({unit}): "))
        thickness["Bottom"] = float(input(f"Introduceți grosimea fundului ({unit}): "))
        thickness["Front"] = float(input(f"Introduceți grosimea frontului ({unit}): "))
        thickness["Back"] = float(input(f"Introduceți grosimea spatelui ({unit}): "))
        thickness["Left"] = float(input(f"Introduceți grosimea lateralei stângi ({unit}): "))
        thickness["Right"] = float(input(f"Introduceți grosimea lateralei drepte ({unit}): "))

    return thickness


def main():
    units = ["mm", "cm", "m"]
    print("Introduceți unitatea de măsură dorită (mm, cm, m):")
    unit = input().strip().lower()
    if unit not in units:
        print("Unitate de măsură invalidă! Folosim centimetri (cm) ca unitate implicită.")
        unit = "cm"

    print(f"Introduceți dimensiunile mobilierului în {unit}:")
    height = float(input(f"Înălțime ({unit}): "))
    length = float(input(f"Lungime ({unit}): "))
    width = float(input(f"Lățime ({unit}): "))

    thickness = get_thickness(unit)
    front_thickness = float(input(f"Introduceți grosimea materialului din față ({unit}): "))
    back_thickness = float(input(f"Introduceți grosimea materialului din spate ({unit}): "))

    top_between_sides = input("Partea superioară merge între laturi? (da/nu): ").strip().lower() == 'da'
    bottom_between_sides = input("Partea inferioară merge între laturi? (da/nu): ").strip().lower() == 'da'

    furniture = Furniture(height, length, width, thickness, front_thickness, back_thickness)
    sides = furniture.calculate_sides(top_between_sides, bottom_between_sides)
    total_area = furniture.calculate_material_needed(sides)

    print("\nDimensiunile părților de tăiat:")
    for side, dimensions in sides.items():
        print(f"{side}: {dimensions[0]} {unit} x {dimensions[1]} {unit}")

    unit_conversion_factor = {"mm": 0.000001, "cm": 0.0001, "m": 1}
    total_area_m2 = total_area * unit_conversion_factor[unit]
    print(f"\nSuprafața totală a materialului necesar: {total_area_m2:.2f} m²")


if __name__ == "__main__":
    main()
5