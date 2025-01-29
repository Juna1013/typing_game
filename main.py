import tkinter as tk
from tkinter import messagebox
import sys
import time
import threading
import random
from question import QUESTION

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        master.geometry("400x300")
        master.title("Typing game")

        random.shuffle(QUESTION)

        self.index = 0

        self.correct_cnt = 0

        self.create_canvas()
        self.create_widgets()

        t = threading.Thread(target=self.timer)
        t.start()

        self.master.bind("<KeyPress>", self.type_event)

    def create_canvas(self):
        self.canvas = tk.Canvas(self, width=400, height=300, bg="lightblue")
        self.canvas.pack(fill="both", expand=True)

        self.canvas.create_text(200, 30, text="Typing Game", font=("Arial", 24, "bold"), fill="darkblue")
        self.canvas.create_oval(300, 200, 350, 250, fill="yellow", outline="orange")

        self.canvas.create_line(0, 260, 400, 280, fill="darkblue", width=3)
    
    def create_widgets(self):
        self.q_label = tk.Label(self.canvas, text="Question:", font=("",20), bg="lightblue")
        self.q_label.place(x=50, y=80)
        self.q_label2 = tk.Label(self.canvas, text=QUESTION[self.index], width=10, anchor="w", font=("",20), bg="lightblue")
        self.q_label2.place(x=180, y=80)
        self.ans_label = tk.Label(self.canvas, text="Answer:", font=("",20), bg="lightblue")
        self.ans_label.place(x=50, y=130)
        self.ans_label2 = tk.Label(self.canvas, text="", width=10, anchor="w", font=("",20), bg="lightblue")
        self.ans_label2.place(x=180, y=130)
        self.result_label = tk.Label(self.canvas, text="", font=("",20), bg="lightblue")
        self.result_label.place(x=50, y=180)

        self.time_label = tk.Label(self.canvas, text="", font=("",20), bg="lightblue")
        self.time_label.place(x=50, y=230)

    def type_event(self, event):
        if event.keysym == "Return":
            if self.q_label2["text"] == self.ans_label2["text"]:
                self.result_label.configure(text="正解！", fg="red")
                self.correct_cnt += 1
            else:
                self.result_label.configure(text="残念！", fg="blue")

            self.ans_label2.configure(text="")

            self.index += 1
            if self.index == len(QUESTION):
                self.flg = False
                self.q_label2.configure(text="Finish!")
                messagebox.showinfo("Result", f"Your score is {self.correct_cnt}/{self.index}\ntime is {self.second}s")
                sys.exit(0)
            self.q_label2.configure(text=QUESTION[self.index])

        elif event.keysym == "BackSpace":
            text = self.ans_label2["text"]
            self.ans_label2["text"] = text[:-1]

        else:
            self.ans_label2["text"] += event.keysym

    def timer(self):
        self.second = 0
        self.flg = True
        while self.flg:
            self.second += 1
            self.time_label.configure(text=f"経過時間：{self.second}s")
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    Application(master=root)
    root.mainloop()
