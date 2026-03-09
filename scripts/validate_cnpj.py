import argparse
import re
import sys

def validate_cnpj(cnpj: str) -> bool:
    cnpj = re.sub(r'[^0-9]', '', str(cnpj))
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False
        
    # First digit
    weights1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_val = sum(int(cnpj[i]) * weights1[i] for i in range(12))
    rem = sum_val % 11
    digit1 = 0 if rem < 2 else 11 - rem
    if str(digit1) != cnpj[12]:
        return False
        
    # Second digit
    weights2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    sum_val = sum(int(cnpj[i]) * weights2[i] for i in range(13))
    rem = sum_val % 11
    digit2 = 0 if rem < 2 else 11 - rem
    if str(digit2) != cnpj[13]:
        return False
        
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate a CNPJ.")
    parser.add_argument("cnpj", help="The CNPJ to validate.")
    args = parser.parse_args()
    
    if validate_cnpj(args.cnpj):
        print("Valid CNPJ")
        sys.exit(0)
    else:
        print("Invalid CNPJ")
        sys.exit(1)
