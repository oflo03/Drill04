from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
ground = load_image('TUK_GROUND.png')
idle = [load_image('marin_idle_front_left.png'), load_image('marin_idle_front.png'),
        load_image('marin_idle_front_right.png'), load_image('marin_idle_back_left.png'),
        load_image('marin_idle_back.png'), load_image('marin_idle_back_right.png')]

run = [load_image('marin_run_front_left.png'), load_image('marin_run_front.png'),
        load_image('marin_run_front_right.png'), load_image('marin_run_back_left.png'),
        load_image('marin_run_back.png'), load_image('marin_run_back_right.png')]

def handle_events():
    global running, dir, face, isidle, frame
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_UP or event.key == SDLK_w:
                dir -= 3
            elif event.key == SDLK_LEFT or event.key == SDLK_a:
                dir -= 1
            elif event.key == SDLK_DOWN or event.key == SDLK_s:
                dir += 3
            elif event.key == SDLK_RIGHT or event.key == SDLK_d:
                dir += 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_UP or event.key == SDLK_w:
                dir += 3
            elif event.key == SDLK_LEFT or event.key == SDLK_a:
                dir += 1
            elif event.key == SDLK_DOWN or event.key == SDLK_s:
                dir -= 3
            elif event.key == SDLK_RIGHT or event.key == SDLK_d:
                dir -= 1


running = True
x, y = 400, 300
dir = 4 # back_left 0, back 1, back_right 2, left 3, idle 4, right 5, front_left 6, front 7, front_right 8,
face = 1 # front_left 0, front 1, front_right 2, back_left 3, back 4, back_right 5
frame = 0
idleFrame = 4
runFrame = 6

while running:
    clear_canvas()
    ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir == 4:
        idle[face].clip_draw(frame * idle[face].w // idleFrame, 0, idle[face].w // idleFrame, idle[face].h, x, y, idle[face].w // idleFrame * 4, idle[face].h * 4)
    else:
        run[face].clip_draw(frame * run[face].w // runFrame, 0, run[face].w // runFrame, run[face].h, x, y, run[face].w // runFrame * 4, run[face].h * 4)
    update_canvas()
    handle_events()
    if dir != 4:
        if dir % 3 == 0:
            x -= 10
            if face % 3 != 0:
                face = face - (face % 3)
        if dir % 3 == 2:
            x += 10
            if face % 3 != 2:
                face = face - (face % 3) + 2
        if dir < 3:
            y += 10
            face = dir + 3
        if dir > 5:
            y -= 10
            face = dir % 3
    frame = (frame + 1) % (idleFrame if dir == 4 else runFrame)
    delay(0.08)

close_canvas()
