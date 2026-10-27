# Technology in government: catalogue

This repository decides what tech.gov.uk lists: the standards, policy,
guidance and methods for people working in government technology, wherever
they are published.

Each entry either holds its content here, points at another repository that
holds it, or links to where it is already published (for example GOV.UK). The
site reads this repository and builds its pages from it. Nothing about an
entry is set up in the site itself.


## Add or change an entry

1. Copy an existing file in `entries/` and name it after the new entry's
   `id`, for example `entries/my-standard.yml`.
2. Fill in the fields (see below). Take `type`, `tags` and `professions`
   from `vocabularies.yml`. To add a value, add it there in the same pull
   request.
3. Open a pull request. The checks validate every file, and the entry's
   owners, as listed in `.github/CODEOWNERS`, review it.

To check locally:

```bash
pip install jsonschema PyYAML
python scripts/validate.py
```


## Entry fields

| Field | Required | What it is |
| --- | --- | --- |
| `id` | yes | Lower case and hyphens. Must match the file name. It becomes the entry's address on the site (`/<id>/`), so don't change it once published. |
| `title` | yes | The entry's name, as its owner publishes it. |
| `short_description` | yes | One sentence, up to 180 characters, for the card that links to the entry. |
| `long_description` | yes | The opening paragraph of the entry's front page, up to 1,200 characters. |
| `type` | yes | One value from `types` in `vocabularies.yml`. It decides the page layout. |
| `primary` | no | `true` to rank the entry above others where they compete, for example in search and filtered lists. Defaults to `false`. |
| `scope` | yes | One value from `scope`: how widely the entry is meant to be used, from the whole public sector to a single organisation. |
| `tags` | yes | One or more topics from `tags`, used for filtering. |
| `professions` | yes | One or more from `professions`: who the entry is for. |
| `owner` | yes | `organisation`, and optionally `team` and a `contact` (`email`, `url` or `slack`). |
| `source` | yes | Where the content is (see below). |
| `status` | no | `current` (default), `draft` (not shown on the site) or `withdrawn` (shown with a withdrawn notice). |
| `applies_to` | no | Who the entry is for, or for standards and policy, who must follow it. One sentence. |
| `related` | no | Ids of other entries to link to. |


## Sources

Every source has a `type`, a `name` (where it is published, for example
`GOV.UK`, shown next to the link) and a `path`.

| `type` | `path` | Other fields | The site |
| --- | --- | --- | --- |
| `external` | The `https://` address where it is published | | Serves a summary page under `/<id>/` with the descriptions, owner and a link to the content. |
| `repo` | The GitHub repository, as `owner/name` | `branch` (default `main`), `directory` (optional), `ref` (optional tag or commit to pin) | Syncs the repository and serves its pages under `/<id>/`. The repository can use the `guidance.yml` format or be a tech-docs site. |
| `hosted` | A directory under `content/` with a `guidance.yml` | | As `repo`, but the content is held here. |

Pinning a `repo` source with `ref` means changes in that repository only
reach the site when this repository is updated to a new `ref`, and so only
after review here.


## Types and layouts

Each type in `vocabularies.yml` names one of these layouts:

| Layout | Used by | Shows |
| --- | --- | --- |
| `requirements` | standard, principles | Who it applies to, then the numbered requirements or principles, each with its own page where the source has them. |
| `policy` | policy, strategy | The policy statement and who it applies to, the owner, and the latest change. |
| `guide` | guidance | A front page, then pages with the side navigation. |
| `steps` | method | The pages as numbered steps, in order, with previous and next links. |
| `tool` | resource, product | What it is, who owns it and a link to use it. |
| `media` | blog | What it covers, who writes it and a link to read it. |

An `external` entry uses its type's layout for its summary page.


## Licence

The catalogue data is © Crown copyright, available under the Open Government
Licence v3.0. Content held in `content/` is under the same licence unless its
files say otherwise. Linked content is under its publisher's licence.
