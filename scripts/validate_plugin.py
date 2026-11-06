#!/usr/bin/env python3
"""Inspect the actual ZIP. Requires Pillow, PyYAML, and jsonschema."""
import hashlib
import io
import json
from pathlib import Path, PurePosixPath
import re
import sys
import urllib.request
import zipfile
import yaml
import jsonschema
from PIL import Image

archive = Path(sys.argv[1])
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    names = z.namelist()
    assert len(names) == len(set(names)) == 5, names
    assert all(n.startswith("promptcraft-pro/") for n in names)
    assert all(".." not in PurePosixPath(n).parts and not n.startswith("/") for n in names)
    assert not any(".app.json" in n or "mcp.json" in n or ".git/" in n for n in names)
    for item in z.infolist():
        assert (item.external_attr >> 16) & 0o170000 != 0o120000
    root = "promptcraft-pro/"
    m = json.loads(z.read(root + "plugin.json"))
    schema = json.load(urllib.request.urlopen(m["$schema"], timeout=30))
    jsonschema.Draft202012Validator(schema).validate(m)
    assert re.fullmatch(r"\d+\.\d+\.\d+", m["version"])
    ext = m["extensions"]["com.openai"]
    assert "apps" not in ext and "apps" not in m
    interface = ext["interface"]
    for key, limit in {"displayName":30,"shortDescription":30,"longDescription":4000,"developerName":80}.items():
        assert 0 < len(interface[key]) <= limit, key
    assert interface["category"] == "Productivity"
    prompts = interface["defaultPrompt"]
    assert 1 <= len(prompts) <= 3
    assert len(set(" ".join(p.split()) for p in prompts)) == len(prompts)
    assert all(0 < len(p) <= 128 and "\n" not in p and "@" not in p for p in prompts)
    for key in ("websiteURL","supportURL","privacyPolicyURL","termsOfServiceURL"):
        assert interface[key].startswith("https://") and len(interface[key]) <= 1024
    for key in ("logo","composerIcon"):
        path = interface[key]
        assert path.startswith("./") and ".." not in PurePosixPath(path).parts
        data = z.read(root + path[2:])
        im = Image.open(io.BytesIO(data)); im.verify()
        assert im.format == "PNG" and 256 <= im.width == im.height <= 4096
        assert len(data) <= 5 * 1024 * 1024
    skill = z.read(root + "skills/promptcraft-pro/SKILL.md")
    assert len(skill) < 1024 * 1024
    front = yaml.safe_load(skill.decode().split("---", 2)[1])
    assert front["name"] == "promptcraft-pro" and front["description"].strip()
    source = Path(__file__).resolve().parents[1] / "skills/promptcraft-pro/SKILL.md"
    assert skill == source.read_bytes()
    agent = yaml.safe_load(z.read(root + "skills/promptcraft-pro/agents/openai.yaml"))
    assert agent["interface"]["display_name"] == interface["displayName"]
    assert ext["publication"]["countries"] == []
    assert ext["review"]["commerce"] is False
    assert "test_cases" not in ext["review"] and "demo_recording_url" not in ext["review"]
    assert "MIT License" in z.read(root + "LICENSE").decode()
print(json.dumps({"result":"PASS", "archive":str(archive), "files":names,
                  "sha256":hashlib.sha256(archive.read_bytes()).hexdigest(),
                  "skill_sha256":hashlib.sha256(skill).hexdigest(),
                  "subtitle_length":len(interface["shortDescription"]),
                  "scope":"Package structure, public-upload restrictions, manifest schema, metadata, skill YAML, icon and license. Host activation, behavior and portal scans are separate."}, indent=2))
