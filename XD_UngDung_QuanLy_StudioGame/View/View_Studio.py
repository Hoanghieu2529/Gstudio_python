import tkinter as tk
from tkinter import messagebox, simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from controllers import StudioFormController


class StudioForm:
    def __init__(self, master):
        self.frame = tk.Frame(master, bg="#f8f9fa")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.controllers = StudioFormController(self)
        self.controllers.create_info_section(self.frame)
        self.controllers.create_graph_section(self.frame)





if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quản lý Studio")
    root.geometry("800x600")
    app = StudioForm(root)
    root.mainloop()
