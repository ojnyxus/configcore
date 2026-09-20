#!/usr/bin/env python3
"""Regenerates assets/configcore/sounds.json from the .ogg files in sounds/voice/.
Run from the project root:  python tools/gen_sounds.py   (or python3 on Linux/Mac)"""
import json, pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "src/main/resources/assets/configcore"
voice_dir = root / "sounds" / "voice"

sounds = {
    "glitch_static": {
        "subtitle": "subtitles.configcore.glitch_static",
        "sounds": [
            {"name": "configcore:glitch_static1"},
            {"name": "configcore:glitch_static2"},
        ],
    }
}

files = sorted(voice_dir.glob("*.ogg"))
for f in files:
    sounds[f.stem] = {"sounds": [{"name": f"configcore:voice/{f.stem}"}]}

(root / "sounds.json").write_text(json.dumps(sounds, indent="\t"), encoding="utf-8")
print(f"sounds.json written: glitch_static + {len(files)} voice line(s)")
for f in files:
    print("  -", f.name)
