import os
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring
from turtle import *
from os import system, startfile
from gtts import gTTS
from time import sleep
import win10toast

color_dict = {
    "red": "#FF3F5F",
    "orange": "#FF8A47",
    "yellow": "#FFDC51",
    "green": "#3AFF7F",
    "blue": "#00AEFF"
}

root = Tk()
root.title("Windows Tkinter Tool")
root.geometry("570x345")


def main():
    help_btn = Button(root, text="Help", bg="#00AEFF", command=wtt_help)
    help_btn.pack()

    explorer = Button(root, text="Open File Explorer", bg="#3AFF7F", command=open_epl)
    explorer.pack()

    del_file = Button(root, text="Delete File (from Python console)", bg="#FF3F5F", command=delete_file)
    del_file.pack()

    cmd = Button(root, text="Open CMD", bg="#FFDC51", command=open_cmd)
    cmd.pack()

    py_console = Button(root, text="Open Python Console", bg="#FF8A47", command=open_py_console)
    py_console.pack()

    new_file = Button(root, text="Create file (from Python console)", bg="#00AEFF", command=create_file)
    new_file.pack()

    cpedit_btn = Button(root, text="CopyPaste Editor", bg="#00AEFF", command=copy_paste_editor)
    cpedit_btn.pack()

    satisfy_btn = Button(root, text="Satisfy yourself", bg="#00AEFF", command=satisfy)
    satisfy_btn.pack()

    open_ps_btn = Button(root, text="Open PowerShell", bg="#FF8A47", command=open_ps)
    open_ps_btn.pack()

    open_ps_ise_btn = Button(root, text="Open PowerShell ISE", bg="#FF8A47", command=open_ps_ise)
    open_ps_ise_btn.pack()

    use_tts_btn = Button(root, text="Use English TTS (from Python Console)", bg="#00AEFF", command=use_tts)
    use_tts_btn.pack()

    change_win_geometry_btn = Button(root, text="Change Window Geometry (from Python Console)", bg="#00AEFF", command=change_geometry)
    change_win_geometry_btn.pack()
    
    open_file_btn = Button(root, text="Open File (from Python Console)", bg="#FFDC51", command=open_file)
    open_file_btn.pack()

    set_alarm_btn = Button(root, text="Set Alarm", bg=color_dict["blue"], command=set_alarm)
    set_alarm_btn.pack()
    mainloop()


def open_epl():
    startfile("explorer.exe")


def delete_file():
    file = str(input("File to delete (use \\ to indicate a subdirectory): "))
    system(f"takeown /f {file}")
    system(f"del {file}")


def open_cmd():
    startfile("C:\\Windows\\System32\\cmd.exe")


def open_py_console():
    startfile("py.exe")


def wtt_help():
    help_win = Tk()
    help_win.title("Windows Tkinter Tool Help")
    help_label = Label(help_win, text="Windows Tkinter Tool is a tool designed with Tkinter. Red color: Very high risk, Orange color: High risk, Yellow color: Medium risk, Green color: Low risk, Blue color: No risk.")
    help_label.pack()


def create_file():
    filename = str(input("Enter the filename: "))
    lines = int(input("Enter the number of lines: "))
    for i in range(1, lines + 1):
        line_input = str(input(f"Line {i}: "))
        if i < lines:
            with open(filename, 'a') as f:
                f.write(f"{line_input}\n")
        else:
            with open(filename, 'a') as f:
                f.write(line_input)


def copy_paste_editor():
    cpedit = Tk()
    cpedit.title("CopyPaste Editor")
    editor = ScrolledText(cpedit, width=95, height=30)
    editor.pack()


def satisfy():
    title("Satisfy")
    bgcolor("black")
    colors = ["red", "dark red"]
    for i in range(100000):
        hideturtle()
        speed(50000)
        color(colors[i % 2])
        forward(i + 1)
        right(360 / 4 - 0.1)
    done()


def open_ps():
    startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")


def open_ps_ise():
    startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell_ise.exe")


def use_tts():
    tts_in = gTTS(str(input("Enter the text you want to hear: ")))
    tts_in.save("tts_out.mp3")
    os.startfile("tts_out.mp3")


def change_geometry():
    w = int(input("Width: "))
    h = int(input("Height: "))
    root.geometry(f"{w}x{h}")


def open_file():
    filename = str(input("Enter filename (use \\\\ to indicate the subdirectory): "))
    startfile(filename)


def set_alarm():
    alarm_length = askstring("Input Alarm Length", "Enter how much the alarm will last (hh:mm:ss): ")
    alarm_hrs_mins_secs = alarm_length.split(":")
    alarm_hrs = int(alarm_hrs_mins_secs[0])
    alarm_mins = int(alarm_hrs_mins_secs[1])
    alarm_secs = int(alarm_hrs_mins_secs[2])
    toaster = win10toast.ToastNotifier()
    sleep((alarm_hrs * (60 ** 2)) + (alarm_mins * (60 ** 1)) + (alarm_secs * (60 ** 0)))
    toaster.show_toast("Alarm finished", "Alarm finished", duration=5)


if __name__ == "__main__":
    main()
