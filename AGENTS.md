# 研究指示 — nc-cubic-ambient

2026-11-17 / ambient-v1。本リポジトリは非可換三次曲面のambient射、四周期superpotential、R(1,3)成分の正本である。最初に `00_research_plan.md`、次に `papers/nc-cubic-ambient.tex` と入力節、研究ノート、証明書を読む。**標識忘却は `uedakazushi/nc-cubic-unmark` の独立論文が正本**であり、この研究で同じ標識忘却の主論文を再作成しない。

数学的重要性、新規性、理解の深化、正確性、実現可能性を総合して方針を現行版へ更新し、履歴を蓄積しない。証明済み・仮定付き・未完成・予想・有限計算を区別。一次資料を点検し、未確認の新規性を推測で補わない。日本語LuaLaTeXで有効な主張と証明を保持する。不要な旧版・ログ・PDF・ZIP・キャッシュをGit追跡せず、計算証明書・コードと再現手順を保持する。

研究区切りにはユーザーの追加承諾なく軽量継続bundleをLibraryへ保存してよい。GitHub mainへのpush、Library保存、組版・計算検証は別々に確認。Libraryの既存ファイルを明示指示なく削除しない。PR・Actions・force pushを使わずmainへfast-forwardする。約15分を目安に研究の区切りでpushする。

検証: `python3 scripts/verify_surface_bundle.py`; `latexmk -lualatex papers/nc-cubic-ambient.tex`。全内在的対象のambient自動認識は保留したまま、次数付きJacobian型中心拡大はAff3商として証明済みで、全四頂点Zhang同型商とは区別する。次はその差・AOU相対比較・境界のH3性を優先する。
