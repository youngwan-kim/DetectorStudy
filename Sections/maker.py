import os

d_ = {
    "Interactions of Particles and Radiation with Matter":8,
    "Characteristic Properties of Detectors":3,
    "Units of Radiation Measurements and Radiation Sources":11,
    "Accelerators":5,
    "Main Physical Phenomena Used for Particle Detection":4,
    "Historical track detectors":3,
    "Track detectors":5,
    "Calorimetry":3,
    "Particle Identification":6,
    "Neutrino Detectors":6,
    "Momentum Measurement and Muon Detection":4,
    "Ageing and Radiation Effects":2,
    "Example of a General-purpose Detector: Belle":6,
    "Electronics":5,
    "Data analysis":4
}


i = 1
for chname in d_ :

    header = f"""
\\noindent\\rule{{7in}}{{2.8pt}}
\\section{{{chname}}}
    """

    with open(f"Ch{i}.tex",'w') as tex :
        tex.write(header)

    for j in range(1,d_[chname]+1) :
        prob = f"""
\\begin{{problem}}{{{i}.{j}}}

\\end{{problem}}
\\begin{{solution}}

\\end{{solution}}

\\noindent\\rule{{7in}}{{1.5pt}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
"""

        with open(f"Ch{i}.tex",'a') as tex :
            tex.write(prob)
    i+=1