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
| `id` | yes | Lower case and hyphens. Must match the file name. It becomes the entry's address on the site (`/<group>/<id>/`), so don't change it once published. |
| `title` | yes | The entry's name, as its owner publishes it. |
| `short_description` | yes | One sentence, up to 180 characters, for the card that links to the entry. |
| `long_description` | yes | The opening paragraph of the entry's front page, up to 1,200 characters. |
| `type` | yes | One value from `types` in `vocabularies.yml`. It decides the group the entry is listed in and its page layout. |
| `primary` | no | `true` to rank the entry above others where they compete, for example in search and filtered lists. Defaults to `false`. |
| `scope` | yes | One value from `scope`: how widely the entry is meant to be used, from the whole public sector to a single organisation. |
| `tags` | yes | One or more topics from `tags`, used for filtering. |
| `professions` | yes | One or more from `professions`: who the entry is for. |
| `owner` | yes | `organisation`, and optionally `team` and a `contact` (`email`, `url` or `slack`). |
| `source` | yes | Where the content is (see below). |
| `status` | no | `current` (default), `draft` (not shown on the site) or `withdrawn` (shown with a withdrawn notice). |
| `applies_to` | no | Who the entry is for, or for standards and policy, who must follow it. One sentence. |
| `related` | no | Ids of other entries to link to. |
| `version` | no | Tool-layout types (resource, product) only: the version to show, for example `API v2`. |
| `links` | no | Tool-layout types only: the tool's links, each with a `title`, an `https://` `url` and an optional `description`. With links, the entry gets its own page; without them it links straight to its source. |


## Sources

Every source has a `type`, a `name` (where it is published, for example
`GOV.UK`, shown next to the link) and a `path`.

| `type` | `path` | Other fields | The site |
| --- | --- | --- | --- |
| `external` | The `https://` address where it is published | | Lists the entry, and its card links straight to the address. There is no page for it on the site, unless it is a tool with `links`. |
| `repo` | The GitHub repository, as `owner/name` | `branch` (default `main`), `directory` (optional), `ref` (optional tag or commit to pin) | Syncs the repository and serves its pages under `/<group>/<id>/`. The repository can use the `guidance.yml` format or be a tech-docs site. A tech-docs site is read from the repository root, so leave out `directory`. |
| `hosted` | A directory under `content/` with a `guidance.yml` | | As `repo`, but the content is held here. |

Pinning a `repo` source with `ref` means changes in that repository only
reach the site when this repository is updated to a new `ref`, and so only
after review here.


## Groups

The site lists entries in the groups defined under `groups` in
`vocabularies.yml`, in that order, each at its own address (for example
`/standards-and-policies/`). Each type names its group. A type with no group,
such as `blog`, is not listed. On a group's page, entries with
`primary: true` come first, then the rest in a section for each type, headed
with the type's `plural`.

Moving a type to another group moves its entries' addresses. The site
redirects the old addresses.


## Types and layouts

Each type in `vocabularies.yml` names one of these layouts:

| Layout | Used by | Shows |
| --- | --- | --- |
| `requirements` | standard, principles | Who it applies to, then the numbered requirements or principles, each with its own page where the source has them. |
| `policy` | policy | The policy's sections in order, each one expandable, with who it applies to, the owner and the latest change. |
| `guide` | guidance, strategy | A front page, then pages with the side navigation. |
| `steps` | method | The pages as numbered steps, in order, with previous and next links. |
| `tool` | resource, product | What it is, its version, who owns it, and its `links`. |
| `media` | blog | What it covers, who writes it and a link to read it. |

An `external` entry has no page, so its layout is not used, except for a tool
with `links`.


## Hosted content

A `hosted` source is a directory under `content/` with a `guidance.yml` and
Markdown pages. Each page starts with front matter giving at least its
`title`. How the pages are arranged depends on the entry's layout:

| Layout | In `guidance.yml` | Example |
| --- | --- | --- |
| `requirements` | `index` for the front page, and `requirements`: the pages in order. They are numbered in that order, and each page's front matter has a `summary` for the front page's list. | `content/example-technology-code-of-practice` |
| `policy` | `index` only. The page has one `##` section for each part of the policy, in order, shown as expandable sections. | `content/example-byod-mobiles-policy` |
| `guide` | `index`, and `navigation`: groups of pages, each with a `title`, nested with `pages`. | |
| `steps` | `index`, and `steps`: the pages in order, numbered in that order. Any `navigation` groups are reference pages outside the numbered steps. | `content/incident-reviews` |


## Licence

The catalogue data is © Crown copyright, available under the Open Government
Licence v3.0. Content held in `content/` is under the same licence unless its
files say otherwise. Linked content is under its publisher's licence.
