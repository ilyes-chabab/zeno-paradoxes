def paradoxDichotomy(initialDistance, tolerance):
    remainingDistance = initialDistance
    distanceTravelled = 0
    steps = 0
    l = []

    while remainingDistance > tolerance:
        steps += 1
        remainingDistance /= 2
        distanceTravelled += remainingDistance
        l.append(remainingDistance)
        print(l)
    return l
        # if mode == "GUI":
        #     for i in range(20):
        #         l.append(remainingDistance)
        #         print(i)
        #     return l
        # elif mode == "CLI":
        #     print(
        #         f"Step {steps}: Remaining distance = {remainingDistance:.10f}, Distance travelled = {distanceTravelled:.10f}"
        #     )
        # print(f"\nFinal result: {remainingDistance:.10f}")
        # print(f"Steps neccesary : {steps}")
        # print(f"Total distance covered : {distanceTravelled:.10f}")


# Parameters
initialDistance = 800.0  # Total distance to cover
tolerance = 0.00240  # Tolerance to stop the simulation

if __name__ == "__main__":

    # paradoxDichotomy(initialDistance, tolerance, mode='CLI') # Calling the function

    print(paradoxDichotomy(initialDistance, tolerance))
