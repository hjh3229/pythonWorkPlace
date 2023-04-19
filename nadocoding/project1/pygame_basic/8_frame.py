import pygame
##########################################################################################################################################
pygame.init()  # 초기화(필수)

# 화면크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("게임 이름")

# FPS
clock = pygame.time.Clock()
##########################################################################################################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 폰트 등)

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임 fps 설정
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            running = False           

    # 3. 게임 캐릭터 위치 정의

    # 4. 충돌 처리

    # 5. 화면 그리기
    
    pygame.display.update()  # 게임화면 업데이트 (주기적으로 실행 필수)

# 게임 종료
pygame.quit()