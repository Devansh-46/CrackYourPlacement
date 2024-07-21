import re

token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),  # Integer or decimal number
    ('ASSIGN',   r'='),            # Assignment operator
    ('END',      r';'),            # Statement terminator
    ('ID',       r'[A-Za-z]+'),    # Identifiers
    ('OP',       r'[+\-*/()]'),    # Arithmetic operators and parentheses
    ('LBRACE',   r'\{'),           # Left brace
    ('RBRACE',   r'\}'),           # Right brace
    ('LE',       r'<='),           # Less than or equal to
    ('GE',       r'>='),           # Greater than or equal to
    ('LT',       r'<'),            # Less than
    ('GT',       r'>'),            # Greater than
    ('NEWLINE',  r'\n'),           # Line endings
    ('SKIP',     r'[ \t]+'),       # Skip over spaces and tabs
    ('MISMATCH', r'.'),            # Any other character
]

tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

keywords = {'if', 'else', 'while', 'def', 'return', 'print'}

def tokenize(code):
    tokens = []
    line_no = 1  # Initialize the line number
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value.upper()
        elif kind == 'NEWLINE':
            line_no += 1
            continue
        elif kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_no}')
        tokens.append((kind, value))
    return tokens
