# Prevođenje Swift koda u UML dijagram sekvenci

Alat koji iz **Swift** koda automatski generiše **UML dijagram sekvenci**. Koristi ANTLR (lexer/parser), “light” semantiku u Python-u i **PlantUML** za izlazni dijagram.

## Struktura projekta

```
projekat/
├── examples/               # Swift .swift fajlovi za testiranje
├── output/                 # Generisani .puml i .png fajlovi
├── grammar/                # ANTLR gramatike (SwiftLexer.g4, SwiftParser.g4)
├── src/
│   ├── antlr_gen/          # (GENERISANO) ANTLR Python fajlovi
│   ├── main.py             # Glavna skripta
│   ├── semantic_analyzer.py# Osnovna semantika (scope, nedef. imena)
│   ├── seq_collector.py    # Ekstrakcija create/call događaja
│   └── uml_generator.py    # PlantUML generisanje i render
├── tools/                  # antlr-4.x-complete.jar, plantuml.jar
└── requirements.txt
```

## Funkcionalnosti

* **Leksička i sintaksna analiza:** ANTLR gramatike za podskup Swifta
* **Semantika (osnovno):** nedefinisana imena, dvostruke deklaracije, jednostavne heuristike tipova
* **Generisanje dijagrama:** `create` i pozivi metoda/funkcija → PlantUML → `.png`

## Upotreba (kratko)

```
# generisanje ANTLR fajlova
java -jar tools/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/antlr_gen grammar/SwiftLexer.g4
java -jar tools/antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor -o src/antlr_gen -lib src/antlr_gen/grammar grammar/SwiftParser.g4

# pokretanje
python -m src.main examples/create_call.swift
```

**Napomena:** ako se detektuju semantičke greške, generisanje UML dijagrama se preskače.
