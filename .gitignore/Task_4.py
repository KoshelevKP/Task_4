import os
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))

program = os.path.join(current_dir, "convert")

files = os.listdir(os.path.join(current_dir, "Source"))
print(files)

output_dir=os.path.join(current_dir, "Results")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in files:
    input_file = os.path.join(current_dir, "Source", file)
    output_file = os.path.join(current_dir, "Results", file)
    atributs = "-resize 200"
    task = program+" "+input_file+" "+atributs+" "+output_file
    print(task)
    subprocess.run(task)