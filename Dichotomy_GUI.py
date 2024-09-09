import pygame


def compute_distances(initialDistance, tolerance):
    remainingDistance = initialDistance
    distanceTravelled = 0
    steps = 0
    l = []

    while remainingDistance > tolerance:
        steps += 1
        remainingDistance /= 2
        distanceTravelled += remainingDistance
        l.append(remainingDistance)
    return l


def main_dichotomy():
    pygame.init()

    initialDistance = 800
    tolerance = 0.05

    surf = pygame.display.set_mode((1200, 600))
    surf.fill((255, 255, 255))
    tree = pygame.image.load("image/arbre-removebg-preview.png").convert_alpha()
    newTree = pygame.transform.scale(tree, (350, 300))
    rock = pygame.image.load("image/cercle.png").convert_alpha()
    newRock = pygame.transform.scale(rock, (150, 100))

    surf.blit(newTree, (500, 150))
    l = compute_distances(initialDistance, tolerance)
    initialPosition = 500
    # surf.blit(newRock, (initialPosition, 250))
    for i in l:
        surf.blit(newRock, (initialPosition - i, 250))
        pygame.display.flip()
        pygame.time.wait(500)
    pygame.display.flip()


pygame.quit()

if __name__ == "__main__":
    main_dichotomy()
