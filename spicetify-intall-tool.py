from subprocess import run
from shutil import rmtree
from time import sleep
from os import getlogin, path, system

config_folder = f"C:/Users/{getlogin()}/.spicetify"
cli_folder = f"C:/Users/{getlogin()}/spicetify-cli"
config_file = f"C:/Users/{getlogin()}/.spicetify/config-xpui.ini"

def clear():
    system("cls")

def start():
    if path.exists(cli_folder):
        installed = True
    else:
        installed = False
    
    clear()
    print("Spicetify installation tool\n")
    print("'I' -Install spicetify")
    print("'S' -Set up spicetify")
    print("'A' -Apply spicetify")
    print("'R' -Restore spotify")
    print("'U' -Update spicetify")
    print("'C' -Open config folder")
    print("'D' -Delete spicetify")
    print("'X' -Exit")
    user = input("\nChoose an action:\n")

    if user.lower() == "i":
        clear()
        print("Installing spicetify...\n")
        run('powershell.exe Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/khanhas/spicetify-cli/master/install.ps1" | Invoke-Expression')
        run("spicetify")
        run("spicetify backup apply enable-devtool")
        print("\nIf you didn't see any errors, that means spicetify was installed successfully!\n")
        input("Press any key to return to the menu...")
        start()
    elif user.lower() == "s":
        clear()
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start()
        print("This will install a couple of custom apps and extensions to get you started")
        print("The following extensions and custom apps will be installed:")
        print("PopupLyrics, FullAppDisplay, Lyrics-plus, New-releases, spicetify marketplace")
        input("\nPress any key to continue...")
        run("spicetify config extensions popupLyrics.js")
        run("spicetify config extensions fullAppDisplay.js")
        run("spicetify config custom_apps lyrics-plus")
        run("spicetify config custom_apps new-releases")
        run('powershell.exe Invoke-WebRequest -UseBasicParsing "https://raw.githubusercontent.com/CharlieS1103/spicetify-marketplace/master/install.ps1" | Invoke-Expression')
        run("spicetify apply")
        print("\nIf you didn't see any errors, all extensions and custom apps are installed successfully!")
        input("\nPress any key to return to the menu...")
        start()
    elif user.lower() == "a":
        clear()
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start()
        print("Applying...\n")
        run("spicetify apply")
        print("\nApplied successfully!\n")
        input("Press any key to return to the menu...")
        start()
    elif user.lower() == "r":
        clear()
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start() 
        print("Restoring spicetify...\n")
        run("spicetify restore")
        print("\nRestored successfully!\n")
        input("Press any key to return to the menu...")
        start()
    elif user.lower() == "u":
        clear()
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start() 
        print("Updating spicetify...\n")
        run("Spicetify upgrade")
        print("\nupdated successfully!\n")
        input("Press any key to return to the menu...")
        start()
    elif user.lower() == "c":
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start() 
        run("spicetify config-dir")
        start()
    elif user.lower() == "d":
        clear()
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start() 
        print("\nAre you sure you want to remove all contents of spicetify?")
        print("Yes")
        print("No")
        user = input()
        if user.lower() == "yes":
            print("WARNING!")
            print("This will REMOVE ALL your custom apps, extensions and themes!")
            print(f"It is recommended to back up the '.spicetify' folder located at 'C:/Users/{getlogin()}/.spicetify'")
            input("\nPress any key to continue...")
            run("spicetify restore")
            rmtree(cli_folder)
            rmtree(config_folder)
            print("Spicetify has been successfully removed")
            print("To complete the removal process, please reinstall spotify")
            input("\nPress any key to return to the menu...")
            start()
        else:
            print("Cancelling...")
            sleep(0.5)
            start()
    elif user.lower() == "x":
        clear()
        print("Closing...")
        sleep(0.5)
        quit()
    else:
        start()

start()