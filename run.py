import time
import subprocess
passes = 1

while passes<=1:
    print(f"Rolling the dice ({passes})...")
    subprocess.run([ "python", "twist.py"])  
    

    time.sleep(2)  # optional pause

    print("Documenting...")
    subprocess.run(["python", "takephoto.py"])

    time.sleep(1)  # optional pause
    passes+=1

print("Processing Data...")
subprocess.run(["python", "readdice.py"])  