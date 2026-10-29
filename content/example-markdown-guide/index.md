---
title: Writing guidance in Markdown
last_reviewed_on: 2026-10-29
review_in: 12 months
---

# Writing guidance in Markdown

This guide shows every kind of Markdown the site renders, and what each one
becomes on the page. Use it as a reference when writing guidance to be held in
the catalogue.

The pages are plain Markdown (CommonMark, with tables) and read the same on
GitHub. The site adds GOV.UK Design System styles: you never write a class.

## How a guide is arranged

A guide is a directory with a `guidance.yml` and one Markdown file per page.
The side navigation comes from `navigation` in `guidance.yml`, in the order it
lists the pages. A page can list `pages` of its own, which appear beneath it in
the navigation while the reader is in that part of the guide, as
[Linking](formatting/links.md) sits under [Text](formatting/text.md).

## Front matter

Each page starts with front matter. Only `title` is needed:

```yaml
---
title: The page's title
last_reviewed_on: 2026-10-29
review_in: 12 months
---
```

`last_reviewed_on` and `review_in` give the page's review dates. The site shows
them, and warns readers once the review is overdue.
