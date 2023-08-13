# Para cada partido del equipo B, calcula el número total de partidos del
# equipo A en los que el equipo A ha marcado menos o igual que el número de goles marcados
# por el equipo B en ese partido.



equipoA = [2, 10, 5, 4, 8]
equipoB = [2, 10, 5, 4, 8]


def counts(equipoA, equipoB):

    resultado=[]
    
    for valor_partidoB in  equipoB:

        gol_menor_partido=0

        for valor_partidoA in equipoA:

            if  valor_partidoA <= valor_partidoB:
                
                gol_menor_partido = gol_menor_partido+1
            
        resultado.append(gol_menor_partido)
        
    return resultado

print(counts(equipoA,equipoB))