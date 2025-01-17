"""
This is the driver code for a synthsizer.
"""
from machine import I2S, Pin

keys = {
    letter: Pin(i, Pin.IN, Pin.PULL_UP)
    for i, letter in zip(range(4, 16), "C C# D D# E F F# G G# A A# B".split())
}

silence = bytes(100)

tones = {
    "C": silence,
    "C#": silence,
    "D": silence,
    "D#": silence,
    "E": silence,
    "F": b"\x00\x00_\x06\xae\x0c\xdd\x12\xdc\x18\x9b\x1e\r$#)\xd0-\t2\xc25\xf38\x93;\x9b=\x07?\xd2?\xfa?\x80?e>\xaa<V:l7\xf63\xfc/\x87+\xa4&_!\xc4\x1b\xe3\x15\xca\x0f\x89\t0\x03\xd0\xfcw\xf66\xf0\x1d\xea<\xe4\xa1\xde\\\xd9y\xd4\x04\xd0\n\xcc\x94\xc8\xaa\xc5V\xc3\x9b\xc1\x80\xc0\x06\xc0.\xc0\xf9\xc0e\xc2m\xc4\r\xc7>\xca\xf7\xcd0\xd2\xdd\xd6\xf3\xdbe\xe1$\xe7#\xedR\xf3\xa1\xf9",
    "F#": silence,
    "G": silence,
    "G#": silence,
    "A": silence,
    "A#": silence,
    "B": b'\x00\x00\xf9\x08\xc4\x116\x1a$"d)\xd3/Q5\xc19\x0c=#?\xfb?\x8f?\xe2=\xfb:\xeb6\xc41\xa2+\xa3$\xeb\x1c\xa1\x14\xee\x0b\xff\x02\x02\xfa"\xf1\x8e\xe8p\xe0\xf1\xd88\xd2g\xcc\x9a\xc7\xeb\xc3l\xc1)\xc0)\xc0l\xc1\xeb\xc3\x9a\xc7g\xcc8\xd2\xf1\xd8p\xe0\x8e\xe8"\xf1\x02\xfa\xff\x02\xee\x0b\xa1\x14\xeb\x1c\xa3$\xa2+\xc41\xeb6\xfb:\xe2=\x8f?\xfb?#?\x0c=\xc19Q5\xd3/d)$"6\x1a\xc4\x11\xf9\x08\x00\x00\x07\xf7<\xee\xca\xe5\xdc\xdd\x9c\xd6-\xd0\xaf\xca?\xc6\xf4\xc2\xdd\xc0\x05\xc0q\xc0\x1e\xc2\x05\xc5\x15\xc9<\xce^\xd4]\xdb\x15\xe3_\xeb\x12\xf4\x01\xfd\xfe\x05\xde\x0er\x17\x90\x1f\x0f\'\xc8-\x993f8\x15<\x94>\xd7?\xd7?\x94>\x15<f8\x993\xc8-\x0f\'\x90\x1fr\x17\xde\x0e\xfe\x05\x01\xfd\x12\xf4_\xeb\x15\xe3]\xdb^\xd4<\xce\x15\xc9\x05\xc5\x1e\xc2q\xc0\x05\xc0\xdd\xc0\xf4\xc2?\xc6\xaf\xca-\xd0\x9c\xd6\xdc\xdd\xca\xe5<\xee\x07\xf7',
}

try:
    audio_out = I2S(
        0,
        sck=Pin(16),
        ws=Pin(17),
        sd=Pin(18),
        mode=I2S.TX,
        bits=16,
        format=I2S.MONO,
        rate=22_050,
        ibuf=2000,
    )

    while True:
        for letter, pin in keys.items():
            if not pin.value():
                audio_out.write(tones[letter])
                break
        else:
            audio_out.write(silence)

finally:
    audio_out.deinit()
