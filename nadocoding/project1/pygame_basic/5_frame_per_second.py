import pygame

pygame.init()  # 초기화(필수)

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("공 맞추기") # 게임이름

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기  # \는 \\나 /로 바꿔야함
background = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)         # 화면 가로 절반 위치
character_y_pos = screen_height - character_height           # 화면 세로 가장 아래 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(10) # 게임 fps 설정

    print("fps : "+ str(clock.get_fps()))

    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False           # 게임 진행중이 아님
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤(지정안할 시 멈추지 않음)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt # * dt를 통해 프레임에 따른 속도차이 완화(거의 0)
    character_y_pos += to_y * dt

    # 가로세로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # screen.fill((0,0,255))          # RGB 색 채워넣기로 배경 이미지 대체 가능
    screen.blit(background, (0,0))    # 왼쪽 위 기준
    screen.blit(character, (character_x_pos, character_y_pos)) # 좌표 기준으로 그리기 때문에 계산
    pygame.display.update()           # 게임화면 업데이트 (주기적으로 실행 필수)

# 게임 종료
pygame.quit()