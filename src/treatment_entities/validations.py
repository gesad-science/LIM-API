from src.treatment_entities.entities import Treatmentinput

def len_test(input:Treatmentinput)->bool:
    if len(input.value) <= 0:
        return False
    return True

def paragraph_test(input:Treatmentinput)->bool:
    if '\n' in input.value:
        return False