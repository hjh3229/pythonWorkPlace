import pygame

pygame.init()  # 초기화(필수)

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 배경 이미지 불러오기  # \는 \\나 /로 바꿔야함
background = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/pygame_basic/background.png")

# 스프라이트(캐릭터) 불러오기
character = pygame.image.load("C:/Users/한지훈/OneDrive/바탕 화면/pythonworkspace/나도코딩/활용1/pygame_basic/character.png")
character_size = character.get_rect().size # 이미지의 크기 구해옴
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width / 2         # 화면 가로 절반 위치
character_y_pos = screen_height            # 화면 세로 가장 아래 위치
 
# 화면 타이틀 설정
pygame.display.set_caption("공 맞추기") # 게임이름

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생 하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False           # 게임 진행중이 아님
    # screen.fill((0,0,255))          # RGB 색 채워넣기로 배경 이미지 대체 가능
    screen.blit(background, (0,0))    # 왼쪽 위 기준
    screen.blit(character, (character_x_pos-35, character_y_pos-70)) # 좌표 기준으로 그리기 때문에 계산
    pygame.display.update()           # 게임화면 업데이트 (주기적으로 실행 필수)

# 게임 종료
pygame.quit()