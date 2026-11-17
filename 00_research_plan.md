# 研究方針：内在的非可換三次曲面とambientモジュライの比較

2026-11-17 / surface-v4 / 独立研究正本。**再開時は本書を最初に読む。** 次に `research/cubic_surface_comparison.md`、`research/r13_generic_moduli.md`、`papers/nc-cubic-ambient-moduli.tex` と入力節を読む。

## I. 恒常的な研究原則と保存許可

数学的重要性、新規性、理解の深化、実現可能性、正確性を重視し研究方針を柔軟に更新する。重要な変更は現行方針として理由を記し、履歴を積まない。証明済み・条件付き・未証明・予想・計算結果を区別し、既存と新規の成果を区別する。先行研究の一次資料と仮定を確認し、未確認の書誌・新規性を推測で補わない。論文は原則日本語LuaLaTeXで現在の成果と必要な証明を保持し、研究ノートは日誌にしない。旧ZIP・バックアップ・ログ・PDF・キャッシュをGitに入れず、必要なコード・入力・小証明書を保持する。

研究区切りで承諾なくLibrary保存する一般許可はあるが、このリポジトリはGitHub mainが正本であり、push成功時はLibrary保存せず、GitHub失敗時の緊急避難に限る。既存Libraryファイルは明示指示なしに削除しない。

## II. 研究の最優先目標と達成基準

weakly marked intrinsic非可換三次曲面のモジュライとambient AS4・4頂点potentialモジュライおよびAOU/OUのmarked AS surfaceモジュライを比較する。自然な射と忘却の定義域、一般ファイバー、W(E6)のmarking商、境界、幾何学的同型・慣性、相対基底変更・降下を達成基準とする。period指定のZ代数と無標識の圏、通常のpotentialとtwisted potentialを区別する。

## III. 現在の到達点

現行原稿と `research/surface_validation.json` に証明と検算範囲を記す。R(1,3)の全4頂点potentialの接空間から67次元成分と7次元rigidified商・有限型エタールatlas、Poisson側の一意延長・中心三次ペンシル・一般8個のnodal特異曲面、AOU marked形式近傍のW(E6) torsorと、比較仮定に依存する一般支配性、固定ambient中心三次ファイバーP1などを保持する。これらの適用仮定と原稿での証明の所在を確認してから引用する。

全大域weak moduliがWeyl商と一致すること、全intrinsic曲面が正規三次超曲面で認識されること、全境界のAS条件と全スタック降下は未解決。これらを成立済みと記さない。

## IV. 次の課題と具体的な着手

(1) AOU有限代数から相対Serre・反標準線型系を直接比較する。必要なbase-changeとheart保存を検査する。(2) Pym R(1,3) locus上でambient射のファイバー・慣性を全幾何学的点で計算する。(3) P3 directed/rolled-up箙と4周期Z代数の整合性を検証し、一般非捩れpotential部分を全AS locusと混同しない。(4) コンパクト化境界、marked忘却、モジュライの代数性を調べる。(5) AOU Theorem 9.4・Lemma 9.2とVdB Chapter 12から一般幾何学的点の反標準orbit環F=P/(G)を証明した。残る相対Serre・base-change・heartの比較と形式変形8方向の比較を検証して支配性の条件を外す。

## V. 再現

```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_surface_incidence.py
python3 computations/verify_r13_potential.py
python3 computations/verify_pencil_discriminant.py
latexmk -lualatex papers/nc-cubic-ambient-moduli.tex
python3 scripts/verify_surface_bundle.py
```

計算のPASSと原稿中の通常の証明を混同しない。検証者の独立査読・先行研究の網羅的な新規性調査は未完。
