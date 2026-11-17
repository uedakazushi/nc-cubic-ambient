# 研究方針：非可換三次曲面のambient射とR(1,3)成分

2026-11-17 / ambient-v2。研究再開時は本ファイルを最初に読み、`papers/nc-cubic-ambient.tex` と入力節 `papers/sections/surface_stack_comparison.tex`、`research/cubic_surface_comparison.md` を参照する。GitHub mainをこの研究の正本とする。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合して、現在の研究価値を最大化する。重要な方針変更は有効な現行方針として書き直し、時系列の更新履歴を蓄積しない。証明済み・追加仮定付き・未証明・予想・有限計算の観察を分離し、仮定・依存文献・証明の所在・未解決点を示す。先行研究は一次資料の正確な仮定を確認し、未確認の書誌や優先権を推測しない。論文は日本語LuaLaTeXとし、公表価値のある有効な成果と必要な証明を残す。研究ノートは今後必要な情報だけを保持し、旧版やバックアップ、ZIP、PDF、中間生成物、重複をGitに入れない。

研究区切りには追加承諾なく、現行研究方針・研究ノート・原稿・必要な検証資産を含む軽量継続bundleをLibraryに保存してよい。GitHubへのpush、Library保存、組版・計算の検証は別々に確認して報告する。Libraryにある旧ファイルの削除は、明示的な指示なしに行わない。

## II. 今の研究目標

本研究は**ambientが与えられた非可換三次曲面のモジュライ比較**を扱う。四次元quadratic Koszul AS正則代数の正規三次商、四周期Z代数の関係式stack、符号付き四次superpotentialの同値関係、R(1,3)の成分、次数付き中心拡大のアフィン同型群oid、Poisson延長、八次判別式の共変性、固定ambientの正規三次ファイバー、AOUの反標準orbit環からの有理射を明確化する。

**保留：** 内在的弱標識付き非可換三次曲面の全対象でambientのAS正則性が自動的に従うか（反例も未発見）。本稿の定義は内在的な許容構造対象を簡潔に再掲するが、ambient射は超曲面認識部分に限定する。

標識付き・弱標識付き・無標識の二段階の忘却は独立論文 `uedakazushi/nc-cubic-unmark/papers/nc-cubic-unmark.tex` が正本。本研究では標識忘却の形式Weyl商を重複して主結果にしない。

## III. 主結果と状態

- 【新たに証明】R(1,3)中心一次拡大$B_f$の一次中心は$kt$。次数付き同型は（全次数共通スカラーを除いて）$f\mapsto(f(Au+b)-f(b))/\det A$の$\operatorname{Aff}_3$作用と完全に一致。graded表示の群oid商$[\mathcal F_{19}^{sm}/\operatorname{Aff}_3]$は一般に滑らかなDM 7次元。素朴なZhang商への昇格は未証明（\`thm:r13-affine\`）。固定次数の計算と独立したLie安定化群の有理数上のrank12証明点を収録。
- 【新たに証明】Jacobian臨界値八次多項式は$\Delta_{\rho_{A,b}f}(\lambda)=(\det A)^{-8}\Delta_f((\det A)\lambda-f(b))$と変換する。非被約Jacobian schemeにも成立（\`prop:critical-discriminant-covariance\`）。
- 【新たに証明】臨界点scheme $Z_f=V(\nabla f)$の二次以下の消滅式は3個の偏微分で張られる。一般の閉1形式のintegrability行列（12×9）のrankは8（明示有理数証明点）で、同じ$Z_f$からは$f$をスカラー倍を除き一意に復元できる。Hilbert schemeへの像は18次元、8個の一般点配置をAff3で割った商は6次元。次数付き中心拡大の7次元商との差を説明（\`thm:r13-eight-reconstruction\`）。
- 【証明・正確な計算証明書】R(1,3)四頂点quartic superpotentialの二flattening全方向の接空間、67次元既約成分の一般正則性、rigidified7次元DM商のエタールatlas（`thm:r13-open`）。
- 【証明】任意に指定した四周期付き関係式stackと非捩れpotentialが同一でない具体的反例（`prop:period-counterexample`）。二因子stabilizerが有限な一般点での形式一致（`prop:period-formal-rigidity`）。
- 【証明】可換三次曲面のPoisson構造の一意ambient延長、中心三次ペンシル、八次臨界値多項式、8個の通常二重点と中心一次拡大の8個のpoint moduleへの対応（`thm:extension`, `thm:pencil-critical`, `prop:critical-point-modules`）。八点の既知LBS結果と新しい具体的対応を区別。
- 【証明・追加仮定】固定ambientの中心三次正規ファイバーのP1と形式一変数（`prop:center`, `prop:normal`）。
- 【既存文献入力のもとで証明】AOU一般幾何点でinverse Serre orbit環がVdBのF=P/(G)に一致（`prop:aou-orbit-generic`）。【追加仮定付き】相対底変更と八方向微分を仮定してambientのR(1,3)成分への支配性・一般一次元ファイバー（`thm:aou-dominance`）。
- 【計算的な障害】量子中心三次の8個の値と古典臨界値が単純なアフィン変換で対応しない例。中心性と数値を有限関係式から検算し、一般定理としない。

## IV. 優先課題

1. AOU有限代数の相対inverse Serre・heart・base changeを一次資料と照合し、支配性定理の仮定のどこを無条件化できるか決定する。
2. R(1,3)の**次数付き**同型はAff3商として決定した。次はこれと四頂点Z代数の一般Zhang同型群oidとの差、Hesseの有限同一視の次数、境界・慣性・七係数atlasの群oidを厳密に比較する。
3. 新たに得た八点臨界schemeの一般復元を、Hilbert scheme上の積分可能なquadratic netの具体的な局所閉locusとその線束へ拡張する。一般の8点構造・Hesse群の有限同一視・境界での重複臨界点を追跡する。併せて既知中心三次商の正規性・H3適合性・homological singularityと量子中心値の関係を調べる。
4. 四周期raw GL商、rigidified PGL商、twisted/untwisted potentialの群oid差を明確化する。標識忘却の一般認識は本研究の達成条件にしない。

## V. 再現

```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_r13_affine_quotient.py
python3 computations/verify_r13_potential.py
python3 computations/verify_surface_incidence.py
python3 computations/verify_pencil_discriminant.py
python3 computations/verify_quantum_casimir_obstruction.py
python3 computations/verify_directed_p3_syzygy.py
python3 scripts/verify_surface_bundle.py
latexmk -lualatex papers/nc-cubic-ambient.tex
```

証明書のrankと通常のAS正則性証明を混同しない。大域同型・全境界・網羅的な優先権調査は未完了。
