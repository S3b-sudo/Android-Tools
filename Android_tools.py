from rich import print
from rich.console import Console
import os
import subprocess

#Console init
console = Console()

#Pairing
ip = "null"
port = "null"
p_code = "null"

#Connecting
ip_connect = "null"
port_connect = "null"

#File Downloading
target_file = "null"
location_file = "~/Downloads"

#File updating
File_to_push = "null"
location_of_drop = "/sdcard/Download/"

#Settings editing
name_space = "null"
key = "null"
value = "null"

ERR_check = "null"

while True:
    print("""[green]                                   =                            =                                   
                                   ==                          ==                                   
                                    ==                        ==                                    
                                     ==     =============    =                                      
                                      ========================                                      
                                   ==============================                                   
                                 ==================================                                 
                                ====================================                                
                              ========   ==================   ========                              
                             ========    ==================    ========                             
                            ============================================                            
                            ============================================                            
                           ==============================================                           
                           ==============================================                           
                           ==============================================                           """)
    print(" ")
    print("[bold][green]=======================================================================================================")
    print("""[green] █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ███████╗
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║██║  ██║       ██║   ██║   ██║██║   ██║██║     ╚════██║
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝""")
    print("[bold][green]=======================================================================================================")
    print("[bold][green]           Quick tools for ADB including screen copy, Android recovery and much much more.")
    print("[bold][green]=======================================================================================================")
    print("[bold][green]Simple to use tools [yellow]                   Some what advanced tools[red]                           Advanced tools")
    print("[bold][green]=======================================================================================================")
    print("[bold][green]Connection tools: =====================================================================================")
    print("[green](1) Connect to a Device") #Add error handling [X]
    print("[green](2) Pair a New Device") #Add error handling [X]
    print("[green](3) Show currently connected device") #Error handling impossible
    print("[green](4) Disconect from device")
    print("[bold][green]Tools: =================================================================================================")
    print("[green](5) Use Scrcpy (remote)") 
    print("[yellow](6) Reboot device to recovery - WILL DISCONNECT TARGET") #Add error handling [X]
    print("[red](7) Run a shell instence on the Android Device") #Impossible to add error handling [X]
    print("[yellow](8) File Management") #Add error handling [X]
    print("[yellow](9) Advanced device info") 
    print("[green](10) Emulate key strokes") #Still needs to be made [X
    print("[yellow](11) Application manager") #Error handling has been fully added to this catagory [X]
    print("[green](12) Change System Settings / Misc")
    print("[green](13) Shizuku startup") #Done
    print("[green](14) Set Launcher as Pixel Launcher")
    print("[green](15) [yellow]Set [blue]Launcher [red]as [blue]Troll [red]Launcher")
    print("(16) Exit")
    
    coice = input("Choose a nomber: ")
    #Connecting to a device through wifi (Pairing) or wire
    if coice == "1":
        
        os.system("clear")
        print("How will you be connecting this device?")
        print("(1) Wirelessly (Requires paring a new device first if you havnt already)")
        print("(2) With a wire")
        print("(3) Back")
        while True:
            c1 = input("Choose a nomber: ")

            if c1 == "1":    
                os.system("clear")
                print("Do you know how to open the Wireless Debugging options menue?")
                print("(1) Yes")
                print("(2) No")
                while True:

                    cc1 = input("Choose a nomber: ")

                    if cc1 == "1":
                        break

                    if cc1 == "2":
                        os.system("clear")
                        print("[green] Advanced users: Settings > Developer Mode > Wireless Debugging")
                        print("Step 1: Open the settings app on your Android device.")
                        input("(Return) I have opened the settings app: ")
                        print("====================================================================================================")
                        print("Step 2: Go to about device")
                        input("(Return) I have opened about device: ") 
                        print("====================================================================================================")
                        print("Step 3: Find the build nomber and tap it 7 times (or untill prompted to enter your screen lock).")
                        input("(Return) I have been prompted: ")
                        print("====================================================================================================")
                        print("Step 4: Open developer options and enable wireless debugging and expand the options for it")
                        input("(Return) Wireless debugging is enabled and i have expanded the options: ")
                        print("====================================================================================================")
                        print("[green]Congradulations!!!!!! You finished the tutorial, time to connect.")
                        print("[yellow][bold]Remember: If you didnt pair your device first, do that or this section will fail.")
                        input("Press return to enter connection setup: ")
                        os.system("clear")
                        break

                print("=============================================================================================================================================")
                print("      All information for this section is found at the top of the expanded wireless debugging settings window under [yellow] IP & Port")
                print("=============================================================================================================================================")
                print("IP format: [green][bold]111.111.1.11[red]:111111")
                print("[green]Type this [red]Dont type this")
        
                ip_connect = input("Enter the Devices IP adress: ")
        
                print("Port format: [red][bold]111.111.1.11:[green]111111")
                port_connect = input("Enter the Devices Port: ")
        
                os.system(f"./res/scrcpy/adb connect {ip_connect}:{port_connect}")
                input("Press returen to go back to the menue: ")
                os.system("clear")
                
                break

            if c1 == "2":
                
                os.system("clear")
                print("Do you know how to enable USB Debugging options menue?")
                print("(1) Yes")
                print("(2) No")
                while True:
                    wc1 = input("Choose a nomber: ")

                    if wc1 == "1":
                        break

                print("========================================================================")
                print("Ensure that usb debugging is enabled and plug the device into one of the")
                print("USB ports on the machene using a cable that is capable of transfering   ")
                print("data.")
                print("========================================================================")
                input("Press return when you see and pressed allow on any popup windows for data transfer or USB debugging: ")
                print("========================================================================")
                os.system("./res/scrcpy/adb devices -l")
                print("========================================================================")
                print("If your device is listed here, you are sucessfully connected.")
                print("If not, try connecting wirelessly or try this method again.")
                input("Press return to go back to menue: ")
                break
                

            if c1 == "3":
                os.system("clear")
                break
    #Handles paring for wireless debugging
    if coice == "2":
        
        os.system("clear")
        print("Do you know how to open the Wireless Debugging options menue?")
        print("(1) Yes")
        print("(2) No")
        while True:
            cc2 = input("Choose a nomber: ")

            if cc2 == "1":
                break

            if cc2 == "2":
                        os.system("clear")
                        print("[green] Advanced users: Settings > Developer Mode > Wireless Debugging")
                        print("Step 1: Open the settings app on your Android device.")
                        input("(Return) I have opened the settings app: ")
                        print("====================================================================================================")
                        print("Step 2: Go to about device")
                        input("(Return) I have opened about device: ") 
                        print("====================================================================================================")
                        print("Step 3: Find the build nomber and tap it 7 times (or untill prompted to enter your screen lock).")
                        input("(Return) I have been prompted: ")
                        print("====================================================================================================")
                        print("Step 4: Open developer options and enable wireless debugging and expand the options for it")
                        input("(Return) Wireless debugging is enabled and i have expanded the options: ")
                        print("====================================================================================================")
                        print("[green]Congradulations!!!!!! You finished the tutorial, time to connect.")
                        print("[yellow][bold]Remember: If you didnt pair your device first, do that or this section will fail.")
                        input("Press return to enter connection setup: ")
                        os.system("clear")
                        break
        
        os.system("clear")

        while True:
              print("How would you like to connect?")
              print("(1) Pairing code")
              print("(2) QR code")
              test = input("Choose a nomber: ")

              if test == "1":
                    print("cool")
                    print("===========================================================================================================================")
                    print("  All of the Information for this is found when hitting the[yellow] Pair With Paring code Button in wireless debugging")
                    print("===========================================================================================================================")
                    print("[green]Type this [red]Dont type this")
                    print("IP format: [green][bold]111.111.1.11[red]:111111")
                    ip = input("Enter the Devices IP adress: ")

                    print("Port format: [red][bold]111.111.1.11:[green]111111")
                    port = input("Enter the Devices Port: ")

                    print("Paring code: The bold nombers in the box")
                    p_code = input("Enter the Devices Paring code: ")

                    os.system(f"./res/scrcpy/adb pair {ip}:{port} {p_code}")
                    input("Press returen to go back to menue: ")
                    os.system("clear")
                    break
              
              if test == "2":
                    os.system("python3 qr.py")
                    input("Press return to go back to menu: ")
                    os.system("clear")
                    break
                    
    #Lists all devices currently connected through ADB
    if coice == "3":
        os.system("clear")
        os.system("./res/scrcpy/adb devices -l")
        input("Press return to continue: ")
        os.system("clear")
    #Disconnect All Devices
    if coice == "4":
          os.system("./res/scrcpy/adb disconnect")
          print("[green]==========================================================")
          print("[green]               Disconnected Sucessfully")
          print("[green]==========================================================")
          input("Press return to continue: ")   
    #Starts screen copy for remote
    if coice == "5":
        print("Starting Scrcpy...")
        #os.system("scrcpy")
        subprocess.run("./res/scrcpy/scrcpy")
        print("Screen copy session stopped")
        input("Press return to go back to menue: ")
        os.system("clear")
    #Reboot target device to recovery
    if coice == "6":
      print("[red]WARNING: This will dissconnect the target device.")
      input("Press return to continue: ")
      
      try: 
          with console.status("[bold green]Rebooting into recovery...") as status:
            result = subprocess.run(["./res/scrcpy/adb", "reboot", "recovery"], capture_output=True, text=True, check=True)
            print("[green]Output:", result.stdout)
            print("[red]Errors:", result.stderr)
                                   
      except subprocess.CalledProcessError as e:
          print(f"Command failed with return code {e.returncode}")
          print("Error output:", e.stderr)
          print("[red]===================================================================")
          print("[red]     An Error Ocured: Plese connect a device before continuing     ")
          print("[red]===================================================================")
          input("Press return to exit the application because i dont know how to fix the oncomming error :) : ")
          os.system("clear")
          break
                                   
      if result.stderr == "":
          print("[green]===================================================================")
          print("[green]                    Command sent to device                         ")
          print("[green]===================================================================")
          input("Press return to go back to menu: ")
          os.system("clear")
          
      else:
          print("[red]===================================================================")
          print("[red]             An Error Ocured: See Above for Details                ")
          print("[red]===================================================================")
          input("Press return to continue: ")
          os.system("clear")
          
    #Run's a shell instence on the target device (Can be used for data extraction and file management)
    if coice == "7":
         os.system("./res/scrcpy/adb shell")
    #FIle management
    if coice == "8":
         while True: 
            print("=====================================================================")
            print("                   What would you like to do?                        ")
            print("=====================================================================")
            print("[yellow]Note: Error handling is not supported in this part of the application.")
            print("(1) Download a file or folder from the device")
            print("(2) Upload a file or folder to the device")
            print("(3) Go back to main menue")
            ft = input("Choose a nomber: ")
            #Pulling files
            if ft == "1": 
                 print("=====================================================================")
                 print("[yellow]Example Directories: /sdcard/Download - /sdcard/Documents - /sdcard/DCIM - /sdcard/Pictures")
                 target_file = input("Full android path to the file you wish to download: ")
                 while True:
                      print(" ")
                      print("[green]=====================================================================")
                      print("[green]           Where would you like the file to be saved?                 ")
                      print("[green]=====================================================================")
                      print("(1) Downloads folder")
                      print("(2) Custum Directory (Full Path Required)")
                      cc111 = input("Choose a nomber: ")

                      if cc111 == "1":
                        os.system(f"./res/scrcpy/adb pull {target_file} {location_file}")
                        print("[green]===================================================================")
                        print("[green]               File pull command has completed                     ")
                        print("[green]===================================================================")
                        input("Press return to go back to menu: ")
                        os.system("clear")
                        break
                        
                      
                      if cc111 == "2":                 
                           location_file = input("Full path of the location you wish to save the files: ")
                           os.system(f"./res/scrcpy/adb pull {target_file} {location_file}")
                           print("[green]===================================================================")
                           print("[green]               File pull command has completed                     ")
                           print("[green]===================================================================")
                           input("Press return to go back to menu: ")
                           os.system("clear")
                           break
            
            #Pushing files
            if ft == "2":
                 print("=====================================================================")  
                 File_to_push = input("Enter the full path of the file or folder you wish to send to the target device: ")
                 while True:
                      print("=====================================================================")
                      print("          Where do you want this file on the target device?          ")
                      print("=====================================================================")
                      print("(1) Downloads folder")
                      print("(2) Custum Directory (Full Path Required)")
                      send111 = input("Choose a nomber: ")

                      if send111 == "1":
                           os.system(f"./res/scrcpy/adb push {File_to_push} {location_of_drop}")
                           print("[green]=====================================================================")
                           print("[green]                 File push command has completed                     ")
                           print("[green]=====================================================================")
                           input("Press return to go back: ")
                           os.system("clear")
                           break
                    
                      if send111 == "2":
                           print("=====================================================================")
                           location_of_drop = input("Full android path of the location you wish to save the file: ")
                           os.system(f"./res/scrcpy/adb push {File_to_push} {location_of_drop}")
                           print("[green]=====================================================================")
                           print("[green]                File push command has completed                     ")
                           print("[green]=====================================================================")
                           input("Press return to go back: ")
                           os.system("clear")
                           break
            #Quitting
            if ft == "3":
                 os.system("clear")
                 break
         
    #Grabbs advanced info like sensor data, accounts, wifi, and more.
    if coice == "9":
         while True:
              
            print("==================================================================================")
            print("           Which of the following options would you like to use?                  ")
            print("==================================================================================")
            print("(1) Show everything happining on th device in real time through logs")
            print("(2) See live networking data")
            print("(3) dumpsys meminfo - See information reguarding the RAM of the device")
            print("(4) dumpsys sensorservice - See info drom things like the jiroscope and ALS of the device")
            print("(5) dumpsys mount - See all mounted disks of the device")
            print("(6) dumpsys power - See battery related information of the device")
            print("(7) dumpsys location - See location based information of the device")
            print("(8) dumpsys notification - See all current and dismissed notifications of the device")
            print("(9) dumpsys lock_settings - See lockscreen settings of the device")
            print("(10) dumpsys stats - See system status")
            print("(11) dumpsys batterystats - See battery status")
            print("(12) dumpsys usb - See previousoly connected usb devices")
            print("(13) See all apps installed on the device") # Move app listing function to advanced data tab
            print("(14) Back to the main menue")

            di = input("Choose a nomber: ")

            if di == "1":
                 print("[red][bold]WARNING: This script runs forever until it is manually stopped. Press Ctrl+C to stop it")
                 input("(Return)I understand: ")
                 os.system("./res/scrcpy/adb logcat -v color")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "2":
                    print("[red][bold]WARNING: This script runs forever until it is manually stopped. Press Ctrl+C to stop it")
                    input("(Return)I understand: ")
                    os.system("./res/scrcpy/adb logcat -b radio -v color")
                    print("==================================================================================")
                    print("                      Opporation Completed Successfully                           ")
                    print("==================================================================================")
                    input("(Reruen) Show dumpsys data, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
                    os.system("./res/scrcpy/adb shell dumpsys wifi")
                    print("==================================================================================")
                    print("                      Opporation Completed Successfully                           ")
                    print("==================================================================================")
                    input("(Reruen) Go back to main menue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "3":
                 os.system("./res/scrcpy/adb shell dumpsys meminfo")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "4":
                 os.system("./res/scrcpy/adb shell dumpsys sensorservice")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
            
            if di == "5":
                 os.system("./res/scrcpy/adb shell dumpsys mount")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "6":
                 os.system("./res/scrcpy/adb shell dumpsys power")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "7":
                 os.system("./res/scrcpy/adb shell dumpsys location")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "8":
                 #os.system("adb shell dumpsys notification") 
                 os.system("./res/scrcpy/adb shell dumpsys notification")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) See ticker text, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
                 print("==================================================================================")
                 os.system("./res/scrcpy/adb shell dumpsys notification --noredact | grep ticker")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) See text of sum notifications, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
                 os.system("./res/scrcpy/adb shell dumpsys notification --noredact | grep extras")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
            
            if di == "9":
                 os.system("./res/scrcpy/adb shell dumpsys lock_settings")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "10":
                 os.system("./res/scrcpy/adb shell dumpsys stats")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")
            
            if di == "11":
                 os.system("./res/scrcpy/adb shell dumpsys batterystats")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "12":
                 os.system("./res/scrcpy/adb shell dumpsys usb")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "13":
                 os.system("./res/scrcpy/adb shell pm list packages")
                 print("==================================================================================")
                 print("                      Opporation Completed Successfully                           ")
                 print("==================================================================================")
                 input("(Reruen) Go back to meue, (Highlight + Ctrl+Shift+V) Save the output into another program via the clipbord")

            if di == "14":
                 os.system("clear")
                 break
    #Key Stroke Emulation
    if coice == "10":
          while True:
                print("======================================================================")
                print("          Select a key stroke that you would like to emulate          ")
                print("======================================================================")
                print("(1) Home button")
                print("(2) Back button")
                print("(3) Power button")
                print("(4) Open Camara")
                print("(5) Raise Brightness")
                print("(6) Lower Brightness")
                print("(7) Volume up")
                print("(8) Volume down")
                print("(9) Back to menue")
                ks = input("Choose a nomber: ")

                if ks == "1":
                      os.system("./res/scrcpy/adb shell input keyevent 3")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")
                if ks == "2":
                      os.system("./res/scrcpy/adb shell input keyevent 4")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "3":
                      os.system("./res/scrcpy/adb shell input keyevent 26")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "4":
                      os.system("./res/scrcpy/adb shell input keyevent 27")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "5":
                      os.system("./res/scrcpy/adb shell input keyevent 221")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "6":
                      os.system("./res/scrcpy/adb shell input keyevent 220")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "7":
                      os.system("./res/scrcpy/adb shell input keyevent 24")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")                      
                if ks == "8":
                      os.system("./res/scrcpy/adb shell input keyevent 25")
                      print("======================================================================")
                      print("                      Keystroke command sent                          ")
                      print("======================================================================")
                      input("Press return to go back to the menue: ")
                      os.system("clear")
                if ks == "9":
                      os.system("clear")
                      break                      
          
    #App management
    if coice == "11":
         while True:
              print("===================================================================")
              print("                  What would you like to do?                       ")
              print("===================================================================")
              print("(1) Install an app from an APK")
              print("(2) Uninstall an aplication [red][bold] WARNING: Be avry cairful with this option, missuse will leed to you lousing all of your data")
              print("(3) Open an aplication")
              print("(4) Open a website on the devices default web browser")
              print("(5) Go back to menue")
              appmgr = input("Choose a nomber: ")
              #Install an app using an apk
              if appmgr == "1":
                   print("===================================================================")
                   print("[red]     WARNING: ONLY INSTALL APKS FROM DEVELOPERS YOU TRUST!!!  ")
                   print("===================================================================")
                   apkfilepath = input("Full path of the apk you with to install to the device: ")
                   #os.system(f"adb install {apkfilepath}")
                   print("[yellow][bold]Attempting install - Please Wait...")
                   try: 
                              with console.status("[bold green]Installing APK...") as status:
                                     result = subprocess.run(["./res/scrcpy/adb", "install", f"{apkfilepath}"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                   except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                   if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                   else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
              
              #Uninstall an application
              if appmgr == "2":
                   while True:
                    print("[red]==============================================================================================")
                    print("[red]  WARNING: YOU CAN SOFT BRICK YOUR DEVICE AND LOOSE ALL YOUR DATA WITH THIS OPTION  ")
                    print("[bold][red]               PROCEED ONLY IF YOU KNOW WHAT YOU ARE DOING                              ")
                    print("[red]==============================================================================================")
                    print("Type: 'I Acnoledge the risks and wish to continue'")
                    print("Press return or type anything else to return to the menue")

                    bigboypants = input("Time tooo choose MR.Freeman: ")

                    if bigboypants == "I Acnoledge the risks and wish to continue":
                         print("Your decision has been made")
                         input("Press return to list all packages")
                         print("===================================================================")
                         print("                       Application list                            ")
                         print("===================================================================")                         
                         os.system("./res/scrcpy/adb shell pm list packages")
                         print("===================================================================")
                         print("[red][bold]This is your final warning, the package you provide will be nucked")
                         print("===================================================================")
                         appdel = input("Input the package that you would like to purge: ")

                         #os.system(f"./res/scrcpy/adb uninstall {appdel}")
                         try: 
                               with console.status("[bold red]Uninstalling APK...") as status:
                                     result = subprocess.run(["./res/scrcpy/adb", "uninstall", f"{appdel}"], capture_output=True, text=True, check=True)
                                     
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                         except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                         if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         print(f"[green][bold]The deed is done, RIP: {appdel}")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                         else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                         
                                                             
                    else:
                         os.system("clear")
                         break
                   
              #Attempts to open an application
              if appmgr == "3":
                    print("===================================================================")
                    print("                       Application list                            ")
                    print("===================================================================")
                    input("Press return to list all apps on the device")
                    os.system("./res/scrcpy/adb shell pm list packages")
                    print("===================================================================")
                    print("[red][bold]WARNING: If you do not know what you are doing, hit return and lat this part of the script fail.")
                    print("App name format: [red]Package:[green]com.example.ex")
                    print("[green]Type this [red]Dont type this")
                    openapp = input("Plese input the full package name to open it on target device: ")
                    while True:
                         print("===================================================================")
                         print("    Do you want to launch with the default activity namespace.")
                         print("===================================================================")
                         print("[yellow]Note: Not all apps will work with this name space, and you can launch all apps with this tool.")
                         print("(1) Use Default Namespace: .MainActivity")
                         print("(2) Use custum activity name")
                         tooling = input("Choose a nomber: ")

                         if tooling == "1":
                                   #os.system(f"adb shell am start -n {openapp}/{openapp}.MainActivity")
                                   try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "am", "start", "-n", f"{openapp}/{openapp}.MainActivity"], capture_output=True, text=True, check=True)
                                     
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                                   except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                                   if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                                   else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                                        
                         
                         if tooling == "2":
                              print("===================================================================")
                              print("To find an activity name you can ether: Google it, or use Activity")
                              print("Launcher on an android device to find an activity name to use.")
                              print("===================================================================")
                              print("[red]com.example.example[green].<Activity>")
                              print("[green]Type this [red]Dont type this")
                              Actaspp = input("Type the activity: ")
                              #os.system(f"./res/scrcpy/adb shell am start -n {openapp}/{Actaspp}")
                              try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "am", "start", "-n", f"{openapp}/{Actaspp}"], capture_output=True, text=True, check=True)
                                     
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                              except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                              if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                              else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                              
              #Opens a web brouser window on target device
              if appmgr == "4":
                   print("===================================================================")
                   webaddr = input("Plese input the web adress to open on target device: ")
                   #Runs the command and checks for any errors
                   try: 
                    result = subprocess.run(["./res/scrcpy/adb", "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", f"'{webaddr}'"], capture_output=True, text=True, check=True)
                    print("[green]Output:", result.stdout)
                    print("[red]Errors:", result.stderr)
                    
                    if result.stderr == "":
                          print("[green]===================================================================")
                          print("[green]                    Command sent to device                         ")
                          print("[green]===================================================================")
                          input("Press return to go back to menu: ")
                          os.system("clear")
                    else:
                        print("[red]===================================================================")
                        print("[red]             An Error Ocured: See Above for Details                ")
                        print("[red]===================================================================")
                        input("Press return to continue: ")
                        os.system("clear")
                   
                   except subprocess.CalledProcessError as e:
                        print(f"Command failed with return code {e.returncode}")
                        print("Error output:", e.stderr)
                        print("[red]===================================================================")
                        print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                        print("[red]===================================================================")
                        input("Press return to continue: ")
                        os.system("clear")
                   except subprocess.SubprocessError as e:
                        print(f"Command failed with return code {e.returncode}")
                        print("Error output:", e.stderr)
                        print("[red]===================================================================")
                        print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                        print("[red]===================================================================")
                        input("Press return to continue: ")  

  
                   
               #Back to main
              if appmgr == "5":
                   os.system("clear")
                   break
    #Settings manager
    if coice == "12":
          while True:
                os.system("clear")
                print("========================================================================")
                print("                 Pick a system setting to change                        ")
                print("========================================================================")
                print("Quick Settings Changes: ================================================")
                print("(1) Enable / Disable Extream Slowness")
                print("(2) Enable / Disable Wi-Fi")
                print("(3) Enable / Disable Bluetooth")
                print("(4) Enable / Disable Bounding boxes")
                print("(5) Enable / Disable Show tapps")
                print("(6) Enable / Disable Zoom [red][bold]WARNING: It is best not to disconnect while this is enabled, SETTING CHANGED: Adjust minimum width")
                print("(7) Roate the screen")
                print("(8) Change screen colors")
                print("(9) Invoke Home Screen Switcher")
                print(" ")
                print("Misc: ==================================================================")
                print("(10) Send a custum notification to the device")
                print("(11) Take a Screenshot") 
                print("(12) Take a Screen Recording") #Add
                print("(13) Starting phone loop")
                print("Custum: ================================================================")
                print("(14) Use a custum namespace, key and value [bold][red]FOR ADVANCED USE ONLY, NOT RECOMENDED FOR NORMAL USE")
                print("(15) Exit")
                setngs = input("Choose a nomber: ")
                print("========================================================================")
                
                if setngs == "1":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable Extream Slowness")
                            print("(2) Dissable Extream Slowness")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     #adb shell settings put global window_animation_scale 0.5
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "global", "window_animation_scale", "10"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put global transition_animation_scale 10")
                                         os.system("./res/scrcpy/adb shell settings put global animator_duration_scale 10")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                             
                            
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "global", "window_animation_scale", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put global transition_animation_scale 1")
                                         os.system("./res/scrcpy/adb shell settings put global animator_duration_scale 1")                                         
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break

                #Wifi
                if setngs == "2":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable Wi-Fi")
                            print("(2) Dissable Wi-Fi")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "svc", "wifi", "enable"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                            
                            
                            
                            
                            
                            
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "svc", "wifi", "disable"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #Bluetooth                
                if setngs == "3":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable Bluetooth")
                            print("(2) Dissable Bluetooth")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "cmd", "bluetooth_manager", "enable"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                              
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "cmd", "bluetooth_manager", "disable"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #Bounding boxes      
                if setngs == "4":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable Bounding Boxes")
                            print("(2) Dissable Bounding")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     #adb shell setprop debug.layout true

                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "setprop", "debug.layout", "true"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell service call activity 1599295570")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                              
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "setprop", "debug.layout", "false"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell service call activity 1599295570")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #Taps      
                if setngs == "5":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable Show taps")
                            print("(2) Dissable Show taps")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     #./res/scrcpy/adb shell settings put system show_touches 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "show_touches", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                              
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "show_touches", "0"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #Zoom
                if setngs == "6":
                      while True:
                            print("What would you like to do?")
                            print("(1) Enable zoom")
                            print("(2) Dissable zoom")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     #adb shell settings put global debug.force_rtl 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "wm", "size", "600x600"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         #os.system("./res/scrcpy/adb shell wm size 500x500")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                              
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "wm", "size", "reset"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":                                        
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #Screen Rotation
                if setngs == "7":
                      while True:
                            print("What would you like to do?")
                            print("(1) Rotate Portrate")
                            print("(2) Rotate Landscape")
                            print("(3) Roatte Portrate Flipped")
                            print("(4) Roatte Landscape Flipped")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: 
                                     #./res/scrcpy/adb shell settings put system user_rotation 0
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "user_rotation", "0"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         #os.system("./res/scrcpy/adb shell wm size 500x500")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                              
                            if onoffwifi == "2":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "user_rotation", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":                                        
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                               
                            if onoffwifi == "3":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "user_rotation", "2"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":                                        
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                               
                            if onoffwifi == "4":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "system", "user_rotation", "3"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":                                        
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                      
                #Color Management
                if setngs == "8":
                       while True:
                              print("Which color setting would you like to set?")
                              print("(1) Default colors")
                              print("(2) Monochromatic colors")
                              print("(3) Protanomaly colors")
                              print("(4) Invert colors")
                              colorscape = input("Choose a nomber: ")

                              if colorscape == "1":
                               try: #adb shell settings put secure accessibility_display_daltonizer_enabled 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "secure", "accessibility_display_daltonizer_enabled", "0"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put secure accessibility_display_daltonizer -1")
                                         os.system("./res/scrcpy/adb shell settings put secure accessibility_display_inversion_enabled 0")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break 
                               
                              if colorscape == "2":
                               try: #adb shell settings put secure accessibility_display_daltonizer_enabled 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "secure", "accessibility_display_daltonizer_enabled", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put secure accessibility_display_daltonizer 0")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break 
                               
                              if colorscape == "3":
                               try: #./res/scrcpy/adb shell settings put secure accessibility_display_daltonizer_enabled 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "secure", "accessibility_display_daltonizer_enabled", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put secure accessibility_display_daltonizer 11")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                              
                              if colorscape == "4":
                               try: #a./res/scrcpy/adb shell settings put secure accessibility_display_inversion_enabled 1
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", "secure", "accessibility_display_inversion_enabled", "1"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell settings put secure accessibility_display_daltonizer 11")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break  
                #Swich default home menu                     
                if setngs == "9":
                  while True:
                            print("What would you like to do?")
                            print("(1) Invoke default home menu swicher")
                            print("(2) Go Back")
                            onoffwifi = input("Choose a nomber: ")

                            if onoffwifi == "1":
                               try: #./res/scrcpy/adb shell am start -a android.settings.HOME_SETTINGS   
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "am", "start", "-a", "android.settings.HOME_SETTINGS"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break                            
                            
                            
                            
                            
                            
                            
                            if onoffwifi == "2":
                              break
                #Send a notification
                if setngs == "10":
                      print("Custum: ================================================================")
                      title = input("Write the title/ hedder of the notification: ")
                      print(title)
                      tag = input("Write a tag for the notification: ")
                      text = input("Write the main text of the notification: ")
                      #os.system(f"./res/scrcpy/adb shell cmd notification post -S bigtext -t '{title}' '{tag}' '{text}'")
                      subprocess.run(["./res/scrcpy/adb","shell","cmd","notification","post","-S","bigtext","-t",f"'{title}'", f"'{tag}'",f"'{text}'"])
                      print("[green][bold]Command sent sucessfully")
                      input("Press return to go back to menue: ")
                      break
                #Take a screenshot
                if setngs == "11":
                      print("========================================================================")
                      print("                   Attempting to take screenshot                        ")
                      print("========================================================================")
                      os.system("./res/scrcpy/adb exec-out screencap -p > Latest_screenshot.png")
                      print("[green]===================================================================")
                      print("[green]                    Command sent to device                         ")
                      print("[green]===================================================================")
                      print("[yellow] File has been saved to the program directory")
                      input("Press return to go back to the menue: ")
                      os.system("clear")
                #Screen recording
                if setngs == "12":
                      print("[yellow]This tool does not support error handling")
                      print("When you want to finish recording, press ctrl + c")
                      os.system("./res/scrcpy/adb shell screenrecord /sdcard/Movies/vibdio.mp4")
                      input("Screen recording captured, Press return for options: ")
                      print("========================================================================")
                      print("What would you like to do with the video file?")
                      print("(1) Send captured video to this device")
                      print("(2) Do nothing and go back to the main menu")
                      vrec = input("Choose a nomber: ")
                      while True:
                        if vrec == "1":
                              print("Attempting to download file to this device")
                              os.system("./res/scrcpy/adb pull /sdcard/Movies/vibdio.mp4 ~/Downloads")
                              print("[green]==============================================")
                              print("[green]       File seved to Downloads folder         ")
                              print("[green]==============================================")
                              input("Press return to go back to main menu: ")
                              os.system("clear")
                              break
                        if vrec == "2":
                              os.system("clear")
                              break
                
                if setngs == "13":
                       print("What would you like to do?")
                       print("(1) Enable Looping Home")
                       print("(2) Go back")
                       print("[red][bold]Warning: To undo this change, you must invoke the homescreen swicher")
                       loop = input("Choose a nomber: ")

                       if loop == "1":
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "cmd", "package", "set-home-activity", "'com.android.settings/com.android.settings.Settings'"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break  
                              
                       
                       if loop == "2":
                              break
                #Custum Settings
                if setngs == "14":
                      while True: 
                         print("========================================================================")
                         print("Choose a namespace: ")
                         print("(1) System")
                         print("(2) Secure")
                         print("(3) Global")
                         name_space = input("Choose a nomber: ")

                         if name_space == "1":
                               name_space = "system"
                               print("========================================================================")
                               print(f"Showing all keys in namespace: {name_space}")
                               input("Press return for list: ")
                               os.system(f"./res/scrcpy/adb shell settings list {name_space}")
                               print("========================================================================")
                               key = input("Pick a key: ")
                               value = input("Set a value for this key: ")
                               
                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", f"{name_space}", f"{key}", f"{value}"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                         
                         if name_space == "2":
                               name_space = "secure"
                               print("========================================================================")
                               print(f"Showing all keys in namespace: {name_space}")
                               input("Press return for list: ")
                               os.system(f"./res/scrcpy/adb shell settings list {name_space}")
                               print("========================================================================")
                               key = input("Pick a key: ")
                               value = input("Set a value for this key: ")

                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", f"{name_space}", f"{key}", f"{value}"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                               
                         if name_space == "3":
                               name_space = "global"
                               print(name_space)
                               print("========================================================================")
                               print(f"Showing all keys in namespace: {name_space}")
                               input("Press return for list: ")
                               os.system(f"./res/scrcpy/adb shell settings list {name_space}")
                               print("========================================================================")
                               key = input("Pick a key: ")
                               value = input("Set a value for this key: ")

                               try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "settings", "put", f"{name_space}", f"{key}", f"{value}"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                               except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                               if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                               else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                #BTM
                if setngs == "15":
                      os.system("clear")
                      break
    #Shizuku starter                     
    if coice == "13":
          while True:
                print("========================================================================================")
                print("        Do you have [blue]Shizuku [white]installed on the target device?")
                print("========================================================================================")
                print("(1) Yes")
                print("(2) No")
                shizu = input("Choose a nomber: ")
                print("========================================================================================")

                if shizu == "1":
                      input("Press return to enable Semi-Root prvleges on the target device: ")
                      try: 
                                     result = subprocess.run(["./res/scrcpy/adb", "shell", "sh", "/storage/emulated/0/Android/data/moe.shizuku.privileged.api/start.sh"], capture_output=True, text=True, check=True)
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                      except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                      if result.stderr == "":
                                         os.system("./res/scrcpy/adb shell am start -n moe.shizuku.privileged.api/moe.shizuku.manager.MainActivity")
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                      else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         print("[red]Please ensure that [blue]Shizuku[white] is installed.")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                      

                
                if shizu == "2":
                      print("Please install [blue]Shizuku [white]on the google play store to continue")
                      input("Press return to go back to the main menu: ")
                      os.system("clear")
                      break
    #Switch launcher
    if coice == "14":
           print("========================================================================")
           print("          Set launcher as the google pixel launcher alternative         ")
           print("========================================================================")
           print("[bold]BEFORE YOU RUN THIS SCRIPT: ")
           print("Download the apk from https://lawnchair.app/, renaim it LC")
           print("and put it in the apk folder.")
           print(" ")
           print("WHAT THIS WILL DO:")
           print("1. Install lawnchair 15 to target device.")
           print("2. Force target device to use Lawnchair as its default launcher.")
           print(" ")
           print("WHAT IS THIS FOR: ")
           print("This is primaraly for oem's that do not allow an easy way to swich launcher. EX: Amazon")
           print("This should work on every device.")
           print(" ")
           print("HOW TO REVERT CHANGES: ")
           print("Reverting these changes can be done through device settings.")
           print("It can also be done through the settings manager in this app.")
           print(" ")
           print("[bold]Lawnchair website: https://lawnchair.app/")
           print("========================================================================")
           print("                 (1) Run the script | (2) Cancel                        ")
           
           while True:
            lncher = input("Choose an option listed above: ")
                  
            if lncher == "1":

                        try: 
                              with console.status("[bold green]Installing APK...") as status:
                                    result = subprocess.run(["./res/scrcpy/adb", "install", "apk/LC.apk"], capture_output=True, text=True, check=True)
                                    print("[green]Output:", result.stdout)
                                    print("[red]Errors:", result.stderr)
                                    
                        except subprocess.CalledProcessError as e:
                                          print(f"Command failed with return code {e.returncode}")
                                          print("Error output:", e.stderr)
                                          #console.log(" ")
                                          print("[red]===================================================================")
                                          print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                          print("[red]===================================================================")
                                          input("Press return to continue: ")
                                          os.system("clear")
                                          break
                                    
                        if result.stderr == "":
                                          print("[bold][green] Sucessfully installed APK! Making default...")
                                          os.system("./res/scrcpy/adb shell cmd package set-home-activity 'app.lawnchair/app.lawnchair.LawnchairLauncher' ")
                                          os.system("./res/scrcpy/adb shell am start -n app.lawnchair/app.lawnchair.LawnchairLauncher")
                                          print("[green]===================================================================")
                                          print("[green]           Launcher Sucessfully Installed and Applied                         ")
                                          print("[green]===================================================================")
                                          input("Press return to go back to menu: ")
                                          os.system("clear")
                                          break
                        else:
                                          #console.log(" ")
                                          print("[red]===================================================================")
                                          print("[red]             An Error Ocured: See Above for Details                ")
                                          print("[red]===================================================================")
                                          input("Press return to continue: ")
                                          os.system("clear")
                                          break
            
            if lncher == "2":
                   os.system("clear")
                   break
    #Funnys                                      
    if coice == "15":
           print("========================================================================")
           print("                 Set launcher as the troll launcher                     ")
           print("========================================================================")
           print("WHAT THIS WILL DO:")
           print("1. Install a custum 'troll' launcher that i designed to target device.")
           print("2. Force target device to use it as its default launcher.")
           print(" ")
           print("WHAT IS THIS FOR: ")
           print("This is primeraly to screw with people for the funny")
           print("This should work on every device.")
           print(" ")
           print("HOW TO REVERT CHANGES: ")
           print("Reverting these changes can be done through the device settings")
           print("This can also be done in the settings manager in this app")
           print(" ")
           print("OTHER USEFULL INFORMATION")
           print("Because of the way this app is designed, it is hard to uninstall and it")
           print("does not show up in launchers, because of this, use the uninstall option")
           print("after you are done messing with the target device.")
           print(" ")
           print("[bold]Troll Credits: Me :)")
           print("========================================================================")
           print("(1) Not Finalised, check for updates later | (2) Uninstall |(3) Cancel  ")
           
           while True:
            ltncher = input("Choose an option listed above: ")
                  
            if ltncher == "WIP": #WIP dont change this until Troll is up on github
                        #./res/scrcpy/adb shell cmd package set-home-activity "package.name/activity.name" To set as default launcher
                        try: 
                              with console.status("[bold green]Installing APK...") as status:
                                    result = subprocess.run(["./res/scrcpy/adb", "install", "apk/troll.apk"], capture_output=True, text=True, check=True)
                                    print("[green]Output:", result.stdout)
                                    print("[red]Errors:", result.stderr)
                                    
                        except subprocess.CalledProcessError as e:
                                          print(f"Command failed with return code {e.returncode}")
                                          print("Error output:", e.stderr)
                                          #console.log(" ")
                                          print("[red]===================================================================")
                                          print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                          print("[red]===================================================================")
                                          input("Press return to continue: ")
                                          os.system("clear")
                                          break
                                    
                        if result.stderr == "":
                                          print("[bold][green] Sucessfully installed APK! Making default...")
                                          os.system("./res/scrcpy/adb shell cmd package set-home-activity 'com.troll.ncatl/com.godot.game.GodotApp' ")
                                          os.system("./res/scrcpy/adb shell am start -n com.troll.ncatl/com.godot.game.GodotApp")
                                          print("[green]===================================================================")
                                          print("[green]           Launcher Sucessfully Installed and Applied                         ")
                                          print("[green]===================================================================")
                                          input("Press return to go back to menu: ")
                                          os.system("clear")
                                          break
                        else:
                                          #console.log(" ")
                                          print("[red]===================================================================")
                                          print("[red]             An Error Ocured: See Above for Details                ")
                                          print("[red]===================================================================")
                                          input("Press return to continue: ")
                                          os.system("clear")
                                          break
            
            if ltncher == "2":
                         try: 
                               with console.status("[bold red]Uninstalling APK...") as status:
                                     result = subprocess.run(["./res/scrcpy/adb", "uninstall", "com.troll.ncatl"], capture_output=True, text=True, check=True)
                                     
                                     print("[green]Output:", result.stdout)
                                     print("[red]Errors:", result.stderr)
                                   
                         except subprocess.CalledProcessError as e:
                                    print(f"Command failed with return code {e.returncode}")
                                    print("Error output:", e.stderr)
                                    print("[red]===================================================================")
                                    print("[red]     An Error Ocured: Plese connect a device before continuing     ")
                                    print("[red]===================================================================")
                                    input("Press return to continue: ")
                                    os.system("clear")
                                    break
                                   
                         if result.stderr == "":
                                         print("[green]===================================================================")
                                         print("[green]                    Command sent to device                         ")
                                         print("[green]===================================================================")
                                         print(f"[green][bold]The deed is done, RIP: Troll Launcher")
                                         input("Press return to go back to menu: ")
                                         os.system("clear")
                                         break
                         else:
                                         print("[red]===================================================================")
                                         print("[red]             An Error Ocured: See Above for Details                ")
                                         print("[red]===================================================================")
                                         input("Press return to continue: ")
                                         os.system("clear")
                                         break
                   
                   
            
            if ltncher == "3":
                  os.system("clear")
                  break
    #Quits the app
    if coice == "16":
        os.system("clear")
        print("Created by")
        print("""   [red]█████████   ████████  ███████████ 
 [red]███▒▒▒▒▒███ ███▒▒▒▒███▒▒███▒▒▒▒▒███
[green]▒███    ▒▒▒ ▒▒▒    ▒███ ▒███    ▒███
[green]▒▒█████████    ██████▒  ▒██████████ 
 [blue]▒▒▒▒▒▒▒▒███  ▒▒▒▒▒▒███ ▒███▒▒▒▒▒███
 [blue]███    ▒███ ███   ▒███ ▒███    ▒███
[yellow]▒▒█████████ ▒▒████████  ███████████ 
 [yellow]▒▒▒▒▒▒▒▒▒   ▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒▒▒  
https://github.com/S3b-sudo/Android-Tools""")
        print("The swiss army knife for all things android")
        print("[yellow]Thank you for using Android Tools :)")
        quit()
