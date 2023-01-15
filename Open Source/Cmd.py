import os
import subprocess
from colorama import Fore, Style
import ctypes
import requests
import time
import gzip
import psutil
import string
import random
import smtplib, ssl

def change_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

change_title("XainowAI@DualBoot: ~")


def terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.LIGHTCYAN_EX + "XainowAI Terminal ", end="")
    print(Fore.LIGHTCYAN_EX + "[version 10.0.22000.1455]\n", end="")
    print(Fore.LIGHTYELLOW_EX + "©", end="")
    print(Fore.LIGHTRED_EX + " XainowAI Corporation. Tous droits réservés.")
    current_directory = os.getcwd()
    print(Fore.WHITE + "\n" + current_directory + ">", end="")
    while True:
        command = input()
        print()
        if command == "exit":
            break
        elif command == "help":
            print("Liste des commandes disponibles :")
            print("- exit : pour quitter le terminal")
            print("- help : pour afficher cette liste de commandes")
            print("- clear : pour nettoyer l'écran")
            print("- ip : pour afficher l'adresse IP publique")
            print("- ping : pour envoyer un paquet ping à une adresse IP ou un nom d'hôte")
            print("- pip : pour install les package")
            print("- python : pour éxécuter des fichier python")
            print("- ls : pour afficher le contenu du répertoire courant")
            print("- snake : pour jouer à snake")
            print("- sysinfo : pour afficher les informations système")
            print("- compress : pour compresser un fichier en utilisant un algorithme spécifique")
            print("- decompress : pour décompresser un fichier en utilisant un algorithme spécifique")
            print("- password : pour générer un mot de passe aléatoire")
            print("- ps : pour afficher les processus en cours d'exécution et leur utilisation de la mémoire")
            print("- hacker-mode : active le mode hacker")
            print("- antivirus : execute une analyse anti-virus")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
            
        elif command == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTCYAN_EX + "XainowAI Terminal ", end="")
            print(Fore.LIGHTCYAN_EX + "[version 10.0.22000.1455]\n", end="")
            print(Fore.LIGHTYELLOW_EX + "(c)", end="")
            print(Fore.LIGHTRED_EX + " XainowAI Corporation. Tous droits réservés.")
            current_directory = os.getcwd()
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command == "ip":
            try:
                ip = requests.get("http://ip.42.pl/raw").text
                print("Adresse IP publique : " + ip)
            except requests.ConnectionError:
                print("\nImpossible de se connecter pour obtenir l'adresse IP publique.")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command.startswith("ping "):
            try:
                hostname = command.split(" ")[1]
                subprocess.run(["ping", hostname])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command.startswith("pip"):
           package = command.split(" ")[2]
           subprocess.run(["pip", "install", package])
           print("Installation du package "+ package + " terminé")
           time.sleep(3.4)
           print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command.startswith("python"):
            try:
               filename = command.split(" ")[1]
               subprocess.run(["python", filename])
            except subprocess.CalledProcessError as e:
                print(f"Error: {e}")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command == "ls":
             output = os.popen('dir').read()
             print(output)
             print(Fore.WHITE + "\n" + current_directory + ">", end="")

                
        elif command == "snake":
             file_path = r"C:\Users\vilai\Desktop\Cmd\Snake.exe"
             if os.path.isfile(file_path):
                os.startfile(file_path)
                print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command == "sysinfo":
             print("System Information:")
             print("CPU: ", psutil.cpu_percent(), "%")
             print("Memory: ", psutil.virtual_memory().percent, "%")
             print("Disk: ", psutil.disk_usage('/').percent, "%")
             print(Fore.WHITE + "\n" + current_directory + ">", end="")
             
        elif command == "openapp":
              app_name = command.split(" ")[1]
              subprocess.run([app_name])
              print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command.startswith("compress "):
             file_name = command.split(" ")[1]
             with open(file_name, "rb") as f_in:
               with gzip.open(file_name + ".gz", "wb") as f_out:
                   f_out.writelines(f_in)
                   print(f"File {file_name} has been compressed.")
                   print(Fore.WHITE + "\n" + current_directory + ">", end="")
                              
        elif command.startswith("decompress "):
             file_name = command.split(" ")[1]
             
        if command in ["ps", "processes"]:
            for proc in psutil.process_iter():
                try:
                    process_info = proc.as_dict(attrs=['pid', 'name', 'memory_info'])
                    print(process_info)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                  pass
              
        elif command.startswith("password"):
             args = command.split(" ")
             if len(args)>1:
              length = int(args[1])
              password = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(length))
              print("Votre mot de passe aléatoire est : ", password)
              print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command == "hello":
            print("hello world")
            print(Fore.WHITE + "\n" + current_directory + ">", end="")
        
        elif command == "hacker-mode":
           print("Entrer le mot de passe pour activer le mode hacker:")
           password = input("--> ")
           if password == "admin":
              print("Mode hacker activé. Utilisez la commande 'hacker-help' pour obtenir de l'aide.")
              print(Fore.WHITE + "\n" + current_directory + ">", end="")
        if command == "hacker-help":
               print("Liste des commandes hacker disponibles:")
               print("- hack : pour lancer une attaque sur une cible.")
               print("- spoof [IP/URL]: pour masquer votre adresse IP.")
               print(Fore.WHITE + "\n" + current_directory + ">", end="")
 
        elif command.startswith("spoof"):
             try:
               new_ip = command.split(" ")[1]
               subprocess.run(["netsh", "interface", "ip", "set", "address", "name=", "Local Area Connection", "static", new_ip])
               print("L'adresse IP a été changée en " + new_ip)
               print(Fore.WHITE + "\n" + current_directory + ">", end="")
               current_directory = os.getcwd()
             except IndexError:
                print("Veuillez fournir une adresse IP valide pour effectuer le changement.")
             except Exception as e:
                print(f"Une erreur s'est produite: {e}")
                print(Fore.WHITE + "\n" + current_directory + ">", end="")

        elif command == "antivirus":
             print("Analyse antivirus en cours...")
             try:
                 subprocess.run(["mpcmdrun", "-scan", "-scantype", "3"], check=True)
                 print("Aucun virus détecté.")
             except subprocess.CalledProcessError as e:
                print(e.output)
                print("Des virus ont été détecté.")
             except FileNotFoundError:
                print("Vous devez utiliser une version professionnelle de Windows pour utiliser cette commande.")
                print(Fore.WHITE + "\n" + current_directory + ">", end="")
        elif command == "hack":
             input("entrez la cible: ")
             print("[-] Lancement de l'attaque...")
             os.system("color 0c") # change la couleur du texte en rouge
             subprocess.call("title Attaque en cours", shell=True) # change le titre de la fenêtre
             subprocess.call("ping localhost -n 2 > nul", shell=True) # envoie un ping à localhost (simule une activité réseau)
             print("[-] Connexion à la cible...")
             subprocess.call("ping 8.8.8.8 -n 2 > nul", shell=True) # envoie un ping à 8.8.8.8 (simule une connexion à un hôte distant)
             print("[+] Cible acquise.")
             time.sleep(1.5)
             print("[-] Lancement de l'exploit...")
             subprocess.call("ping localhost -n 2 > nul", shell=True) # envoie un ping à localhost (simule une activité réseau)
             print("[+] Exploit réussi.")
             time.sleep(1.0)
             print("[-] Récupération des données...")
             subprocess.call("ping localhost -n 2 > nul", shell=True) # envoie un ping à localhost (simule une activité réseau)
             print("[+] Données récupérées.")
             time.sleep(1.0)
             print("[+] Attaque terminée.")
             os.system("color 07") # change la couleur du texte en blanc
             print(Fore.WHITE + "\n" + current_directory + ">", end="")

 
 
 
 
        
terminal()
