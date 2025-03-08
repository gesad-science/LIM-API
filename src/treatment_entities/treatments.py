from src.treatment_entities.entities import Treatmentinput

def single_paragraph_treatment(input:Treatmentinput):
    values = input.value.split('\n')
    high_len=0
    high_idx=None
    for i, value in enumerate(values):
        if len(value) > high_len:
            high_len=len(value)
            high_idx=i

    if high_idx:
        input.value = values[high_idx]
    return input
    
def short_paragraph_treatment(input:Treatmentinput):
    values = input.value.split('\n')
    low_len=100000
    low_idx=None
    for i, value in enumerate(values):
        if len(value) < low_len:
            low_len=len(value)
            low_idx=i

    if low_idx:
        input.value = values[low_idx]
    return input
