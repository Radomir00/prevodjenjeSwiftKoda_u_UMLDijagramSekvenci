import os
import shutil
import subprocess

PLANTUML_JAR_CANDIDATES = ["tools/plantuml.jar", "plantuml.jar"]

def _find_plantuml_jar() -> str | None:
    for c in PLANTUML_JAR_CANDIDATES:
        if os.path.exists(c):
            return c
    return None

def to_plantuml(events, title: str = "Sequence (Swift -> UML)") -> str:
    order = []
    def touch(n):
        if n and n != "Global" and n not in order:
            order.append(n)

    for e in events:
        touch(e.sender)
        touch(e.receiver)

    lines = [
        "autonumber",
        "autoactivate on",
        "skinparam ArrowThickness 1",
        "skinparam ParticipantPadding 20",
        f"title {title}",
    ]
    for a in order:
        lines.append(f"participant {a}")

    for e in events:
        k = getattr(e, "kind", "sync")
        if k == "create":
            lines.append(f"create {e.receiver}")
            lines.append(f"{e.sender} -> {e.receiver} : {e.message}")
        elif k == "return":
            lines.append(f"{e.receiver} --> {e.sender} : return")
        else:
            lines.append(f"{e.sender} -> {e.receiver} : {e.message}")
    return "\n".join(lines)

def generate_uml_image(plantuml_inner_code: str, base_name: str, *, output_folder: str = "output") -> None:
    os.makedirs(output_folder, exist_ok=True)
    if not shutil.which("java"):
        print("[GREŠKA] Java nije instalirana ili nije dostupna u PATH-u.")
        return
    jar = _find_plantuml_jar()
    if not jar:
        print("[GREŠKA] Nije pronađen plantuml.jar (probano: tools/plantuml.jar i ./plantuml.jar)")
        return

    puml_path = os.path.join(output_folder, f"{base_name}.puml")
    with open(puml_path, "w", encoding="utf-8") as f:
        f.write("@startuml\n"); f.write(plantuml_inner_code); f.write("\n@enduml\n")

    subprocess.run(["java", "-jar", jar, puml_path])
    print(f"Dijagram generisan i sačuvan: {os.path.join(output_folder, base_name + '.png')}")
