replay = 0

while replay != 2: 
    print("\n--------CONVERSOR--------\n")

    segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
    total_segs = int(segundos_str)

    dia = total_segs // (3600*24)
    horas = (total_segs // 3600) - (dia * 24)
    segs_restantes = total_segs % 3600
    minutos = segs_restantes // 60
    segs_restantes_final = segs_restantes % 60

    print("\n", total_segs, "equivalem a...")
    print("\n", dia, "dias,", horas, "horas,", minutos, "minutos e", segs_restantes_final, "segundos.")

    replay= int(input("\nDeseja realizar outra conversão? (1 - Nova conversão/ 2 - Sair): "))

while replay == 2:
    print("\nEncerrando conversor......\n")
    exit ()