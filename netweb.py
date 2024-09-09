# os module allows system interaction
import os

# Utilized a raw string so python ignores slashes
ascii_art = r"""    
   ________  ________  ________  ________  ________  ________
  ╱    ╱   ╲╱        ╲╱        ╲╱  ╱  ╱  ╲╱        ╲╱       ╱
 ╱         ╱        _╱        _╱         ╱        _╱        ╲
╱         ╱        _╱╱       ╱╱         ╱        _╱         ╱
╲__╱_____╱╲________╱ ╲______╱ ╲________╱╲________╱╲________╱ 
"""

print(ascii_art)

print("""Options:
        1 - ping
        2 - tracert""")

choice = input("Please choose a number: ")

website = input("Please enter a URL: ")

# Initialize response to avoid NameError
response = None

# "system" function from os module allows me to use system commands
# Utilized an f string to embed website variable into the string
if choice == "1":
    response = os.system(f"ping -n 4 {website}")

    if response == 0:
        print(f"{website} is reachable")

# A successful ping command has an exit code of 0
    else:
        print(f"{website} is not reachable")

elif choice == "2": 
    os.system(f"tracert {website}")
else: 
    print("Invalid choice. Please choose 1 or 2.")
# tracert does not produce an exit code so no need to verify equality with response

input("Press Enter to exit...")
