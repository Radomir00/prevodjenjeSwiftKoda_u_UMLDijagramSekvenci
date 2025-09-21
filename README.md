
## (Opcionalno) Lokalni .venv (preporučeno)

**Windows (PowerShell):**
```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r .equirements.txt
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Ako ne želiš koristiti virtualno okruženje, može i bez aktivacije:  
> `py -3 -m pip install --user -r requirements.txt`


# Swift → UML Sequence (PlantUML)

Minimalni projekt (Python + ANTLR4) koji iz Swift koda izdvaja pozive i pravi UML **dijagram sekvenci** u PlantUML-u.

## Preduvjeti
- **Java 8+** (za PlantUML)
- **Python 3.10+**
- **ANTLR4** (tool + runtime za Python)
- **PlantUML** `plantuml.jar` (preuzmi i stavi u `tools/` ili koristi sistemski)

## Instalacija (lokalno)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Instaliraj ANTLR runtime (Python) i preuzmi `antlr-4.X-complete.jar` (npr. 4.13.1) u folder `tools/`:
```bash
mkdir -p tools
# preuzmi jar pa stavi u tools/
# npr. curl -L -o tools/antlr-4.13.1-complete.jar <URL_DO_ANTLR_JAR>
# preuzmi i plantuml.jar pa stavi u tools/
```

## Generisanje parsera
```bash
# generiši Python lexer/parser iz SwiftMini.g4
java -jar tools/antlr-4.13.1-complete.jar -Dlanguage=Python3 grammar/SwiftMini.g4 -o src/antlr_gen
```

## Pokretanje
```bash
# 1) Parsiraj, sakupi evente i napravi PlantUML (out/sequence.puml)
python src/main.py examples/sample.swift --puml out/sequence.puml

# 2) Renderuj PlantUML → PNG
java -jar tools/plantuml.jar out/sequence.puml
# dobićeš: out/sequence.png
```

## Struktura
```
swift_to_uml_sequence/
  .vscode/            # VS Code tasks/launch
  grammar/            # ANTLR gramatika (SwiftMini.g4)
  src/
    antlr_gen/        # (generisano) Kotlin/Swift parser/lexer od ANTLR-a
    main.py           # CLI ulaz
    seq_collector.py  # Visitor koji skuplja poruke
    uml_generator.py  # PlantUML generator
  tools/              # (ti dodaš) antlr jar i plantuml.jar
  examples/           # Swift primjeri
  out/                # izlazni .puml i .png
```

## Napomene
- Gramatika je **pojednostavljena** i hvata: `class`, `func`, `let/var`, `Type()`, `obj.method()`, i goli `func()` poziv.
- Lako se širi za `if/for/async`, `init`, `extension`, `protocol`.


## Brzo pokretanje (Windows PowerShell)
```powershell
# 1) instaliraj runtime
py -3 -m pip install --user -r .\requirements.txt

# 2) generiši ANTLR parser (lexer+parser)
java -jar .\tools\antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o .\src\antlr_gen .\grammar\SwiftLexer.g4 .\grammar\SwiftParser.g4

# 3) pokreni i renderuj
py -3 -m src.main .\examples\sample.swift
py -3 -m src.main .\examples\example_calls.swift
py -3 -m src.main .\examples\example_flow.swift
```
Dijagrami će biti u `output/`.
