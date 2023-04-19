import pygame
from random import *
##########################################################################################################################################
pygame.init()  # 초기화(필수)

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()
##########################################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)
background = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/똥 피하기 게임/background.png")
character = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/똥 피하기 게임/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height
enemy = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/똥 피하기 게임/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randrange(0, int(screen_width - enemy_width))
enemy_y_pos = 0
character_to_x = 0
enemy_to_y = 0
character_speed = 10
enemy_speed = 13
game_font = pygame.font.Font(None, 40)
start_ticks = pygame.time.get_ticks() 
start_time = 0



# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임 fps 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False   
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤(지정안할 시 멈추지 않음)
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
         
    character_x_pos += character_to_x
    enemy_y_pos += enemy_speed

    # 3. 게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    elif enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = randrange(0, int(screen_width - enemy_width))

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        running = False

    # 5. 화면 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # 경과시간(ms)을 초 단위로 표시
    timer = game_font.render(str(int(elapsed_time)), True, (255, 255, 255)) # 출력할 정보, True, 글자 색상
    screen.blit(timer, (10,10))

    pygame.display.update()  # 게임화면 업데이트 (주기적으로 실행 필수)

pygame.time.delay(2000)

# 게임 종료
pygame.quit()