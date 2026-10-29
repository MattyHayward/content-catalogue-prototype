---
title: HTML
---

# HTML

A little HTML can be written where Markdown has no equivalent. The site keeps
only a short list of elements, and removes every `class`, `style`, script and
event handler.

## Details

A `details` element becomes the GOV.UK details component:

<details>
<summary>What happens to HTML the site does not allow?</summary>

It is removed, and its text is kept. A `script` is removed with its contents.

</details>

## Abbreviations, keys, and superscript

<abbr title="Technology Code of Practice">TCoP</abbr> shows its full name on
hover. Press <kbd>Ctrl</kbd> and <kbd>F</kbd> to search a page. Water is
H<sub>2</sub>O, and 2<sup>10</sup> is 1,024.

## What is removed

This would not survive, so it is shown here as code instead:

```html
<p class="govuk-!-font-size-80" style="color: red" onclick="alert('hi')">Big red text</p>
<script>alert("hi")</script>
```

On the site, the paragraph would keep its words but lose its class, style and
`onclick`, and the script would go entirely.
