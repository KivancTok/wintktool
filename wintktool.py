import tkinter.simpledialog as tkdialog
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.simpledialog import askstring
from turtle import *
from os import system, startfile
from gtts import gTTS
from time import sleep
import playsound
import malcollect.forkbomb
import malcollect.plusram_041

colors = {
    "red": "#FF3F5F",
    "orange": "#FF8A47",
    "yellow": "#FFDC51",
    "green": "#3AFF7F",
    "blue": "#00AEFF"
}


def getcolor(name):
    return colors[name]


root = Tk()
root.title("Windows Tkinter Tool")
root.geometry("585x350")


editor: Tk
editor_body: Text
editor_menu: Menu
editor_file_dropdown: Menu
malc: Tk
malc_fbomb: Button
malc_pram: Button


def main():
    help_btn = Button(root, text="Help", bg=getcolor("blue"), command=BtnMethods.wtt_help)
    help_btn.pack()

    explorer = Button(root, text="Open File Explorer", bg=getcolor("green"), command=BtnMethods.open_epl)
    explorer.pack()

    del_file = Button(root, text="Delete File", bg=getcolor("red"), command=BtnMethods.delete_file)
    del_file.pack()

    cmd = Button(root, text="Open CMD", bg=getcolor("yellow"), command=BtnMethods.open_cmd)
    cmd.pack()

    py_console = Button(root, text="Open Python Console", bg=getcolor("orange"), command=BtnMethods.open_py_console)
    py_console.pack()

    wte = Button(root, text="WinTkEdit", bg=getcolor("blue"), command=BtnMethods.wte)
    wte.pack()

    satisfy_btn = Button(root, text="Satisfy yourself", bg=getcolor("blue"), command=BtnMethods.satisfy)
    satisfy_btn.pack()

    open_ps_btn = Button(root, text="Open PowerShell 1.0", bg=getcolor("orange"), command=BtnMethods.open_ps)
    open_ps_btn.pack()

    open_ps_ise_btn = Button(root, text="Open PowerShell ISE", bg=getcolor("orange"), command=BtnMethods.open_ps_ise)
    open_ps_ise_btn.pack()

    use_tts_btn = Button(root, text="Use English TTS", bg=getcolor("blue"), command=BtnMethods.use_tts)
    use_tts_btn.pack()

    change_win_geometry_btn = Button(root, text="Change Window Geometry", bg=getcolor("blue"), command=BtnMethods.change_geometry)
    change_win_geometry_btn.pack()

    open_file_btn = Button(root, text="Open File", bg=getcolor("blue"), command=BtnMethods.open_file)
    open_file_btn.pack()

    set_alarm_btn = Button(root, text="Set Alarm", bg=getcolor("blue"), command=BtnMethods.set_alarm)
    set_alarm_btn.pack()

    mal_btn = Button(root, text="Malware Collection (VM/Non-Primary Computer Only!)", bg=getcolor("red"), command=BtnMethods.malco)
    root.mainloop()


class BtnMethods:
    @staticmethod
    def delete_file():
        file = tkdialog.askstring("Delete", "File's full path to delete:")
        system(f"takeown /f {file} /d y")
        system(f"del {file}")

    @staticmethod
    def open_cmd():
        startfile("C:\\Windows\\System32\\cmd.exe")

    @staticmethod
    def open_epl():
        startfile("explorer.exe")

    @staticmethod
    def open_py_console():
        startfile("py.exe")

    @staticmethod
    def wtt_help():
        help_win = Tk()
        help_win.title("Windows Tkinter Tool Help")
        help_label = Label(help_win,
                           text="Windows Tkinter Tool is a tool designed with Tkinter. Red color: Very high risk, Orange color: High risk, Yellow color: Medium risk, Green color: Low risk, Blue color: No risk.")
        help_label.pack()

    @staticmethod
    def wte():
        global editor, editor_body, editor_menu, editor_file_dropdown
        editor = Tk()
        editor.title("WinTkEdit")
        editor_body = ScrolledText(editor, font=("Consolas", 16))
        editor_body.pack()

        editor_menu = Menu(editor)
        editor.config(menu=editor_menu)
        editor_file_dropdown = Menu(editor_menu)
        editor_menu.add_cascade(label="File", menu=editor_file_dropdown)
        editor_file_dropdown.add_command(label="Save", command=BtnMethods.WTEMethods.save)
        editor_file_dropdown.add_command(label="Open", command=BtnMethods.WTEMethods.open)
        editor_file_dropdown.add_separator()
        editor_file_dropdown.add_command(label="Exit", command=BtnMethods.WTEMethods.wteexit)
        editor.mainloop()

    class WTEMethods:
        @staticmethod
        def save():
            path = tkdialog.askstring("Save", "Full file path:")
            with open(path, "w") as f:
                f.write(editor_body.get("1.0", "end"))

        @staticmethod
        def open():
            path = tkdialog.askstring("Open", "Full file path:")
            with open(path, "r") as f:
                editor_body.delete("1.0", "end")
                editor_body.insert("end", f.read())

        @staticmethod
        def wteexit():
            editor.destroy()

    @staticmethod
    def satisfy():
        title("Satisfy")
        bgcolor("black")
        cls = ["red", "dark red"]
        for i in range(100000):
            hideturtle()
            speed(50000)
            color(cls[i % 2])
            forward(i + 1)
            right(360 / 4 - 0.1)
        done()

    @staticmethod
    def open_ps():
        startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe")

    @staticmethod
    def open_ps_ise():
        startfile("C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell_ise.exe")

    @staticmethod
    def use_tts():
        tts_in = gTTS(tkdialog.askstring("TTS", "Enter the text you want to hear:"))

        tts_in.save("tts_out.mp3")
        playsound.playsound("tts_out.mp3")

    @staticmethod
    def change_geometry():
        wh = tkdialog.askstring("Change Geometry", "Enter width and height in wxh format:")
        w, h = wh.split("x")

        root.geometry(f"{w}x{h}")

    @staticmethod
    def open_file():
        filename = str(input("Enter filename (use \\\\ to indicate the subdirectory): "))
        startfile(filename)

    @staticmethod
    def set_alarm():
        alarm_length = askstring("Input Alarm Length", "Enter how long the alarm will last (hh:mm:ss): ")
        alarm_hrs_mins_secs = alarm_length.split(":")
        alarm_hrs, alarm_mins, alarm_secs = alarm_hrs_mins_secs
        alarm_hrs, alarm_mins, alarm_secs = int(alarm_hrs), int(alarm_mins), int(alarm_secs)
        sleep((alarm_hrs * (60 ** 2)) + (alarm_mins * (60 ** 1)) + (alarm_secs * (60 ** 0)))
        playsound.playsound("alarm.mp3")

    @staticmethod
    def malco():
        global malc, malc_fbomb, malc_pram
        malc = Tk()
        malc_fbomb = Button(malc, text="Forkbomb", command=malcollect.forkbomb.run)
        malc_pram = Button(malc, text="+RAM 0.4.1", command=malcollect.plusram_041.start)


if __name__ == "__main__":
    main()
