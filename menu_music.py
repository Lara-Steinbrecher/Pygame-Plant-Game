from pygame import mixer

def background_music():
    mixer.init()
    mixer.music.load('assets//musica//PyGameBGMusic.wav')
    mixer.music.play(loops=-1,fade_ms=700)
    mixer.music.set_volume(0.7)

def menu_music():
    mixer.init()
    mixer.music.load('assets//musica//MENU_SCREEN_BG.mp3')
    mixer.music.play(loops=-1,fade_ms=700)
    mixer.music.set_volume(0.7)

def aplastar_gusano():
    mixer.music.load('assets//musica//aplastargusano.mp3')
    mixer.music.play(loops=1,fade_ms=700)
    mixer.music.set_volume(0.7)

def choque_obj():
    mixer.music.load('assets//musica//choqueobj.mp3')
    mixer.music.play(loops=1,fade_ms=700)
    mixer.music.set_volume(0.7)


def saltito():
    mixer.music.load('assets//musica//saltito.mp3')
    mixer.music.play(loops=1,fade_ms=700)
    mixer.music.set_volume(0.7)

def win_sound():
    mixer.music.load('assets//musica//YOUWIN.mp3')
    mixer.music.play(loops=1,fade_ms=700)
    mixer.music.set_volume(0.7)

def game_over_sound():
    mixer.music.load('assets\musica\gameoversoundeffect.mp3')
    mixer.music.play(loops=1,fade_ms=700)
    mixer.music.set_volume(0.7)

def stop_music():
    mixer.music.stop()
