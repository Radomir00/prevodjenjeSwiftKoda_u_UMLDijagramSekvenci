# src/main.py
import os
import sys
import glob
from antlr4 import FileStream, CommonTokenStream
from src.antlr_gen.SwiftLexer import SwiftLexer
from src.antlr_gen.SwiftParser import SwiftParser
from src.seq_collector import SeqCollector
from src.uml_generator import to_plantuml, generate_uml_image
from src.semantic_analyzer import SemanticAnalyzer   # uključena semantika

EXAMPLES_DIR = "examples"
OUTPUT_DIR = "output"

def iter_inputs(args):
    if not args:
        yield from sorted(glob.glob(os.path.join(EXAMPLES_DIR, "*.swift")))
        return
    for a in args:
        if os.path.isdir(a):
            yield from sorted(glob.glob(os.path.join(a, "*.swift")))
        else:
            if not os.path.isfile(a):
                cand = os.path.join(EXAMPLES_DIR, a)
                a = cand if os.path.isfile(cand) else a
            if os.path.isfile(a):
                yield a
            else:
                print(f"[WARN] Preskačem, ne postoji: {a}")

def _parse_with_start_rule(parser):
    for name in ["compilationUnit", "sourceFile", "file", "program", "start", "unit", "topLevel"]:
        fn = getattr(parser, name, None)
        if callable(fn):
            return fn()
    raise RuntimeError(f"Nema start pravila u SwiftParser-u. Pravila: {getattr(type(parser), 'ruleNames', [])}")

def process_swift_file(path: str) -> None:
    input_stream = FileStream(path, encoding="utf-8")
    lexer = SwiftLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = SwiftParser(tokens)
    tree = _parse_with_start_rule(parser)

    # SEMANTIČKA ANALIZA – samo ispisuje greške
    analyzer = SemanticAnalyzer()
    errors = analyzer.analyze(tree)
    if errors:
        print(f"[SEMANTIKA] Upozorenja/greške u: {path}")
        for e in errors:
            print(" -", e)

    # Kolekcija sekvenci
    collector = SeqCollector()
    collector.visit(tree)

    # Render
    base = os.path.splitext(os.path.basename(path))[0]
    uml_inner = to_plantuml(collector.events, title=f"Sequence: {base}")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generate_uml_image(uml_inner, base_name=base, output_folder=OUTPUT_DIR)

def main(argv):
    inputs = list(iter_inputs(argv[1:]))
    if not inputs:
        print(f"Nema ulaza. Stavi .swift fajlove u '{EXAMPLES_DIR}/' ili prosledi putanje.")
        return 1
    for p in inputs:
        print(f"Generišem dijagram za: {p}")
        process_swift_file(p)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
