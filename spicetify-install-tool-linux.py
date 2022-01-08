from shutil import rmtree
from time import sleep
from os import getlogin, path, system

config_folder = f"home/{getlogin()}.config/.spicetify"
cli_folder = f"/home/{getlogin()}/spicetify-cli"

def clear():
    system("clear")

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
        print("Is spotify already installed on your system? (not installed with snap, for more info, visit the spicetify documentation")
        print("yes")
        print("no")
        user = input()
        if user.lower() == "yes":
            pass
        elif user.lower() == "no":
            print("This will install spotify using apt")
            print("If you dont have apt installed on your distro, please install it")
            print("Note: In order to install spotify you will have to enter your sudo password")
            system("curl -sS https://download.spotify.com/debian/pubkey_5E3C45D7B312C643.gpg | sudo apt-key add - ")
            system('echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
            system("sudo apt-get update && sudo apt-get install spotify-client")
        else:
            print("Invalid input")
            start()
        system("curl -fsSL https://raw.githubusercontent.com/khanhas/spicetify-cli/master/install.sh | sh")
        system(f"{cli_folder} spicetify")
        system(f"{cli_folder} spicetify backup apply enable-devtool")
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
        print("PopupLyrics, FullAppDisplay, Lyrics-plus, New-releases")
        input("\nPress any key to continue...")
        system(f"{cli_folder}/spicetify config extensions popupLyrics.js")
        system(f"{cli_folder}/spicetify config extensions fullAppDisplay.js")
        system(f"{cli_folder}/spicetify config extensions shuffle+.js")
        system(f"{cli_folder}/spicetify config custom_apps lyrics-plus")
        system(f"{cli_folder}/spicetify config custom_apps new-releases")
        system(f"{cli_folder}/spicetify apply")
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
        system(f"{cli_folder}/spicetify apply")
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
        system(f"{cli_folder}/spicetify restore")
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
        system(f"{cli_folder}/Spicetify upgrade")
        print("\nupdated successfully!\n")
        input("Press any key to return to the menu...")
        start()
    elif user.lower() == "c":
        if not installed:
            print("Spicetify is not installed, please install it")
            input("\nPress any key to return to the menu...")
            start() 
        system(f"{cli_folder}/spicetify config-dir")
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
            system(f"{cli_folder}/spicetify restore")
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