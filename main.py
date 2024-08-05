import tkinter as tk
from tkinter import ttk
from furniture import Furniture
from utils import get_unit_conversion_factor


class FurnitureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Furniture Dimension Calculator - AdyMob Factory")
        self.set_window_size_and_center(700, 650)  # Set the window size and center it
        self.root.resizable(False, False)

        self.create_widgets()

    def set_window_size_and_center(self, width, height):
        # Calculate the center position
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Set the window size and position
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def create_widgets(self):
        # Set the background color to match the image provided
        self.bg_color = "#f2e5d7"

        self.fields_frame = tk.Frame(self.root, bg=self.bg_color, bd=5)
        self.fields_frame.place(relx=0.5, rely=0.4, anchor="center")

        self.entries = {}
        labels = ["Înălțime", "Lungime", "Lățime", "Grosime unică (opțional)",
                  "Grosimea topului", "Grosimea fundului",
                  "Grosimea lateralei stângi", "Grosimea lateralei drepte",
                  "Grosimea materialului din față", "Grosimea materialului din spate"]

        for i, label in enumerate(labels):
            tk.Label(self.fields_frame, text=label, bg=self.bg_color).grid(row=i, column=0, pady=5, padx=5, sticky="w")
            entry = ttk.Entry(self.fields_frame)
            entry.grid(row=i, column=1, pady=5, padx=5)
            self.entries[label] = entry

        self.entries["Înălțime"].focus_set()

        self.unit_var = tk.StringVar(value="cm")
        tk.Label(self.fields_frame, text="Unitate (mm, cm, m):", bg=self.bg_color).grid(row=len(labels), column=0,
                                                                                        pady=5, padx=5, sticky="w")
        self.unit_entry = ttk.Entry(self.fields_frame, textvariable=self.unit_var)
        self.unit_entry.grid(row=len(labels), column=1, pady=5, padx=5)

        self.top_between_sides = tk.BooleanVar(value=False)
        self.bottom_between_sides = tk.BooleanVar(value=False)

        tk.Checkbutton(self.fields_frame, text="Partea superioară merge între laturi?", variable=self.top_between_sides,
                       bg=self.bg_color).grid(row=len(labels) + 1, columnspan=2, pady=5, padx=5, sticky="w")

        self.calculate_button = ttk.Button(self.fields_frame, text="Calculează", command=self.calculate_dimensions)
        self.calculate_button.grid(row=len(labels) + 2, columnspan=2, pady=10)

        self.result_frame = tk.Frame(self.root, bg=self.bg_color, bd=5)
        self.result_frame.place(relx=0.5, rely=0.85, anchor="center")  # Adjusted position

        self.result_label = tk.Label(self.result_frame, text="", bg=self.bg_color, justify="left")
        self.result_label.pack()

        self.root.bind('<Return>', lambda event: self.focus_next_widget(event))
        self.root.bind('<Up>', lambda event: self.focus_previous_widget(event))
        self.root.bind('<Down>', lambda event: self.focus_next_widget(event))

    def focus_next_widget(self, event):
        event.widget.tk_focusNext().focus()
        return ("break")

    def focus_previous_widget(self, event):
        event.widget.tk_focusPrev().focus()
        return ("break")

    def calculate_dimensions(self):
        unit = self.unit_var.get()
        height = float(self.entries["Înălțime"].get())
        length = float(self.entries["Lungime"].get())
        width = float(self.entries["Lățime"].get())

        unique_thickness = self.entries["Grosime unică (opțional)"].get()
        if unique_thickness:
            unique_thickness = float(unique_thickness)
            thickness = {
                "Top": unique_thickness, "Bottom": unique_thickness,
                "Left": unique_thickness, "Right": unique_thickness
            }
        else:
            thickness = {
                "Top": float(self.entries["Grosimea topului"].get()),
                "Bottom": float(self.entries["Grosimea fundului"].get()),
                "Left": float(self.entries["Grosimea lateralei stângi"].get()),
                "Right": float(self.entries["Grosimea lateralei drepte"].get())
            }

        front_thickness = float(self.entries["Grosimea materialului din față"].get())
        back_thickness = float(self.entries["Grosimea materialului din spate"].get())

        top_between_sides = self.top_between_sides.get()
        bottom_between_sides = top_between_sides

        furniture = Furniture(height, length, width, thickness, front_thickness, back_thickness)
        sides = furniture.calculate_sides(top_between_sides, bottom_between_sides)
        total_area = furniture.calculate_material_needed(sides)

        unit_conversion_factor = get_unit_conversion_factor(unit)
        total_area_m2 = total_area * unit_conversion_factor

        result_text = "\nDimensiunile părților de tăiat:\n"
        for side, dimensions in sides.items():
            result_text += f"{side}: {dimensions[0]} {unit} x {dimensions[1]} {unit}\n"
        result_text += f"\nSuprafața totală a materialului necesar: {total_area_m2:.2f} m²"

        self.result_label.config(text=result_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = FurnitureApp(root)
    root.mainloop()
