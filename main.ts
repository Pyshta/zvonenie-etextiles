let cyklus = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    music.setVolume(160)
    cyklus = 200
    for (let index = 0; index < cyklus; index++) {
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(349, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(262, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(392, music.beat(BeatFraction.Whole))
        music.rest(music.beat(BeatFraction.Double))
    }
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    cyklus = 0
    music.setVolume(0)
})
