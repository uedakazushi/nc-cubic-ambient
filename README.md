# 非可換三次曲面のマーキング忘却とPicard作用

**[研究方針](00_research_plan.md)から読む。** 現行公表稿は [nc-cubic-ambient-moduli.tex](papers/nc-cubic-ambient-moduli.tex) で、[markingの主節](papers/sections/marking_forgetful.tex) と [ambientの既存結果](papers/sections/surface_stack_comparison.tex) を読み込む。[研究ノート](research/cubic_surface_comparison.md)・[再現手順](research/cubic_surface_reproduce.md)・[検証状態](research/surface_validation.json)を参照。

現在の最優先研究は、標準九対象helix（AOU）→rank-one torsion-free exceptional構造対象を指定したweakly marked圏→unmarked Abel圏、という二段階の忘却の幾何学的ファイバーと慣性である。ambient quadratic AS-regularityの自動認識問題は**保留**し、既に証明したambient結果は後半に保持する。

可換三次曲面では構造対象が線束となり、exact自己同値のPicard作用で推移的。非可換一次変形では線束の持上げとtensor自己同値の持上げが異なり、障害は `delta_pi(L)=H^1(pi^sharp)c1(L)`。**非常に一般の組(X,π)について整数障害核は厳密にZK_X**で、許容一次NC変形の同一圏のexact自己同値が動かせる構造対象は反Serre方向のみ。許容構造対象の同型類商はPic(X)/ZK_X≅Q(E6)^∨≅Z^6（相対heart条件付き）。可換点での形式的W(E6)商は相対heart条件付きで、全大域weak商同定は未証明。AOUのGIT関係式表示に共通tensorが既に見えない点にも注意。

## 再現
```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_surface_bundle.py
latexmk -lualatex papers/nc-cubic-ambient-moduli.tex
```

完全な数値計算の追加手順は研究ノート参照。PDF・ZIP・aux等はGit追跡しない。H3全分類の別正本は [nc-cubic-moduli](https://github.com/uedakazushi/nc-cubic-moduli)、非AS短報は [nc-cubic-non-as](https://github.com/uedakazushi/nc-cubic-non-as)。
