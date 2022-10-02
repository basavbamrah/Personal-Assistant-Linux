import os
from textwrap import wrap
import multiprocessing
from tkinter import *
from tkinter import font
from tkinter.scrolledtext import *
from voice import VoiceGtts


class Window:
    def __init__(self):
        self.text = None
        self.vg = VoiceGtts()

    def speak(self):

        self.p1 = multiprocessing.Process(
            target=self.vg.text_to_speech, args=(self.text,))
        self.p1.start()

    def print_text(self, text="nothing specified"):
        self.text = text

        window = Tk()
        window.geometry('400x395')
        button = Button(window, text="Read Out", command=self.speak)
        button.place(relx=0.20, rely=0.01)
        button = Button(window, text="Stop Read",
                        command=lambda: self.p1.terminate())
        button.place(relx=0.50, rely=0.01)
        window.wm_title("Scroll From Bottom")

        TextBox = ScrolledText(window, wrap=WORD, height='20', width='45')
        TextBox.place(relx=0.02, rely=0.1)

        TextBox.insert(END, self.text)
        # Pushes the scrollbar and focus of text to the end of the text input.
        # TextBox.yview(END)
        window.mainloop()
        try:
            self.p1.terminate()
            os.remove('./voice.mp3')
        except:
            pass

    def todo(self):
        root = Tk()
        root.geometry('500x500')
        root.resizable(0, 0)
        root.title("Bella's Todo List")
        root.config(bg='#0860c2')
        #
        # heading label
        Label(root, text="Todo List", bg='#0860c2', font=(
            'Times New Roman', 19), wraplength=300).place(relx=0.4, rely=0.01)

        tasks = Listbox(root, selectbackground='Gold', bg='#dcecff', font=(
            'Times New Roman', 14, 'italic', 'bold'), height=15, width=50)

        scroller = Scrollbar(root, orient=VERTICAL, command=tasks.yview)
        scroller.place(relx=0.8999, rely=0.07, height=350)

        tasks.config(yscrollcommand=scroller.set)
        tasks.place(relx=0.03, rely=0.07)

        with open('tasks.txt', 'r+') as tasks_list:
            for task in tasks_list:
                tasks.insert(END, task)
            tasks_list.close()

        # entry fields
        new_item_entry = Entry(root, width=50)
        new_item_entry.place(relx=0.03, rely=0.8)

        add_btn = Button(root, text='Add Item', bg='Azure', width=10, font=('Times New Roman', 12),
                         command=lambda: self.add_item(new_item_entry, tasks))

        add_btn.place(relx=0.15, rely=0.88)
        delete_btn = Button(root, text='Delete Item', bg='Azure', width=10, font=('Times New Roman', 12),
                            command=lambda: self.delete_item(tasks))
        delete_btn.place(relx=0.45, rely=0.88)

        root.mainloop()

    def add_item(self, entry: Entry, listbox: Listbox):
        new_task = entry.get()
        listbox.insert(END, new_task)
        with open(r'./tasks.txt', 'a') as fl:
            fl.write(f'{new_task}\n')
        fl.close()

    def delete_item(self, listbox: Listbox):
        print(listbox.get(ACTIVE))
        with open(r'./tasks.txt', 'r') as fl:
            lines = fl.readlines()

            print(lines)
            for i in lines:
                print(i.strip())
                if listbox.get(ACTIVE) == i.strip():
                    lines.remove(i)
        fl.close()
        # print(lines)
        with open(f'./tasks.txt', 'w')as fl:
            fl.writelines(lines)
        listbox.delete(ACTIVE)

    def disp_article(self, lst):
        root = Tk()
        # w = root.winfo_screenwidth()
        # h = root.winfo_screenheight()
        w = 670
        h = 435
        root.title("NEWS")
        root.geometry(f'{w}x{h}')
        root.configure(bg='#fcf3cf')  # fff1e5
        # root.resizable(0, 0)

        TextBox = ScrolledText(root, wrap=WORD)  # , height=, width='60')
        TextBox.place(relx=0.01, rely=0.02)

        a = 1
        for i in lst:

            source = str(a)+". "+i['source']['name']+"\n"
            title = i['title']+"\n"
            url = i['url']+"\n"
            desc = i['description']+"\n\n"
            a += 1
            TextBox.insert(END, source)
            TextBox.insert(END, title)
            TextBox.insert(END, desc)
            # TextBox.yview(END)
        root.mainloop()
