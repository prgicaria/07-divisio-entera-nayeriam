dividend = int(input("Introdueix el dividend (nombre enter): "))
divisor = int(input("Introdueix el divisor (nombre enter): "))

if divisor != 0:
    divisio = dividend/divisor
    quocient = dividend // divisor
    residu = dividend % divisor

    print(f"divisió : {dividend}/{divisor}")
    print(f"quocient : {quocient}")
    print(f"residu : {residu}")
else:
    print("Error: El divisor no pot ser zero.")
