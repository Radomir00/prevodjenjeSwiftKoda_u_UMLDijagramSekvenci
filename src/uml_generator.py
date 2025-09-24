import os
import re
import shutil
import subprocess
from typing import Iterable, Optional

PLANTUML_JAR_CANDIDATES = ["tools/plantuml.jar", "plantuml.jar"]

def _find_plantuml_jar() -> Optional[str]:
    for c in PLANTUML_JAR_CANDIDATES:
        if os.path.exists(c):
            return c
    return None

_ALIAS_CLEAN_RE = re.compile(r"[^A-Za-z0-9_\.]")  # strogo za alias
def _alias(name: str) -> str:
    s = name or "Actor"
    s = _ALIAS_CLEAN_RE.sub("_", s)
    if s[0].isdigit():
        s = "_" + s
    return s

def to_plantuml(events: Iterable, title: Optional[str] = None) -> str:
    participants_order, seen = [], set()

    def norm_name(n: str) -> str:
        return n if n and n != "Global" else "System"

    def touch(name: str):
        n = norm_name(name)
        if n not in seen:
            seen.add(n)
            participants_order.append(n)

    for e in events:
        touch(e.sender)
        touch(e.receiver)

    lines = []
    if title:
        lines.append(f"title {title}")
    lines += [
        "hide footbox",
        "autonumber",
        "skinparam ParticipantPadding 8",
        "skinparam BoxPadding 8",
        "skinparam ArrowThickness 1",
        "skinparam SequenceMessageAlign center",
    ]

    for p in participants_order:
        lines.append(f'participant {_alias(p)} as "{p}"')

    created = set()

    for e in events:
        s_name = norm_name(e.sender)
        r_name = norm_name(e.receiver)

        s = _alias(s_name)
        r = _alias(r_name)
        kind = getattr(e, "kind", "sync")

        if kind == "create":
            if r_name not in created and r_name != "System":
                lines.append(f"create {r}")
                created.add(r_name)
            lines.append(f'{s} -> {r} ++ : {e.message}')
            continue
        if kind == "return":
            lines.append(f'{r} -->> {s} : {e.message}')
            continue

        lines.append(f'{s} -> {r} : {e.message}')

    return "\n".join(lines)

def generate_uml_image(plantuml_inner_code: str, base_name: str, output_folder: str = "output", fmt: str = "png") -> None:
    os.makedirs(output_folder, exist_ok=True)
    if not shutil.which("java"):
        print("[GREŠKA] Java nije instalirana ili nije u PATH-u.")
        return
    jar = _find_plantuml_jar()
    if not jar:
        print("[GREŠKA] Nije pronađen plantuml.jar (probano: tools/plantuml.jar, ./plantuml.jar).")
        return

    puml_path = os.path.join(output_folder, f"{base_name}.puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write("@startuml\n")
        f.write(plantuml_inner_code)
        f.write("\n@enduml\n")

    try:
        subprocess.run(
            ["java", "-jar", jar, f"-t{fmt}", puml_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        print("[GREŠKA] PlantUML nije uspio da rendere dijagram.")
        if e.stderr:
            print(e.stderr.strip())
        print(f"Provjeri sintaksu u: {puml_path}")
        return

    print(f"Dijagram generisan: {os.path.join(output_folder, base_name + '.' + fmt)}")
