# 非可換三次曲面のambient・markedモジュライ比較

**最初に[研究方針](00_research_plan.md)を読む。** 現行論文は [nc-cubic-ambient-moduli.tex](papers/nc-cubic-ambient-moduli.tex) と [surface_stack_comparison.tex](papers/sections/surface_stack_comparison.tex)。[研究ノート](research/cubic_surface_comparison.md)・[R13](research/r13_generic_moduli.md)・[再現手順](research/cubic_surface_reproduce.md)・[検証範囲](research/surface_validation.json)を参照。

目標はintrinsic H3／weakly marked三次曲面、14641 ambient・4頂点potential、AOUのmarked AS曲面モジュライを比較し、対応射の定義域・像・ファイバー・同型を決定すること。Pym R(1,3)の接空間やW(E6)の形式近傍は扱うが、全大域weakモジュライのWeyl商同定と全対象の超曲面認識は**未証明**。AOUからの支配性は一般位置の明示した比較仮定の下での結論である。

## 再現
```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_surface_incidence.py
python3 computations/verify_r13_potential.py
latexmk -lualatex papers/nc-cubic-ambient-moduli.tex
python3 scripts/verify_surface_bundle.py
```

GitHub mainが唯一の正本。PDF・ZIP・中間生成物はGit追跡しない。分類の正本は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、楕円E6量子化は [nc-cubic-e6](https://github.com/uedakazushi/nc-cubic-e6)、非AS短報は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)。資料の移行元は [固定commit](https://github.com/uedakazushi/nc-cubic-moduli/tree/c5fd8a8301f6b1c283a6f0510cde80ae6a006e80)。
