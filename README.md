# Faction documentation

Source for <https://docs.factionsecurity.com>. Two MkDocs sites live here:

| Path | Site | Built to |
|---|---|---|
| `docs/`, `mkdocs.yml`, `overrides/` | Faction 2 documentation (current) | `site/` |
| `faction1.x/` | Faction 1.x documentation (kept as it was) | `docs/faction1.x/`, then `site/faction1.x/` |

The Faction 2 site links to the 1.x site from its top navigation, and every 1.x page carries a banner back.

## Working on it

Everything runs through [mise](https://mise.jdx.dev):

```bash
mise run up        # serve both docs sites with live reload on :8000 (1.x under /faction1.x/)
mise run up-1x     # serve only the Faction 1.x docs on :8001
mise run build     # build both sites into site/ (Faction 2 in strict mode)
mise run deploy    # build both and publish site/ to the gh-pages branch
mise run gen       # regenerate docs/permissions/reference.md from the backend
mise run check     # fail if generated pages are stale or a build breaks
```

Pages are Markdown under `docs/`; screenshots go in `docs/files/`. Opening `docs/` as an Obsidian vault with the attachment folder set to `files` and Markdown links enabled lets you paste screenshots straight into a page.

`marketing/` holds copy that is deliberately not published on this site.
