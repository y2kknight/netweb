import os

ascii_art = r"""    
   ________  ________  ________  ________  ________  ________
  ╱    ╱   ╲╱        ╲╱        ╲╱  ╱  ╱  ╲╱        ╲╱       ╱
 ╱         ╱        _╱        _╱         ╱        _╱        ╲
╱         ╱        _╱╱       ╱╱         ╱        _╱         ╱
╲__╱_____╱╲________╱ ╲______╱ ╲________╱╲________╱╲________╱ 
"""

print(ascii_art)

website = input("Please enter a website URL: ")
response = os.system(f"ping -n 4 {website}")

if response == 0:
    print(f"{website} is reachable")
else:
    print(f"{website} is not reachable")

input("Press Enter to exit...")




