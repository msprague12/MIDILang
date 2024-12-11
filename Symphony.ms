create song:
tempo 120

instrument "flute"
note C5 quarter
note D5 eighth
note E5 quarter
note F5 eighth
note G5 half
note A5 quarter
note G5 eighth
note F5 quarter
note E5 quarter
note D5 quarter
rest quarter
repeat 2 {
    note E5 quarter
    note G5 eighth
    note F5 quarter
    note C5 whole
}

instrument "violin"
chord { C4, E4, G4 } whole
chord { D4, F4, A4 } whole
chord { E4, G4, B4 } whole
chord { F4, A4, C5 } whole
repeat 1 {
    chord { G4, B4, D5 } whole
    chord { A4, C5, E5 } whole
    chord { F4, A4, D5 } whole
}

instrument "cello"
repeat 3 {
    note C2 whole
    note G2 whole
    note F2 whole
    note G2 whole
}

instrument "oboe"
note G5 quarter
note F5 eighth
note E5 quarter
note D5 eighth
note C5 half
rest quarter
repeat 1 {
    note B4 quarter
    note A4 eighth
    note G4 quarter
    note F4 whole
}

instrument "timpani"
repeat 4 {
    note C2 half
    note G2 half
}

instrument "acoustic_grand_piano"
note C4 quarter
note D4 eighth
note E4 quarter
note F4 eighth
note G4 quarter
note A4 eighth
note B4 quarter
note C5 half
chord { C4, E4, G4 } whole
rest quarter
repeat 1 {
    chord { F4, A4, C5 } half
    chord { G4, B4, D5 } half
}

instrument "string_ensemble_1"
chord { G3, B3, D4 } whole
chord { F3, A3, C4 } whole
chord { C3, E3, G3 } whole
chord { G3, D4, F4 } whole

end
