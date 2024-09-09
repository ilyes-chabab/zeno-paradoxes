def paradoxDichotomy_CLI(initialDistance, tolerance):
    remainingDistance = initialDistance
    distanceTravelled = 0
    steps = 0
    l = []

    while remainingDistance > tolerance:
        steps += 1
        remainingDistance /= 2
        distanceTravelled += remainingDistance
        print(f"Step {steps}: Remaining distance = {remainingDistance:.10f}, Distance travelled = {distanceTravelled:.10f}")
    print(f"\nFinal result: {remainingDistance:.10f}")
    print(f"Steps neccesary : {steps}")
    print(f"Total distance covered : {distanceTravelled:.10f}")

# Parameters
initialDistance = 800.0  # Total distance to cover
tolerance = 0.00800  # Tolerance to stop the simulation

if __name__ == "__main__":

    # paradoxDichotomy_GUI(initialDistance, tolerance)

    paradoxDichotomy_CLI(initialDistance, tolerance)
