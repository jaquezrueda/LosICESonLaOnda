from Tkinter import *
import subprocess
import os
from multiprocessing import Process

window = Tk()
lb = Listbox(window, width=90, height=50)


def create_child():
    os.fork()

def create_subprocess():
    subprocess.call(['python /Users/PycharmProjects/CC406/childs/Main.py'])

def os_system():
    os.system("python /Users/PycharmProjects/CC406/childs/Main.py")


def create_list_process():
    p = Process(target=create_list)
    p.start()
    p.join()

def create_list():
    lb.delete(1,END)
    p1 = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(['grep', 'Main.py'], stdin=p1.stdout, stdout=subprocess.PIPE)

    processes = p2.communicate()[0].split('\n')

    for row in processes:
        lb.insert(END, row.replace("jesusjaquezrueda", "").replace("/System/Library/Frameworks/Python.framework/Versions/2.7/Resources/Python.app/Contents/MacOS/Python", ""))



button_fork = Button(window, text="Fork", command=create_child)
button_subprocess = Button(window, text="Subprocess", command=create_subprocess)
button_refresh = Button(window, text="Refresh", command=create_list)
button_refresh_process = Button(window, text="Refresh with process", command=create_list_process)


create_list()
lb.pack(side=RIGHT)
button_fork.pack(side=LEFT)
button_refresh.pack(side=LEFT)
button_subprocess.pack(side=LEFT)
button_refresh_process.pack(side=LEFT)
mainloop()