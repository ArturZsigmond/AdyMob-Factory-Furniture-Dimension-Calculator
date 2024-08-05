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
        thickness["Left"] = float(input(f"Introduceți grosimea lateralei stângi ({unit}): "))
        thickness["Right"] = float(input(f"Introduceți grosimea lateralei drepte ({unit}): "))

    return thickness


def get_unit_conversion_factor(unit):
    unit_conversion_factor = {"mm": 0.000001, "cm": 0.0001, "m": 1}
    return unit_conversion_factor.get(unit, 0.0001)  # Default to cm if unit is not recognized
