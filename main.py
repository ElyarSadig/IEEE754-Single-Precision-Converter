import tkinter
from tkinter import ttk
from IEEE754 import compute


class Binary(object):
    def __init__(self):
        self.entry_for_binary = None
        self.label_for_binary = None


def main():
    binary = Binary()

    root = tkinter.Tk()
    root.title('IEEE754(single precision)')

    frame = ttk.Frame(root, padding=20)
    frame.grid()

    label1 = ttk.Label(frame, text='Enter a float number')
    label1.grid()

    entry = ttk.Entry(frame, width=20)
    entry.grid()
    binary.entry_for_binary = entry

    label = ttk.Label(frame)
    label.grid()
    binary.label_for_binary = label

    button1 = ttk.Button(frame, text='Compute IEEE754')
    button1.grid()
    button1['command'] = lambda: float_to_binary(binary)

    button2 = ttk.Button(frame, text='Quit')
    button2.grid()
    button2['command'] = lambda: quit()

    root.mainloop()


def float_to_binary(binary):
    entry = binary.entry_for_binary
    contents_of_entry_box = entry.get()
    num = float(contents_of_entry_box)
    answer = compute(num)
    binary.label_for_binary['text'] = answer


main()

