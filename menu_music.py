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
    channel1 = mixer.Channel(0)
    effect = mixer.Sound('assets//musica//aplastargusano.mp3')
    channel1.play(effect)

def choque_obj():
    channel1 = mixer.Channel(0)
    effect = mixer.Sound('assets//musica//choqueobj.mp3')
    channel1.play(effect)


def saltito():
    channel2 = mixer.Channel(1)
    effect = mixer.Sound('assets//musica//saltito.mp3')
    channel2.play(effect)

def win_sound():
    channel3 = mixer.Channel(2)
    effect = mixer.Sound('assets//musica//YOUWIN.mp3')
    channel3.play(effect)
    

def game_over_sound():
    channel3 = mixer.Channel(2)
    effect = mixer.Sound('assets//musica//gameoversoundeffect.mp3')
    channel3.play(effect)

def stop_music():
    mixer.music.stop()
