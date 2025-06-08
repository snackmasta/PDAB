import schemdraw
from schemdraw.elements import lines

with schemdraw.Drawing(file='desalination_pid.svg') as d:
    # Ground Tank (as a labeled box using Container)
    d += lines.Dot(label='Ground Tank', at=(0, 0))
    d += lines.Line().right().length(2)
    # Intake Pump (as a labeled dot)
    d += lines.Dot(label='Intake Pump', at=(2, 0))
    d += lines.Line().right().length(2)
    # Pre-Treatment (as a labeled dot)
    d += lines.Dot(label='Pre-Treatment', at=(4, 0))
    d += lines.Line().right().length(2)
    # RO Pump (as a labeled dot)
    d += lines.Dot(label='RO Pump', at=(6, 0))
    d += lines.Line().right().length(2)
    # RO Membrane (as a labeled dot)
    d += lines.Dot(label='RO Membrane', at=(8, 0))
    d += lines.Line().right().length(2)
    # Transfer Pump (as a labeled dot)
    d += lines.Dot(label='Transfer Pump', at=(10, 0))
    d += lines.Line().right().length(2)
    # Roof Tank (as a labeled dot)
    d += lines.Dot(label='Roof Tank', at=(12, 0))
    # Brine/Reject line (down from RO Membrane)
    d += lines.Line().down().at((8, 0)).length(2)
    d += lines.Dot(label='Brine Discharge', at=(8, -2))

print('P&ID diagram saved as desalination_pid.svg')
