import random
import string

# ==============================
#  GENERADOR DE CONTRASEÑAS
# ==============================

print("=== GENERADOR DE CONTRASEÑAS ===")

# ---------- ENTRADA ----------
longitud = int(input("Ingrese la longitud de la contraseña: "))

usar_letras = input("¿Desea usar letras? (s/n): ").lower()
usar_numeros = input("¿Desea usar números? (s/n): ").lower()
usar_simbolos = input("¿Desea usar símbolos? (s/n): ").lower()

# ---------- PROCESAMIENTO ----------
caracteres = ""

if usar_letras == "s":
    caracteres += string.ascii_letters  # Letras mayúsculas y minúsculas

if usar_numeros == "s":
    caracteres += string.digits  # Números

if usar_simbolos == "s":
    caracteres += string.punctuation  # Símbolos

# ---------- VALIDACIÓN ----------
if caracteres == "":
    print("Error: No se puede generar una contraseña sin caracteres.")
else:
    contraseña = ""

    # ---------- BUCLE ----------
    for i in range(longitud):
        contraseña += random.choice(caracteres)

    # ---------- SALIDA ----------
    print("\nContraseña generada:")
    print(contraseña)
