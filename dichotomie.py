def paradoxDichotomy(initialDistance, tolerance):
    remainingDistance = initialDistance
    distanceTravelled = 0
    steps = 0

    while remainingDistance > tolerance:
        steps += 1
        remainingDistance /= 2
        distanceTravelled += remainingDistance
        print(f"Step {steps}: Remaining distance = {remainingDistance:.10f}, Distance travelled = {distanceTravelled:.10f}")
    
    print(f"\nFinal result:")
    print(f"Steps neccesary : {steps}")
    print(f"Total distance covered : {distanceTravelled:.10f}")

# Parameters
initialDistance = 1.0  # Total distance to cover
tolerance = 0.0001  # Tolerance to stop the simulation

# Calling the function
paradoxDichotomy(initialDistance, tolerance)
