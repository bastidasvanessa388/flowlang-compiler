import os
import subprocess

OUTPUT_FILE = "output.txt"

VALID_DIR = "tests/valid"
INVALID_DIR = "tests/invalid"

results = []

# ==========================================
# Función para ejecutar pruebas
# ==========================================

def run_test(file_path):

    # Copiar test actual a input.txt
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    with open("input.txt", "w", encoding="utf-8") as f:
        f.write(content)

    # Ejecutar compilador
    process = subprocess.run(
        ["python3", "main.py"],
        capture_output=True,
        text=True
    )

    return process.stdout + process.stderr


# ==========================================
# PRUEBAS VALIDAS
# ==========================================

results.append("========================================")
results.append("PRUEBAS VALIDAS")
results.append("========================================\n")

valid_files = sorted(os.listdir(VALID_DIR))

for filename in valid_files:

    path = os.path.join(VALID_DIR, filename)

    results.append(f"--- {filename} ---\n")

    output = run_test(path)

    results.append(output)
    results.append("\n")


# ==========================================
# PRUEBAS INVALIDAS
# ==========================================

results.append("========================================")
results.append("PRUEBAS INVALIDAS")
results.append("========================================\n")

invalid_files = sorted(os.listdir(INVALID_DIR))

for filename in invalid_files:

    path = os.path.join(INVALID_DIR, filename)

    results.append(f"--- {filename} ---\n")

    output = run_test(path)

    results.append(output)
    results.append("\n")


# ==========================================
# GUARDAR OUTPUT
# ==========================================

final_output = "\n".join(results)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(final_output)

print(f"Archivo generado: {OUTPUT_FILE}")
