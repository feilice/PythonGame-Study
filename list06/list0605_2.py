import tkinter

root = tkinter.Tk()
root.title("おみくじソフト")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()
gazou = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400, 300, iamge=gazou)
label = tkinter.Label(root, text="??", font("Times New Roman, 120"), bg="white")
label.place(X-380, y=60)
button = tkinter.Button(root, text="おみくじを引く")
font()