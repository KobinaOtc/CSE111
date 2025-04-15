import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()

def populate_main_window(frm_main):

    lbl_width = Label(frm_main, text="Enter the width in cm:")

    # Create an integer entry box where the user will enter the width.
    ent_width = IntEntry(frm_main, width=4)


    lbl_height = Label(frm_main, text="Enter the height in cm:")

    # Create an integer entry box where the user will enter the height.
    ent_height = IntEntry(frm_main, width=4)

    # create a label for the result
    lbl_areas = Label(frm_main, text="Area:")
    lbl_area_end = Label(frm_main, text="cm^2")
    lbl_width_len = Label(frm_main, text="cm")
    lbl_height_len = Label(frm_main, text="cm")

    lbl_area = Label(frm_main, width=4)

    lbl_error = Label(frm_main, width=15)

    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(row=0, column=0, padx=1, pady=3)
    ent_width.grid(row=0, column=1, padx=1, pady=3)
    lbl_width_len.grid(row=0, column=2, padx=1, pady=1)

    lbl_height.grid(row=0, column=3, padx=3, pady=3)
    ent_height.grid(row=0, column=4, padx=3, pady=3)
    lbl_height_len.grid(row=0, column=5, padx=1, pady=1)

    lbl_areas.grid(row=1, column=0, padx=3, pady=3)
    lbl_area.grid(row=1, column=1, padx=3, pady=3)
    lbl_area_end.grid(row=1, column=2, padx=3, pady=3)
    btn_clear.grid(row=2, column=0, padx=3, pady=3)
    lbl_error.grid(row=3, column=1, padx=3, pady=3)

    def calculate(event):

        try:
            width = ent_width.get()
            height = ent_height.get()

            area = width * height

            lbl_area.config(text=f"{area:.0f}")
            if area > 0:
                lbl_error.config(text='')
        except UnboundLocalError:
            lbl_error.config(text="Type a number in each field")
        except ValueError:
            lbl_error.config(text="Check your values")

    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_height.clear()
        lbl_area.config(text="")
        ent_width.focus()
        ent_height.focus()
        # lbl_error.focus()

    btn_clear.config(command=clear)

    ent_width.bind("<KeyRelease>", calculate)
    ent_height.bind("<KeyRelease>", calculate)
    lbl_error.bind("<KeyRelease>", calculate)
if "__main__" == __name__:
    main()