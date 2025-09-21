import os
import sys
from antlr4 import FileStream, CommonTokenStream
from .antlr_gen.SwiftLexer import SwiftLexer
from .antlr_gen.SwiftParser import SwiftParser

from .semantic_analyzer import SemanticAnalyzer
from .seq_collector import SeqCollector
from .uml_generator import to_plantuml, generate_uml_image

INPUT_FOLDER = "examples"
OUTPUT_FOLDER = "output"

def _resolve_input_path(fname: str) -> str:
    if os.path.isfile(fname):
        return fname
    return os.path.join(INPUT_FOLDER, fname)

def parse_swift_file(filename: str) -> str | None:
    input_stream = FileStream(filename, encoding="utf-8")
    lexer = SwiftLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SwiftParser(stream)
    tree = parser.program()

    analyzer = SemanticAnalyzer()
    errors = analyzer.analyze(tree)
    if errors:
        print("\n".join(errors))
        return None

    visitor = SeqCollector()
    visitor.visit(tree)

    uml_inner = to_plantuml(visitor.events, title=f"Sequence: {os.path.basename(filename)}")
    return uml_inner

def main():
    if len(sys.argv) < 2:
        print("Ispravno: python -m src.main file1.swift [file2.swift ...]")
        sys.exit(1)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for arg in sys.argv[1:]:
        input_path = _resolve_input_path(arg)
        if not os.path.isfile(input_path):
            print(f"[UPOZORENJE] Ne postoji fajl: {input_path}")
            continue

        base_name = os.path.splitext(os.path.basename(input_path))[0]
        print(f"Generišem dijagram za: {input_path}")

        uml_inner = parse_swift_file(input_path)
        if uml_inner is None:
            print(f"Preskačem '{input_path}' (semantičke greške).\n")
            continue

        generate_uml_image(uml_inner, base_name, output_folder=OUTPUT_FOLDER)

if __name__ == "__main__":
    main()
