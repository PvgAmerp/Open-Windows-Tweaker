import tkinter as tk
import shutil
import os
import ctypes
import sys
import threading
import webbrowser
import subprocess

is_terminal_open = False
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def ToggleTerminal():
    global is_terminal_open
    if not is_terminal_open:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 1)
        is_terminal_open = True
    else:
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        is_terminal_open = False

def run_disk_cleanup():
    try:
        print("Starting Disk Cleanup...")
        subprocess.run(["cleanmgr"], check=True)
        print("Disk Cleanup completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def elevate_privileges():
    if not is_admin():
        print("Attempting to elevate privileges...")
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        except Exception as e:
            print(f"Failed to elevate privileges: {str(e)}")
            sys.exit(1)
        sys.exit(0)

#Remove/Install def

def InstallJava():
    link = "https://download.oracle.com/java/21/archive/jdk-21.0.3_windows-x64_bin.msi"

    webbrowser.open(link)

def InstallChrome():
    link = "https://www.google.com/chrome/"

    webbrowser.open(link)

def RemoveMicrosoftEdge():
    dir_path = 'C:/Program Files (x86)/Microsoft/Edge/Application'
    try:
        shutil.rmtree(dir_path)
        print(f"The directory {dir_path} and all its contents have been deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

def RemoveJava():
    dir_path = 'C:/Program Files/Java'
    try:
        shutil.rmtree(dir_path)
        print(f"The directory {dir_path} and all its contents have been deleted successfully.")
    except OSError as e:
        print(f"Error: {e.strerror} - {e.filename}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

#Threads

def InstallJavaThread():
    thread = threading.Thread(target=InstallJava)
    thread.start()

def InstallChromeThread():
    thread = threading.Thread(target=InstallChrome)
    thread.start()

def RemoveMicrosoftEdgeThread():
    thread = threading.Thread(target=RemoveMicrosoftEdge)
    thread.start()

def RemoveJavaThread():
    thread = threading.Thread(target=RemoveJava)
    thread.start()

#Windows Def

def InstallAppF():
    IA = tk.Toplevel(MainWindow)
    IA.resizable(False, False)
    IA.title("Install App")
    IA.geometry("1000x700+100+100")

    NoteText = tk.Label(IA, text="Note: The downloads for the items are from the official websites.", font=("Helvetica", 18))
    NoteText.place(x=100, y=600)

    InstallJavaButton = tk.Button(IA, text="Install Java (Latest)", font=("Helvetica", 18), command=InstallJavaThread)
    InstallJavaButton.place(x=50, y=50)

    InstallChromeButton = tk.Button(IA, text="Install Chrome", font=("Helvetica", 18), command=InstallChromeThread)
    InstallChromeButton.place(x=50, y=200)

    BackToMainButton = tk.Button(IA, text="Back", font=("Helvetica", 18), command=IA.destroy)
    BackToMainButton.place(x=450, y=500)

def RemoveAppF():
    RA = tk.Toplevel(MainWindow)
    RA.resizable(False, False)
    RA.title("Remove App")
    RA.geometry("1000x700+100+100")

    RemoveMicrosoftEdgeButton = tk.Button(RA, text="Remove Microsoft Edge", font=("Helvetica", 18), command=RemoveMicrosoftEdgeThread)
    RemoveMicrosoftEdgeButton.place(x=50, y=50)

    RemoveJavaButton = tk.Button(RA, text="Remove Java(All versions, do it if you have corrupted version of java.)", font=("Helvetica", 18), command=RemoveJavaThread)
    RemoveJavaButton.place(x=50, y=200)

    BackToMainButton = tk.Button(RA, text="Back", font=("Helvetica", 18), command=RA.destroy)
    BackToMainButton.place(x=450, y=500)

def MainMenu():
    global MainWindow
    MainWindow = tk.Tk()
    MainWindow.resizable(False, False)
    MainWindow.title("Open Window Tweaker")
    MainWindow.geometry("1000x700+100+100")

    RemoveApp = tk.Button(MainWindow, text="Remove an app", font=("Helvetica", 18), command=RemoveAppF)
    RemoveApp.place(x=380, y=100)

    DiskCleanup = tk.Button(MainWindow, text="Disk Cleanup (Windows Tool)", font=("Helvetica", 18), command=run_disk_cleanup)
    DiskCleanup.place(x=380, y=500)

    InstallApp = tk.Button(MainWindow, text="Install service/app", font=("Helvetica", 18), command=InstallAppF)
    InstallApp.place(x=380, y=300)

    ToggleTerminalOnOff = tk.Button(MainWindow, text="Toggle Terminal On/Off", font=("Helvetica", 18), command=ToggleTerminal)
    ToggleTerminalOnOff.place(x=700, y=650)

    MainWindow.mainloop()

if __name__ == "__main__":
    elevate_privileges()
    MainMenu()
