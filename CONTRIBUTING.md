# Contributing to gh-yap

Thanks for wanting to help! 🙌 *(Versión en español más abajo.)*

## Before you start

- **Open an issue first** for anything bigger than a typo, so we can agree on the idea before you spend time on it.
- Just want to chat or yap? Use the square: `gh yap`, or [josemingorance/yap](https://github.com/josemingorance/yap/issues).

## Ground rules

- **Zero dependencies.** Only `gh` and what ships with a stock macOS/Linux. No `jq` binary: use `gh api --jq`.
- **bash 3.2 compatible.** No associative arrays, `mapfile`, `${var,,}` or `&>>`. Test with `/bin/bash ./gh-yap` on a Mac if you can.
- **Bilingual.** Any new user-facing message needs an `en:` and an `es:` entry in `t()`.
- **shellcheck clean.** CI runs `shellcheck gh-yap`.

## Testing locally

```sh
gh extension install .                     # installs your local copy as `gh yap`
export GH_YAP_REPO=<you>/yap-sandbox       # use your own private repo, not the public square
gh yap post "testing"
```

To re-record the demo GIFs: `vhs assets/demo.tape` and `vhs assets/demo.es.tape`.

---

# Contribuir a gh-yap

¡Gracias por querer echar una mano!

- **Abre un issue antes** de cualquier cosa más grande que una errata, para acordar la idea antes de que le dediques tiempo.
- **Sin dependencias**: solo `gh`. Nada de instalar `jq`: usa `gh api --jq`.
- **Compatible con bash 3.2** (el de macOS).
- **Bilingüe**: cada mensaje nuevo necesita su versión `en:` y `es:` en `t()`.
- **shellcheck sin avisos**: el CI lo comprueba.
- Para probar, usa tu propio repo privado con `GH_YAP_REPO`, no la plaza pública.
