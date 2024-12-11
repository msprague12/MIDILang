create song:
tempo 100

instrument "trumpet"
note E5 quarter
note E5 quarter
note E5 half
note E5 quarter
note E5 quarter
note E5 half
note E5 quarter
note G5 quarter
note C5 quarter
note D5 quarter
note E5 whole

repeat 1 {
    note F5 quarter
    note F5 quarter
    note F5 quarter
    note F5 quarter
    note F5 quarter
    note E5 quarter
    note E5 quarter
    note E5 quarter
    note E5 quarter
    note E5 quarter
    note D5 quarter
    note D5 quarter
    note E5 quarter
    note D5 quarter
    note G5 whole
}

instrument "violin"
repeat 2 {
    chord { C4, E4, G4 } quarter
    rest quarter
    chord { C4, E4, G4 } quarter
    rest quarter
    chord { F4, A4, C5 } quarter
    chord { G4, B4, D5 } half
}

instrument "tuba"
repeat 4 {
    note C3 half
    note G2 half
    note F2 half
    note G2 half
}

instrument "orchestral_harp"
chord { C4, E4, G4 } whole

end
