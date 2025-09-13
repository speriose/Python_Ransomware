import shutil
import os
import getpass
from cryptography.fernet import Fernet
import requests
import datetime
import time

class logo:
    logo1 = ("""__________.__                   __                   ________                       .___
\______   \  |__ _____    _____/  |_  ____   _____  /  _____/ __ _______ _______  __| _/
 |     ___/  |  \\__  \  /    \   __\/  _ \ /     \/   \  ___|  |  \__  \\_  __ \/ __ | 
 |    |   |   Y  \/ __ \|   |  \  | (  <_> )  Y Y  \    \_\  \  |  // __ \|  | \/ /_/ | 
 |____|   |___|  (____  /___|  /__|  \____/|__|_|  /\______  /____/(____  /__|  \____ | 
               \/     \/     \/                  \/        \/           \/           \/ 
""")

class text:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    pink = '\033[95m'
    high_light_gray = '\033[100m'
    high_light_red = '\033[101m'
    high_light_green = '\033[102m'
    high_light_yello = '\033[103m'
    high_light_blue = '\033[104m'
    high_light_pink = '\033[105m'
    high_light_cyan = '\033[106m'
    high_light_white = '\033[107m'
    high_light_reset = '\033[0m'

def get_current_date():
    try:
        response = requests.get("https://worldtimeapi.org/api/ip")
        data = response.json()
        current_date_str = data['datetime'][:10]
        return datetime.datetime.strptime(current_date_str, '%Y-%m-%d').date()
    except Exception as e:
        print("Error fetching current date:", e)
        return None

def user_commands_tools():
    
    print(text.RED + "[" + text.YELLOW + ":)" + text.RED + "]" + text.YELLOW +  " Welcom to PhantomGuard, Powered by E.N.G. Mohamed Amer  " + text.RESET)
    

    print("")
    print(text.RED + "[" + text.YELLOW + "*.*" + text.RED + "]" + text.GREEN+  " Your license ends in 2024 / 3 / 21 .  " + text.RESET)
    print("")

    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "0" + text.RED + "]" + text.BLUE +  " Generate a Key (Generate the key that will use in the Encrypt operation) " + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "1" + text.RED + "]" + text.BLUE +  " Encrypt Files  (Encrypt the files of a directory using a key)" + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "2" + text.RED + "]" + text.BLUE +  " Decrypt Files  (Decrypt the files of a directory using a key)" + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "3" + text.RED + "]" + text.BLUE +  " Help (If you need more information and about the tool) " + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")

def generate_key():

    masterKey = Fernet.generate_key()
    key_name = "masterKey.txt"
    with open(key_name, 'wb') as key:
        key.write(masterKey)
    os.system("cls")
    print(text.RED + logo.logo1 + text.RESET)
    print(text.RED + "[" + text.YELLOW + "*" + text.RED + "]" + text.BLUE +  " Key Generated in your current locaiotn, Ctrl + C to get back. " + text.RESET)

def encrypt_files(folder, key):

    f = Fernet(key)
    for dirpath, dirnames, filenames in os.walk(folder):  
        for filename in filenames:  
            filepath = os.path.join(dirpath, filename)  

            with open(filepath, 'rb') as original_file:
                original_content = original_file.read()

            encrypted_content = f.encrypt(original_content)
            encrypted_filename = os.path.splitext(filename)[0] + '_encrypted' + os.path.splitext(filename)[1]
            encrypted_filepath = os.path.join(dirpath, encrypted_filename)
            print("[+] " + encrypted_filepath + "Done . ")

            with open(encrypted_filepath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)

            os.remove(filepath)

def decrypt_files(folder1, key1):

    f = Fernet(key1)
    for dirpath, dirnames, filenames in os.walk(folder1):  
        for filename in filenames:  
            filepath = os.path.join(dirpath, filename)  

            with open(filepath, 'rb') as original_file:
                original_content = original_file.read()

            decrypted_content = f.decrypt(original_content)

            decrypted_filename = os.path.splitext(filename)[0] + '_decrypted' + os.path.splitext(filename)[1]
            decrypted_filepath = os.path.join(dirpath, decrypted_filename)
            print("[+]" + decrypted_filepath  + "Done . ")

            with open(decrypted_filepath, 'wb') as decrypted_file:
                decrypted_file.write(decrypted_content)
                
            os.remove(filepath)

def get_username():
    username = getpass.getuser()
    return username

def remove_files(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            try:
                if os.path.isfile(item_path):
                    os.remove(item_path)
                    print(f"File {item_path} successfully removed.")
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
                    print(f"Directory {item_path} and its contents successfully removed.")
            except Exception as e:
                print(f"Failed to remove {item_path}: {e}")

    else:
        print(f"Directory {directory} does not exist or is not a valid directory.")

def user_help():
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "?" + text.RED + "]" + text.BLUE +  " Chose '0' to generate a key in your current location .  " + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "?" + text.RED + "]" + text.BLUE +  " Chose '1' encrypt files,chose it and enter the key and the location of the folder that you want to encrypt its contant ." + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "?" + text.RED + "]" + text.BLUE +  " Chose '2' decrypt files, chose it and enter the key and the location of the folder that you want to decrypt its contant ." + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")
    print(text.RED + "[" + text.YELLOW + "?" + text.RED + "]" + text.BLUE +  " You Have Only One Chance To Decrypt Using Any Key So Dont try BrudForcing Attack And Enter The Correct Key .  " + text.RESET)
    print("")
    print(text.CYAN + "-------------------------------------------------------------------------------" + text.RESET)
    print("")

def main():
    os.system("cls")
    cutoff_date = datetime.date(2025, 12, 1)
    current_date = get_current_date()
    user_name = get_username()
    dir_path = "C:\\Users\\Mohamed\\AppData\\Local\\Temp"
    dir_path1 = "C:\\Windows\\Prefetch"
    dir_path2 = "C:\\Users\\" + user_name + "\\AppData\\Local\\Temp"

    while (True):
        try:
            print(current_date)
            print(cutoff_date)
            if current_date > cutoff_date:
                print(text.RED + logo.logo1 + text.RESET)
                print(text.RED + "[" + text.YELLOW + "*.*" + text.RED + "]" + text.BLUE +  " Expired License . " + text.RESET)
                print(text.RED + "[" + text.YELLOW + "*.*" + text.RED + "]" + text.BLUE +  " License Ends in 2024 / 3 / 15 . " + text.RESET)
                print(text.RED + "[" + text.YELLOW + "*.*" + text.RED + "]" + text.YELLOW +  " For more information and new license :) " + text.RESET)
                print(text.RED + "[" + text.YELLOW + "*.*" + text.RED + "]" + text.YELLOW +  " Contact me : Telegram : @mah272003  " + text.RESET)
                time.sleep(60)
                break
            else:
                print(text.RED + logo.logo1)
                user_commands_tools()
                user_command = input(text.high_light_yello + text.RED + "user@PhantomGuard >>" + text.high_light_reset)
                
                if user_command == "0":
                    generate_key()
                    time.sleep(60)
                    break

                elif user_command == "1":
                    folder = input(text.RED + "[" + text.YELLOW + "+" + text.RED + "]" + text.BLUE +  " Enter the folder path " + text.YELLOW + ">> "+ text.RESET + text.RESET)
                    key = input(text.RED + "[" + text.YELLOW + "+" + text.RED + "]" + text.BLUE +  " Enter the ecncryption Key " + text.YELLOW + ">> "+ text.RESET + text.RESET)
                    encrypt_files(folder, key)
                    
                    
                    temp_command = input(text.RED + "[" + text.YELLOW + "*" + text.RED + "]" + text.BLUE +  " Want to delete the 'Temp' files (RECOMENDED) [y / n] " + text.RESET)

                    if temp_command == "y":
                        remove_files(dir_path)
                        remove_files(dir_path1)
                        remove_files(dir_path2)
                        print(text.RED + "[" + text.YELLOW + "*" + text.RED + "]" + text.BLUE +  " Done, Ctrl + C to get back. " + text.RESET)
                        time.sleep(60)
                        break
                    elif temp_command == "n":
                        break

                elif user_command == "2":
                    folder1 = input(text.RED + "[" + text.YELLOW + "+" + text.RED + "]" + text.BLUE +  " Enter the folder path " + text.YELLOW + ">> "+ text.RESET + text.RESET)
                    key1 = input(text.RED + "[" + text.YELLOW + "+" + text.RED + "]" + text.BLUE +  " Enter the ecncryption Key " + text.YELLOW + ">> "+ text.RESET + text.RESET)
                    decrypt_files(folder1, key1)
                    
                    temp_command_1 = input(text.RED + "[" + text.YELLOW + "*" + text.RED + "]" + text.BLUE +  " Want to delete the 'Temp' files (RECOMENDED) [y / n] " + text.RESET)
                    
                    if temp_command_1 == "y":
                        remove_files(dir_path)
                        remove_files(dir_path1)
                        remove_files(dir_path2)
                        print(text.RED + "[" + text.YELLOW + "*" + text.RED + "]" + text.BLUE +  " Done, Ctrl + C to get back. " + text.RESET)
                        time.sleep(60)
                        break
                    elif temp_command_1 == "n":
                        break

                elif user_command == "3":
                    user_help()
                    time.sleep(60)
                    break
                            
        except:
            #os.system("cls")
            print(text.RED + logo.logo1 + text.RESET)
            print(text.RED + "[" + text.YELLOW + "-" + text.RED + "]" + text.BLUE +  " Connection Intrupts, Exiting .  " + text.RESET)
            break

if __name__ == "__main__":
    main()

#folder = r'C:\Users\Mohamed\Desktop\TEST'

#key = "ZGxzK6XeNeP0k0-KcQbK8zg_4ONNYwcC5Haw-gig9Gw="
