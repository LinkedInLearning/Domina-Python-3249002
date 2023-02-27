import subprocess


file_name = "bash_example.sh"
with open(file_name, "rb") as bash_file:
    script = bash_file.read()
    
print(f"Contenido del archivo bash\n{script}\n")

subprocess.call(script, shell=True)
