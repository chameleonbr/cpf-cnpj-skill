import argparse
import re
import sys

def format_cpf(cpf: str) -> str:
    cpf = re.sub(r'[^0-9]', '', str(cpf))
    if len(cpf) != 11:
        raise ValueError("CPF must have exactly 11 digits.")
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format a CPF.")
    parser.add_argument("cpf", help="The CPF to format.")
    args = parser.parse_args()
    
    try:
        formatted = format_cpf(args.cpf)
        print(formatted)
        sys.exit(0)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
