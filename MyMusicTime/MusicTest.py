import midi
import pygame
import os.path
import sys
import Image
import numpy as np

def PlayMidi(music_file):
    clock = pygame.time.Clock()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        # check if playback has finished
        clock.tick(30)


pygame.mixer.init()


path_name = "./screen_average_color/"

file_name = sys.argv[1] + "_avg_"

full_image_path = path_name+file_name

image_type = ".png"


# Instantiate a MIDI Pattern (contains a list of tracks)
pattern = midi.Pattern()
# Instantiate a MIDI Track (contains a list of MIDI events)
track = midi.Track()
# Append the track to the pattern
pattern.append(track)

iteration = 0

image_note = full_image_path+"%d" % iteration+image_type

on_list = []

if False:
    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=21, pitch=60)
    track.append(on)

    off  = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off  = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)

    on = midi.NoteOnEvent(tick=0, velocity=22, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=24, pitch=60)
    track.append(on)

    off  = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off  = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=60)
    track.append(on)

    off  = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off  = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=60)
    track.append(on)

    off = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=60)
    track.append(on)

    off = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=48)
    track.append(on)

    on = midi.NoteOnEvent(tick=0, velocity=20, pitch=60)
    track.append(on)

    off = midi.NoteOffEvent(tick=100, pitch=48)
    track.append(off)

    off = midi.NoteOffEvent(tick=100, pitch=60)
    track.append(off)



while os.path.exists(image_note):
    im = Image.open(image_note)

    pixel = np.array(im.getdata())

    p_tick = 0
    p_velocity = (20+iteration)%50
    p_pitch = (pixel[0][0] + pixel[0][1] + pixel[0][2])%112

    note_values = [p_tick, p_velocity, p_pitch]

    on_list.append(note_values)

    on = midi.NoteOnEvent(tick=p_tick, velocity=p_velocity, pitch=p_pitch)
    track.append(on)


    if iteration%3 == 0 and iteration != 0:
        last_tick = on_list[-1][0]
        for notes in on_list:
            off_pitch = notes[2]
            off = midi.NoteOffEvent(tick=50, pitch=off_pitch)
            track.append(off)

        on_list = []


    iteration += 1
    image_note = full_image_path + "%d" % iteration + image_type


if on_list != []:
    last_tick = on_list[-1][0]
    for notes in on_list:
        off_pitch = notes[2]
        off = midi.NoteOffEvent(tick=last_tick + 50, pitch=off_pitch)
        track.append(off)


# Add the end of track event, append it to the track
eot = midi.EndOfTrackEvent(tick=1)
track.append(eot)


# Print out the pattern
print (pattern)


midi_file_path = "./midi_files/" + sys.argv[1] + ".mid"

midi.write_midifile(midi_file_path, pattern)


PlayMidi(midi_file_path)