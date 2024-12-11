create song:
tempo 104

instrument "trumpet"
note G4 quarter
note G4 quarter
note G4 quarter
note E4 half
note B4 quarter
note G4 quarter
note E4 half
note B4 quarter
note G4 half

repeat 1 {
    note D5 quarter
    note D5 quarter
    note D5 quarter
    note E5 half
    note B4 quarter
    note F4 quarter
    note E4 half
    note B4 quarter
    note G4 half
}

instrument "french_horn"
chord { G3, B3, D4 } whole
chord { G3, B3, D4 } whole
chord { E3, G3, B3 } whole
chord { B3, D4, G4 } whole
repeat 1 {
    chord { D4, F4, A4 } whole
    chord { E3, G3, B3 } whole
    chord { B3, D4, G4 } whole
}

instrument "tuba"
repeat 2 {
    note G2 whole
    note E2 whole
    note B2 whole
    note G2 whole
}

instrument "violin"
note D5 quarter
note E5 quarter
note B4 quarter
note G4 quarter
rest quarter
note B4 quarter
note G4 quarter
note E4 quarter

instrument "string_ensemble_1"
chord { G3, B3, D4 } whole
chord { F3, A3, C4 } whole
chord { G3, B3, E4 } whole
chord { B3, D4, G4 } whole

end
