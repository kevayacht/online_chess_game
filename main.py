import pygame


def gui_setup():
    pygame.init()

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 250)

    size = (500, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Online Chess Game")

    # carry on until the user clicks the close button,
    # or a event based condition is met?
    running = True

    clock = pygame.time.Clock()  # use to control how fast the screen updates.

    # main event loop.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # game logic of some kind

        # drawing code.
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, [250, 250], 75)
        pygame.display.flip()

    pygame.quit()


def main():
    gui_setup()

    # pygame.quit()


if __name__ == "__main__":
    main()
