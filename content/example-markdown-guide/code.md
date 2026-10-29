---
title: Code
---

# Code

## Inline code

Put commands, file names and values in backticks: run `git status`, or set
`review_in: 12 months`.

## Code blocks

Fence a block with three backticks, and name the language after the opening
fence:

```python
def next_review(last_reviewed, months):
    """Tell me when this page is due for review."""
    return last_reviewed + relativedelta(months=months)
```

A block can also be indented by four spaces:

    $ python scripts/validate.py
    Catalogue is valid: 78 entries.

Long lines scroll sideways rather than wrapping, so the code keeps its shape.
