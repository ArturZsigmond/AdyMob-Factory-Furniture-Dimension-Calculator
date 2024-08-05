from furniture import Furniture
from utils import get_thickness, get_unit_conversion_factor

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
    bottom_between_sides = top_between_sides  # If top is between, bottom is also between

    furniture = Furniture(height, length, width, thickness, front_thickness, back_thickness)
    sides = furniture.calculate_sides(top_between_sides, bottom_between_sides)
    total_area = furniture.calculate_material_needed(sides)

    print("\nDimensiunile părților de tăiat:")
    for side, dimensions in sides.items():
        print(f"{side}: {dimensions[0]} {unit} x {dimensions[1]} {unit}")

    unit_conversion_factor = get_unit_conversion_factor(unit)
    total_area_m2 = total_area * unit_conversion_factor
    print(f"\nSuprafața totală a materialului necesar: {total_area_m2:.2f} m²")

if __name__ == "__main__":
    main()
