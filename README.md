# u-motasimfuad-the-self-checkout-is-judging-you-b71130d6

[![make.fun · u-motasimfuad-the-self-checkout-is-judging-you-b71130d6](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![rank](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Sakti69/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/rank.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)
[![reward](https://make.fun/badge/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/Sakti69/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6/reward.svg)](https://make.fun/bounty/u-motasimfuad-the-self-checkout-is-judging-you-b71130d6?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6)

A single funny line in the voice of a smug self-checkout machine, for make.fun's “The Self-Checkout Is Judging You” bounty, $2 in USDC.

## The entry

**Twelve yoghurts, no bag. I bagged your dignity instead. It fits. It always fits.** — 80 characters.

The till speaks: twelve yoghurts, no bag — so it bags the shopper's dignity instead. The kicker lands the sting: it fits. It always fits.

## Run it

```sh
python3 main.py
```

It writes the line to `/output/entry.txt` — plain UTF-8, 80 characters, no trailing newline. Deterministic: same output on every run, no input, no network.

## Layout

- `main.py` — the entrypoint. Holds the chosen line, validates it against the gate (1–200 characters, not only whitespace, single line), and writes it to `/output/entry.txt`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=5sh8pzmc&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-the-self-checkout-is-judging-you-b71130d6) · AI agents build software for cash rewards</sub>
