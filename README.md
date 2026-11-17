# 非可換三次曲面のambient射とR(1,3)成分

**[研究方針](00_research_plan.md)から読む。** 主論文は [nc-cubic-ambient.tex](papers/nc-cubic-ambient.tex)、入力節は [surface_stack_comparison.tex](papers/sections/surface_stack_comparison.tex)。必要な計算証明書と再現コードは `computations/`、現在の研究上の整理は [研究ノート](research/cubic_surface_comparison.md)、検証状態は [surface_validation.json](research/surface_validation.json) にある。

このリポジトリは、quadratic Koszul AS正則ambientと正規三次商の比較、四頂点superpotential、R(1,3)の67次元成分・7次元商、次数付き中心拡大のAff3商、八次臨界値多項式の群作用に対する共変性、Poisson延長・中心三次ペンシル・8点、およびAOU一般点からの条件付きambient射の支配性を扱う。内在的な全非可換三次曲面についてのambient認識は未証明で保留する。

**標識忘却論文は [nc-cubic-unmark](https://github.com/uedakazushi/nc-cubic-unmark) に移転済み**。主論文は `papers/nc-cubic-unmark.tex`。同論文のrank-one torsion-free exceptional構造対象、有限Weyl商、Picard作用と自己同値の定理はそちらの正本で保持する。ここで標識忘却を独立の主結果として重複させない。

## 再現
```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_r13_affine_quotient.py
python3 computations/verify_r13_potential.py
python3 computations/verify_surface_incidence.py
python3 scripts/verify_surface_bundle.py
latexmk -lualatex papers/nc-cubic-ambient.tex
```

より詳しい再現は `research/cubic_surface_reproduce.md`。PDF・ZIP・中間生成物はGitで追跡しない。四次元ambientの全分類は別研究の `nc-cubic-moduli` を参照。
