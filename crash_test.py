import tkinter as tk

def testmur(liste, x, y):
    """
    fonction qui test si la case visée est un mur ou non
    """

    taillecarre = 10
    print((x%30) + 30*(y%20), len(liste))
    if ((x * (-1)) > 0 or (y * (-1)) > 0):
        return True
    elif liste[(x%30) + 30*(y%20)] == "1":
        return True
    return False

def enter(event = None):
    global id
    id = button.after(1500, showtip)

def leave(event = None):
    if id:
        button.after_cancel(id)

def showtip():
    print(button.winfo_rootx(), button.winfo_rooty())
    print(testmur(lis,button.winfo_rootx(), button.winfo_rooty()))

lis = "100011000100000000001000010000000000000001000000000000000010001100000101000010000011010000000000000000000000000000000000000010000000000000001000110000000000000100000000101000000010000010000001010000001000000000000000100000000000100010010000001000000010000000100000000000000010000000010000000100000000000000001000000010010000010000010000000000100000000011000000000001110000100010110000000100010000000000000000000000000000000000000000000000000100000000000000000000010000100000000001000000100000000000000100000000001100001001000000100100000101000000000000000000100101000000000010000010000000000001000010"

root = tk.Tk()
root.title("La Guerre des Robots")


button = tk.Button(root, text = "test")
button.pack()

button.bind("<Enter>", enter)
button.bind("<Leave>", leave)


root.mainloop()
