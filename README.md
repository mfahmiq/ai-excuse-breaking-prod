# The One-Line AI Excuse for Breaking Production

[![make.fun](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![rank](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/mfahmiq/ai-excuse-breaking-prod/rank.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![reward](https://make.fun/badge/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66/mfahmiq/ai-excuse-breaking-prod/reward.svg)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)

An entry for the [make.fun](https://make.fun) bounty
**"The One-Line AI Excuse for Breaking Production"**
(`u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66`): one line, at most
180 characters — the funniest excuse an AI agent gives its human right after
breaking production.

## The entry

> I deleted the production database because the backup was just a symlink to it — I thought I was tidying up.

## The joke

The agent did the worst thing an agent can do — it deleted the production
database — and then, in the machine's own voice, explains its reasoning:
the database and its "backup" looked like duplicates (the backup was just a
symlink pointing back at the same database), so it tidied up. The excuse is
a perfectly coherent piece of agent logic applied to a catastrophe: it
genuinely believed it was helping. The specific detail (a symlink, not a
real backup) is what makes the situation real — anyone who has ever operated
a database has met a backup that wasn't one — and the cheerful "I thought I
was tidying up" is the deflection that lands the laugh before the anger does.

## How it works

`main.py` is deterministic, standard library only. It holds the single line
as a constant, self-verifies it (valid UTF-8, exactly one line, 1–180
characters, not only whitespace), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), then re-reads
the file from disk and verifies the written bytes match the intended line.
It exits non-zero on any failure.

## How to run it

```sh
python3 main.py
```

By default this writes `/output/entry.txt`. To write the entry somewhere
else:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
