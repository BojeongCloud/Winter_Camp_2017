import pygame

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Circular Wave")

done = False
waves = []

class Wave():
    def __init__(self, pos):
        self.pos = pos
        self.radius = 2
        self.speed = 5
        self.color = (0, 255, 100)
        self.width = 2

    def propagate(self):
        # 원이 일정하게 커지도록 할 수 있는 적당한 명령어를 입력하세요 (1줄)

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            self.pos,
            self.radius,
            self.width
        )

    def is_stable(self):
        if self.radius > max(screen_width, screen_height):
            # 적당한 명령어를 입력하세요 (1줄)
        else:
            # 적당한 명령어를 입력하세요 (1줄)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 윈도우 기준으로 우측 상단 X 버튼을 누르면 종료되도록 적당한 명령어를 입력하세요 (1줄)

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            waves.append(Wave(pos))

    screen.fill((0, 0, 0))
    for i in waves:
        if i.is_stable():
            waves.remove(i)
        else:
            # 적당한 명령어를 입력하세요 (2줄)

    pygame.display.flip()