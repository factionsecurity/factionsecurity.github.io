#!/usr/bin/env python3
"""Regenerate docs/permissions/reference.md from the backend Permission enum.

The permission catalog has exactly one source of truth — `Permission.java`. The API serves it
to the Roles admin UI from there, so a hand-maintained table in the docs would drift the first
time someone adds a permission. Run this instead:

    python3 scripts/gen_permission_reference.py

Point it at another checkout with --repo if the backend does not live at ../faction2.
"""
import argparse
import re
from collections import OrderedDict
from pathlib import Path

PERMISSION_RE = re.compile(
    r'^\s{4}[A-Z0-9_]+\("(?P<key>[^"]+)",\s*"(?P<desc>[^"]+)",\s*PermissionResource\.(?P<res>[A-Z_]+)\)',
    re.M,
)
RESOURCE_RE = re.compile(r'^\s{4}(?P<name>[A-Z_]+)\("(?P<display>[^"]+)",\s*"(?P<desc>[^"]+)"\)', re.M)

HEADER = """# Permission reference

Every permission the platform defines, grouped by resource — the same catalog the Roles admin
screen renders as a checkbox matrix.

!!! note "Generated file"
    This page is generated from `backend/src/main/java/com/faction/clientportal/model/Permission.java`
    by `scripts/gen_permission_reference.py`. Edit the enum, then re-run the script; do not edit
    this page by hand.

`super_admin` is not listed here. It is not part of the catalog, is implied by every gate, and
cannot be granted from the Roles screen.

"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", default="../../faction2", help="path to the faction2 checkout")
    parser.add_argument("--out", default="docs/permissions/reference.md")
    args = parser.parse_args()

    base = Path(args.repo) / "backend/src/main/java/com/faction/clientportal/model"
    permissions = PERMISSION_RE.findall((base / "Permission.java").read_text())
    resources = {
        m.group("name"): m.group("display")
        for m in RESOURCE_RE.finditer((base / "PermissionResource.java").read_text())
    }

    grouped: "OrderedDict[str, list]" = OrderedDict()
    for key, desc, res in permissions:
        grouped.setdefault(res, []).append((key, desc))

    out = [HEADER, f"There are **{len(permissions)}** permissions across "
                   f"**{len(grouped)}** resources.\n"]
    for res, entries in grouped.items():
        out.append(f"\n## {resources.get(res, res)}\n")
        out.append("| Permission | Description |")
        out.append("| --- | --- |")
        for key, desc in entries:
            out.append(f"| `{key}` | {desc} |")
        out.append("")

    Path(args.out).write_text("\n".join(out) + "\n")
    print(f"wrote {args.out}: {len(permissions)} permissions, {len(grouped)} resources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
