import pygame

from assets import globals, scene

pygame.init()
#pygame.mixer.init() # add this line
pygame.mixer.init(44100, -16,2,2048)
screen = pygame.display.set_mode((globals.WINDOW_WIDTH, globals.WINDOW_HEIGHT))
pygame.display.set_caption('QPong')
clock = pygame.time.Clock()

from assets.resources import *
from assets import resources

#beep = load_sound_beep()
start = load_sound_start()

def main():

    # initialize game
    scene_manager = scene.SceneManager()
    scene_manager.push(scene.GameScene())
    #play_beep()
    pygame.mixer.Sound.play(start) 
    
    pygame.time.delay(1500)
    """
    gameover_text = "Welcome"
    font = resources.Font()
    text = font.replay_font.render(gameover_text, 5, globals.WHITE)
    text_pos = text.get_rect(center=(globals.WINDOW_WIDTH/2, globals.WIDTH_UNIT*22))
    screen.blit(text, text_pos)
    """
    while not scene_manager.exit:
        # update game
        scene_manager.update()
        # draw game
        scene_manager.draw(screen)
        # control framerate
        clock.tick(globals.TICKS)
        
if __name__ == '__main__':
    main()
