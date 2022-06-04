from tkinter import *

root=Tk()

root.title("flower")
root.geometry("600x400")

label_series = Label(root, text="fibonacci series is like ")
entry_no = Entry(root)
label_sum = Label(root, text="fibonacci sum is probably ")


def fibonacci():
    input = int(entry_no.get())
    first_no = 0
    second_no = 1
    sum2 = 0
    sum = 0
    counter = 1
    while (counter <= input):
        label_series["text"] += str(sum) + " "
        label_sum["text"] = "fibonic sum is le' " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
        sum2 = sum2 + sum
entry_no.pack()
btn = Button(root, text="Show series of fibon thing", command=fibonacci)
btn.pack()
label_series.pack()
label_sum.pack()
root.mainloop()