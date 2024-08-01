import tkinter as tk
from Vistas.FrmPrincipal import FrmPrincipal

if __name__ == "__main__":
    ventana = tk.Tk()
    app = FrmPrincipal(ventana)
    ventana.mainloop()
