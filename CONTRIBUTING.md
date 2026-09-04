# Contributing

Thank you for helping build a practical, trustworthy transportation directory. The goal is not to collect every related link; it is to preserve a shortlist that professionals will return to.

## Before Suggesting a Resource

Please check that the resource:

- Is directly relevant to transportation, mobility, infrastructure, logistics, or transportation education.
- Is useful to practitioners, researchers, developers, educators, or students.
- Has a stable canonical URL and a page that clearly explains what it provides.
- Is reputable or demonstrably useful, with current documentation when maintenance matters.
- Is not already listed under another name or URL.
- Can be described neutrally in one concise sentence.

We give preference to open-source software, official documentation, open datasets, government and university sources, respected research groups, free educational material, recognized community projects, and widely used standards. Important commercial tools can be included, but the list is not an advertising directory.

Do not submit affiliate links, SEO pages, pirated material, low-value promotional pages, broken links, duplicate resources, abandoned trivial repositories, or generic technology without a meaningful transportation use.

## Robotics, AI, and GIS Scope

Robotics belongs here only when the connection to transportation is explicit. Appropriate examples include an autonomous-driving stack, rail-inspection robot, bridge-inspection UAV workflow, port-automation platform, autonomous delivery vehicle, or transportation mobile-mapping system. A generic robotic-arm framework or general drone library is out of scope.

The same rule applies to AI, GIS, cloud, visualization, and computing tools: the entry or its description must show a substantive transportation application. Being potentially usable in transportation is not enough.

## How to Contribute

For a new resource, either use the resource-suggestion issue form or open a pull request.

1. Add one entry to `data/resources.yml` using the documented schema.
2. Add the matching entry to `README.md` in the narrowest accurate category and subcategory.
3. Use the project's official site or canonical repository.
4. Write a neutral description explaining both what it is and its transportation value.
5. Disclose any personal, employer, client, or financial affiliation in the pull request.
6. Run:

   ```console
   python -m pip install -r requirements-dev.txt
   python scripts/validate_resources.py
   python scripts/validate_readme.py
   ```

7. Commit both the YAML and hand-maintained README changes.

Descriptions begin with an uppercase character, end with a period, and avoid claims such as “best,” “leading,” or “revolutionary.” Do not guess optional metadata. See [docs/curation.md](docs/curation.md) for the full schema and review criteria.

## Pull Request Review

Maintainers may ask for evidence of use, clearer transportation relevance, a more canonical URL, affiliation disclosure, or a narrower description. Inclusion is editorial and may be declined even when a resource is relevant; this keeps the list useful and differentiated.

Removal proposals are welcome when a resource is unavailable, superseded, materially abandoned, misleadingly described, or no longer meets the standard. Explain the reason and, where possible, suggest a stronger replacement.

Please keep pull requests focused. One new resource per pull request is easiest to review, although a small, coherent set is acceptable when the entries share one source or purpose.
