import argparse
import re
import sys

def format_cnpj(cnpj: str) -> str:
    cnpj = re.sub(r'[^0-9]', '', str(cnpj))
    if len(cnpj) != 14:
        raise ValueError("CNPJ must have exactly 14 digits.")
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Format a CNPJ.")
    parser.add_argument("cnpj", help="The CNPJ to format.")
    args = parser.parse_args()
    
    try:
        formatted = format_cnpj(args.cnpj)
        print(formatted)
        sys.exit(0)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
