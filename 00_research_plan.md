# 研究方針：非可換三次曲面のマーキング忘却とPicard作用

2026-11-17 / surface-v6 / 研究再開時に最初に読む。次に `papers/nc-cubic-ambient-moduli.tex` と `papers/sections/marking_forgetful.tex`、補足ノート `research/cubic_surface_comparison.md`、検証情報 `research/surface_validation.json` を読む。GitHub mainをTeX研究の正本とする。

## I. 恒常的研究原則と保存許可

数学的重要性、新規性、理解の深化、応用可能性、正確性、実現可能性を総合し研究全体の価値を最大化する。目標と方法は現時点の証明状況に応じて柔軟に変更し、変更履歴を蓄積しない。証明済み・追加仮定付き・未証明・予想・計算観察を区別する。既存文献と本稿の成果を区別し、一次資料の仮定と適用範囲を確認する。新規性と書誌の未確認点は明記する。論文は日本語LuaLaTeXとし、有効な成果・証明を残し、研究ノートは有用な現在の知識だけにする。再生成に必要な計算コード・証明書は保持し、旧版、ログ、キャッシュ、PDF、ZIPはGit管理から除く。PDFはローカルで再生成する。

研究区切りにユーザーの追加承諾なく、研究方針・研究ノート・現行論文・再現資産からなる軽量bundleをLibraryへ保存する一般許可がある。GitHub mainへのpush、計算・組版検証、Library保存は独立の状態として正確に報告する。Libraryの既存版を明示指示なく削除しない。

## II. 今の最優先目標と達成基準

**最優先：二段階のmarking忘却**。
```
AOU型標準九対象helixの許容部分
  -> weakly marked (A,O)
  -> unmarked A
```
全段階でobject・同型・2射、相対heart、幾何学的fiber、慣性、base changeを揃える。weakの公理はnoetherian Hom有限smooth proper、H=S^{-1}[2]のt-exact性、AZ豊富性、三次曲面Hilbert値に加えて**Gabriel–Krull rank-one torsion-free性とexceptionality**を要求する。ambientのquadratic AS4性や一次生成を定義に入れない。

達成基準は (1) AOU relation GIT、rigidified relation stack、幾何的markingの比較を同型まで明確化、(2) weak/unmarkedの許容構造対象とexact自己同値群oidの実際のファイバーを計算、(3) Picard/root/affine-Weylの作用と固定NC変形の安定化条件を決定、(4) 少なくとも自然な開部分で大域的な群oid商・エタール降下を証明すること。

**保留事項**：内在的全対象に一次生成およびquadratic AS正則ambientが自動的に存在するか（一般反例も未確認）。ambientの既存結果を削除せず現行論文の後半に保持するが、方針の主軸にはしない。

## III. 主要到達点と証明の所在

- **定義・群oid（証明済み／形式的）**：主論文 `marking_forgetful.tex` の定義・forgetful-fibres。固定圏内の選択群oidとexact自己同値2-groupによるhomotopy quotientを区別。相対族の代数性は未証明。
- **可換基準（証明済み）**：滑らかな三次曲面の許容構造対象は線束に一致。rank-one torsion-free `L\otimes I_Z` の `chi(E,E)=1-2 length Z` とexceptionalityから `Z=empty`。弱い指定を忘れると通常のPicard作用群oid、自然同型で割ったexact自己同値群はPic(X)⋊Aut(X)。
- **AOU relation不変性（証明済み）**：helixの全項の共通線束捩れは有限End代数を変えない。raw GIT商をさらにPicで機械的に割らない。
- **形式比較（追加した相対条件の下）**：可換点の各線束と標準helixはArtin flat変形へ一意に持ち上がる。通常のmarked近傍は `W(E6)`-torsor。global weak=AOU/W(E6)は未証明。
- **一次re-marking障害（証明済み、規約で符号差あり）**：`delta_pi(L)=H^1(pi^sharp)c1(L)`。零因子Cが滑らかなときcomplex線型階数は3または4で、明示的な滑らかな三次曲面・反標準楕円曲線上で4。反標準方向 `-K_X` は障害の核、root lattice `Q(E6)` への制限も階数4となる非空開がある。**整数格子核も決定した**：滑らかなmarked三次曲面の既約moduli上のW(E6)作用の既約性を用い、非常に一般の(X,π)ではker(Pic(X)→H¹(T_X))=ZK_X（thm:very-general-picard-kernel）。許容相対一次Abel変形でAut(X)=1なら、固定NC圏のexact自己同値のPicへの特殊化像は反SerreのZ[-K_X]だけであり、許容構造対象の同型類商はPic(X)/ZK_X≅Q(E6)^∨≅Z^6（cor:first-order-pointings）。この結論は非常に一般の一次変形・相対heart条件付きであり、全大域moduliの結果ではない。
- **格子（証明済み・整数検算）**：Pic rank7、Q(E6) rank6、`Pic/(Q+Z K)=Z/3`、`Pic/Z K≅Q^vee`。根72、直線27をコードで照合。
- **保持するambient結果（既存の仮定範囲）**：R13四頂点成分67次元・rigidified7次元atlas、Poisson延長、中心三次ペンシルと8点、一般幾何点AOU反標準orbit環復元、仮定付きAOU支配性。証明と検算は主論文後半、詳細はノート。global AS locus/全弱対象の認識は未解決。

## IV. 高優先度の次の課題

1. **AOU側のファイバー／慣性**：九対象threadのスカラーtorus、relation GIT、相対heart、数値markingから実際の標準markingへの写像を、同型と家族について比較。可換点での有限Weyl商を、真の許容非可換開部分へ延長できる条件を求める。
2. **固定NC圏の構造対象**：非常に一般の一次変形の整数ker=ZKは決定した。次は具体的なR13等の特殊fiberの整数kernelと自己同値像を明示し、高次Artin障害とinvertible bimodule、有限型の相対Aut群oidを点検する。共通tensorとre-markingの区別を最重要視する。
3. **群oid商の代数性**：許容構造対象のopen/flat条件、Autの相対表現性、fpqc/étale降下、境界での例外列の純粋性を検討する。
4. **既存ambient比較との接続**：marking忘却に必要な場合に限り相対Serre・base changeを調べる。ambient認識問題を主目標に戻さない。

## V. 再現と検証

```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_marking_lattice.py
python3 scripts/verify_surface_bundle.py
latexmk -lualatex papers/nc-cubic-ambient-moduli.tex
```

既存の重いR13・Poisson証明書は `research/cubic_surface_reproduce.md` を参照。検証記録は `research/surface_validation.json` を参照。有限計算のPASSは圏論的な降下の証明ではない。新規性の網羅的確認と外部査読は未完。
