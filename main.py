cyklus = 0

def on_button_pressed_a():
    global cyklus
    music.set_volume(160)
    cyklus = 200
    for index in range(cyklus):
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.play_tone(494, music.beat(BeatFraction.WHOLE))
        music.play_tone(294, music.beat(BeatFraction.WHOLE))
        music.play_tone(349, music.beat(BeatFraction.WHOLE))
        music.play_tone(440, music.beat(BeatFraction.WHOLE))
        music.play_tone(262, music.beat(BeatFraction.WHOLE))
        music.play_tone(330, music.beat(BeatFraction.WHOLE))
        music.play_tone(392, music.beat(BeatFraction.WHOLE))
        music.rest(music.beat(BeatFraction.DOUBLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global cyklus
    cyklus = 0
    music.set_volume(0)
input.on_button_pressed(Button.B, on_button_pressed_b)
