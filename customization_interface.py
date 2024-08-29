import tkinter as tk

class CustomizationInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Clothing Customization")
        
        self.label = tk.Label(master, text="Select Clothing Options")
        self.label.pack()
        
        self.sleeve_var = tk.StringVar(value="Short")
        self.sleeve_label = tk.Label(master, text="Sleeve Length:")
        self.sleeve_label.pack()
        self.sleeve_options = tk.OptionMenu(master, self.sleeve_var, "Short", "Medium", "Long")
        self.sleeve_options.pack()

        self.submit_button = tk.Button(master, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        print(f"Sleeve Length Selected: {self.sleeve_var.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    interface = CustomizationInterface(root)
    root.mainloop()
