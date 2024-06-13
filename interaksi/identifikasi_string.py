import math
import re
# Fungsi untuk mengganti operator yang dipahami manusia dengan operator Python
def ganti_operator_yang_dipahami_manusia(ekspresi):
    replacements = {
        '^': '**', 
        '\u00F7': '/', 
        'x': '*',
        u"\u2212": '-',
        ',':'.'
    }
    for human_op, python_op in replacements.items():
        ekspresi = ekspresi.replace(human_op, python_op)
    return ekspresi

# Fungsi untuk mengeksekusi string dengan fungsi trigonometri dan operator matematika lainnya
def eval_mtk(ekspresi):
    ekspresi = ganti_operator_yang_dipahami_manusia(ekspresi)
    local_context = {
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'pi': math.pi,
        'e': math.e,
        'exp': math.exp,
        'log': math.log,
        'sqrt': math.sqrt,
        'pow': math.pow,
        'abs': abs,
        'round': round,
        'floor': math.floor,
        'ceil': math.ceil,
        'factorial': math.factorial
    }
    return eval(ekspresi, {"__builtins__": None}, local_context)

def pisah_bilangan_negatif(ekspresi):
    ekspresi = ekspresi.replace(u"\u2212", "-")
    def replacer(match):
        if match.group(0).startswith('(-'):
            return match.group(0)
        return f"(-{match.group(1)})"
    
    def remove_parentheses(match):
        return match.group(1) + match.group(2)
    ekspresi = re.sub(r'(?<!\()-(\d+)', replacer, ekspresi)
    ekspresi = re.sub(r'(\d)\((-?\d+)\)', remove_parentheses, ekspresi)
    return ekspresi.replace("-", u"\u2212")