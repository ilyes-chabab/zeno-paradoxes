def paradoxDichotomy(initialDistance, tolerance):
    remainingDistance = initialDistance
    distanceTravelled = 0
    steps = 0

    while remainingDistance > tolerance:
        steps += 1
        remainingDistance /= 2
        distanceTravelled += remainingDistance
        print(f"Étape {steps}: Distance restante = {remainingDistance:.10f}, Distance parcourue = {distanceTravelled:.10f}")
    
    print(f"\nRésultat final:")
    print(f"Nombre d'étapes nécessaires : {steps}")
    print(f"Distance totale parcourue : {distanceTravelled:.10f}")

# Parameters
initialDistance = 1.0  # Total distance to cover
tolerance = 0.0001  # Tolerance to stop the simulation

# Calling the function
paradoxDichotomy(initialDistance, tolerance)
