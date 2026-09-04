# Curation and Data Schema

## Curation Standard

This is a shortlist, not an inventory. Inclusion means the maintainers believe a transportation professional can understand the resource's purpose and reasonably expect value from returning to it.

A candidate is assessed on:

1. **Transportation relevance** — The primary use must be transportation, mobility, infrastructure, logistics, or a closely connected application.
2. **Utility** — It solves a real practitioner, research, development, teaching, or learning need.
3. **Authority and evidence** — Prefer official documentation, maintainers, government sources, universities, standards bodies, or established community projects.
4. **Accessibility** — The landing page should explain the resource and provide a stable path to use, documentation, or data.
5. **Health** — Maintenance, documentation, releases, and community activity are considered when they matter to the resource type.
6. **Distinctiveness** — A resource should add a capability or perspective not already represented more effectively.
7. **Neutral presentation** — Descriptions state what a resource does and why it is useful without promotional claims.

Commercial resources are eligible when they are important to professional practice and have substantive technical information. Affiliation must be disclosed. A paid resource receives no preference over a stronger open alternative.

## Review Process

- Open the canonical URL and confirm that it resolves to the named resource.
- Prefer the project's official site or canonical repository over a blog post or aggregator.
- Check documentation, licensing, access conditions, and maintenance signals relevant to the resource type.
- Search the catalog for duplicate names, URLs, and equivalent entries.
- Choose the narrowest accurate category and a stable, kebab-case subcategory.
- Write one concise sentence that starts with an uppercase character and ends with a period.
- Record `last_checked` as the review date in `YYYY-MM-DD` form.

Broken links, abandoned software, or superseded standards are removed or moved to a future archival document only when their historical value is clear.

## YAML Schema

`data/resources.yml` is the source of truth. It contains a schema version and a list of resource objects.

### Required Fields

| Field | Meaning |
| --- | --- |
| `name` | Canonical, human-readable resource name. |
| `url` | Stable canonical HTTP or HTTPS URL. |
| `description` | Neutral one-sentence explanation of purpose and value. |
| `category` | Controlled top-level taxonomy value. |
| `subcategory` | Kebab-case topic within the category. |
| `resource_type` | Controlled description of what the entry is. |
| `transport_mode` | Controlled primary mode, or `multimodal`. |
| `organization` | Maintainer, publisher, standards body, or responsible organization. |
| `geography` | Meaningful geographic coverage, or `global`/`international`. |
| `free` | Whether useful access is available without payment. |
| `open_source` | Whether source code or the maintained specification is openly developed. |
| `tags` | Short list of lowercase, kebab-case discovery terms. |
| `last_checked` | Date the canonical URL and core metadata were reviewed. |

### Optional Fields

| Field | Use it when |
| --- | --- |
| `license` | A software, data, or content license is clearly stated. |
| `academic_level` | A learning resource targets a defined level. |
| `programming_language` | Language is useful when selecting software. |
| `data_format` | A dataset or standard has a notable format. |
| `api_available` | API access is a meaningful feature. |
| `notes` | A short access constraint or qualification cannot fit the description. |

Unknown facts should be omitted, not guessed. Boolean values describe meaningful access to the resource, not whether its website is viewable.

## Maintenance Commands

Run the local catalog checks with:

```console
python scripts/validate_resources.py
```

Render the resource section of the README after editing YAML:

```console
python scripts/render_readme.py
```

CI verifies both the data and that the README is in sync.

## Future Checks

Useful next automation includes scheduled link checking with respectful timeouts, per-category alphabetical checks, stale `last_checked` reporting, catalog statistics, and generated category pages or a searchable website. Link checks should distinguish a genuinely broken resource from rate limits and bot protection.
