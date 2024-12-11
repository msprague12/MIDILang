from textx import metamodel_from_file
from mido import MidiFile, MidiTrack, Message, MetaMessage

# MIDI utilities
note_to_midi = {
    'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5,
    'F#': 6, 'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11
}

instrument_mapping = {
    "acoustic_grand_piano": 0,
    "bright_acoustic_piano": 1,
    "electric_grand_piano": 2,
    "honky_tonk_piano": 3,
    "electric_piano_1": 4,
    "electric_piano_2": 5,
    "harpsichord": 6,
    "clavinet": 7,

    # Chromatic Percussion
    "celesta": 8,
    "glockenspiel": 9,
    "music_box": 10,
    "vibraphone": 11,
    "marimba": 12,
    "xylophone": 13,
    "tubular_bells": 14,
    "dulcimer": 15,

    # Organs
    "drawbar_organ": 16,
    "percussive_organ": 17,
    "rock_organ": 18,
    "church_organ": 19,
    "reed_organ": 20,
    "accordion": 21,
    "harmonica": 22,
    "tango_accordion": 23,

    # Guitars
    "acoustic_guitar_nylon": 24,
    "acoustic_guitar_steel": 25,
    "electric_guitar_jazz": 26,
    "electric_guitar_clean": 27,
    "electric_guitar_muted": 28,
    "overdriven_guitar": 29,
    "distortion_guitar": 30,
    "guitar_harmonics": 31,

    # Bass
    "acoustic_bass": 32,
    "electric_bass_finger": 33,
    "electric_bass_pick": 34,
    "fretless_bass": 35,
    "slap_bass_1": 36,
    "slap_bass_2": 37,
    "synth_bass_1": 38,
    "synth_bass_2": 39,

    # Strings
    "violin": 40,
    "viola": 41,
    "cello": 42,
    "contrabass": 43,
    "tremolo_strings": 44,
    "pizzicato_strings": 45,
    "orchestral_harp": 46,
    "timpani": 47,

    # Ensemble
    "string_ensemble_1": 48,
    "string_ensemble_2": 49,
    "synth_strings_1": 50,
    "synth_strings_2": 51,
    "choir_aahs": 52,
    "voice_oohs": 53,
    "synth_choir": 54,
    "orchestra_hit": 55,

    # Brass
    "trumpet": 56,
    "trombone": 57,
    "tuba": 58,
    "muted_trumpet": 59,
    "french_horn": 60,
    "brass_section": 61,
    "synth_brass_1": 62,
    "synth_brass_2": 63,

    # Reeds
    "soprano_sax": 64,
    "alto_sax": 65,
    "tenor_sax": 66,
    "baritone_sax": 67,
    "oboe": 68,
    "english_horn": 69,
    "bassoon": 70,
    "clarinet": 71,

    # Pipe
    "piccolo": 72,
    "flute": 73,
    "recorder": 74,
    "pan_flute": 75,
    "blown_bottle": 76,
    "shakuhachi": 77,
    "whistle": 78,
    "ocarina": 79,

    # Synth Lead
    "lead_1_square": 80,
    "lead_2_sawtooth": 81,
    "lead_3_calliope": 82,
    "lead_4_chiff": 83,
    "lead_5_charang": 84,
    "lead_6_voice": 85,
    "lead_7_fifths": 86,
    "lead_8_bass_lead": 87,

    # Synth Pad
    "pad_1_new_age": 88,
    "pad_2_warm": 89,
    "pad_3_polysynth": 90,
    "pad_4_choir": 91,
    "pad_5_bowed": 92,
    "pad_6_metallic": 93,
    "pad_7_halo": 94,
    "pad_8_sweep": 95,

    # Synth Effects
    "fx_1_rain": 96,
    "fx_2_soundtrack": 97,
    "fx_3_crystal": 98,
    "fx_4_atmosphere": 99,
    "fx_5_brightness": 100,
    "fx_6_goblins": 101,
    "fx_7_echoes": 102,
    "fx_8_sci_fi": 103,

    # Ethnic
    "sitar": 104,
    "banjo": 105,
    "shamisen": 106,
    "koto": 107,
    "kalimba": 108,
    "bagpipe": 109,
    "fiddle": 110,
    "shanai": 111,

    # Percussion
    "tinkle_bell": 112,
    "agogo": 113,
    "steel_drums": 114,
    "woodblock": 115,
    "taiko_drum": 116,
    "melodic_tom": 117,
    "synth_drum": 118,
    "reverse_cymbal": 119,

    # Sound Effects
    "guitar_fret_noise": 120,
    "breath_noise": 121,
    "seashore": 122,
    "bird_tweet": 123,
    "telephone_ring": 124,
    "helicopter": 125,
    "applause": 126,
    "gunshot": 127
}

# Default instrument
DEFAULT_INSTRUMENT = "acoustic_grand_piano"

def note_to_midi_value(note):
    #Convert note name to MIDI number
    letter, octave = note[:-1], int(note[-1])
    return 12 * (octave + 1) + note_to_midi[letter]

duration_to_ticks = {
    'whole': 1920,
    'half': 960,
    'quarter': 480,
    'eighth': 240,
    'sixteenth': 120,
    'dotted_half': int(960 + 960 / 2),  
    'dotted_quarter': int(480 + 480 / 2) 
}

class MusicInterpreter:
    def __init__(self, output_filename='JingleBells.mid'):
        self.midi = MidiFile()
        self.tracks = {}  #Map instruments to their respective tracks
        self.tempo = 500000  #Set Default tempo: 120 BPM
        self.channel_map = {}  #Map instrument names to MIDI channels
        self.current_channel = 0  #Start with channel 0
        self.output_filename = output_filename
    
    def interpret(self, model):
            for statement in model.statements:
                if statement.__class__.__name__ == 'Tempo':
                    self.set_tempo(statement.value)
                elif statement.__class__.__name__ == 'Instrument':
                    self.set_instrument(statement.name)
                elif statement.__class__.__name__ == 'Note':
                    self.play_note(statement.name, statement.duration)
                elif statement.__class__.__name__ == 'Chord':
                    self.play_chord(statement.notes, statement.duration)
                elif statement.__class__.__name__ == 'Rest':
                    self.add_rest(statement.duration)
                elif statement.__class__.__name__ == 'Repeat':
                    for _ in range(statement.count):
                        self.interpret(statement)  

    def set_tempo(self, bpm):
        #Set the tempo for all tracks
        self.tempo = 60000000 // bpm  # Convert BPM to microseconds per beat
        #Add tempo to all tracks
        for track in self.tracks.values():
            track.append(MetaMessage('set_tempo', tempo=self.tempo))
        print(f"Set tempo to {bpm} BPM.")

    def set_instrument(self, instrument_name):
        #Assign a unique channel for each instrument
        if instrument_name.lower() not in self.channel_map:
            self.channel_map[instrument_name.lower()] = self.current_channel
            self.current_channel += 1

        #Retrieve or create a track for the instrument
        if instrument_name.lower() not in self.tracks:
            track = MidiTrack()
            self.midi.tracks.append(track)
            self.tracks[instrument_name.lower()] = track
            #Add tempo to the new track
            track.append(MetaMessage('set_tempo', tempo=self.tempo))
        else:
            track = self.tracks[instrument_name.lower()]

        #Send program change to the track's channel
        channel = self.channel_map[instrument_name.lower()]
        program_number = instrument_mapping.get(instrument_name.lower(), instrument_mapping[DEFAULT_INSTRUMENT])
        track.append(Message('program_change', program=program_number, channel=channel))

        self.instrument = instrument_name
        print(f"Set instrument to {instrument_name} on channel {channel}.")

    def play_note(self, note, duration):
        track = self.tracks[self.instrument.lower()]  #Use the correct track
        channel = self.channel_map[self.instrument.lower()]  #Use the correct channel
        midi_note = note_to_midi_value(note)
        ticks = duration_to_ticks[duration]
        track.append(Message('note_on', note=midi_note, velocity=64, time=0, channel=channel))
        track.append(Message('note_off', note=midi_note, velocity=64, time=ticks, channel=channel))
        print(f"Played note {note} for {duration} on {self.instrument}.")

    def play_chord(self, notes, duration):
        track = self.tracks[self.instrument.lower()]  #Use the correct track
        channel = self.channel_map[self.instrument.lower()]  #Use the correct channel
        ticks = duration_to_ticks[duration]
        for note in notes:
            midi_note = note_to_midi_value(note)
            track.append(Message('note_on', note=midi_note, velocity=64, time=0, channel=channel))
        for note in notes:
            midi_note = note_to_midi_value(note)
            track.append(Message('note_off', note=midi_note, velocity=64, time=ticks, channel=channel))
        print(f"Played chord {', '.join(notes)} for {duration} on {self.instrument}.")

    def add_rest(self, duration):
        track = self.tracks[self.instrument.lower()]  #Use the correct track
        channel = self.channel_map[self.instrument.lower()]  #Use the correct channel
        ticks = duration_to_ticks[duration]
        track.append(Message('note_off', velocity=0, time=ticks, channel=channel))
        print(f"Added rest for {duration}.")

    
    def save(self):
        self.midi.save(self.output_filename)
        print(f"Saved MIDI file to {self.output_filename}.")

#Main program
def main():
    music_mm = metamodel_from_file('midi.tx')
    model = music_mm.model_from_file('Jingle.ms')

    interpreter = MusicInterpreter()
    interpreter.interpret(model)
    interpreter.save()

if __name__ == "__main__":
    main()



