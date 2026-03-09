import argparse
import re
import sys

def validate_cpf(cpf: str) -> bool:
    cpf = re.sub(r'[^0-9]', '', str(cpf))
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False
    
    # Calculate first digit
    sum_val = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digit1 = (sum_val * 10) % 11
    if digit1 == 10:
        digit1 = 0
    if str(digit1) != cpf[9]:
        return False
        
    # Calculate second digit
    sum_val = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digit2 = (sum_val * 10) % 11
    if digit2 == 10:
        digit2 = 0
    if str(digit2) != cpf[10]:
        return False
        
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a CPF.")
    parser.add_argument("cpf", help="The CPF to validate.")
    args = parser.parse_args()
    
    if validate_cpf(args.cpf):
        print("Valid CPF")
        sys.exit(0)
    else:
        print("Invalid CPF")
        sys.exit(1)
