import os
import datetime

def system_info():
    info = {
        "Operating System": os.name,                  
        "User": os.getlogin(),                        
        "Current Directory": os.getcwd(),             
        "Home Directory": os.path.expanduser("~"),    
        "Current Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("\n SYSTEM INFORMATION ")
    print("-" * 40)
    for key, value in info.items():
        print(f"{key:20}: {value}")
    print("-" * 40)

if __name__ == "__main__":
    system_info()
