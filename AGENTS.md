# Codex研究指示 — nc-cubic-ambient-moduli

2026-11-17 / surface-v6。このリポジトリは二段階の標識忘却（AOU helix→構造対象→圏）の研究正本。研究方針 `00_research_plan.md`、ノート、原稿、証明書の順に読む。全H3分類・楕円E6・非AS短報の別論文は各独立GitHub mainを正本とし、ここから内容を勝手に同期したり編集しない。

数学的重要性、新規性、理解の深化、実現可能性、正確性を重視し研究方針を柔軟に更新する。重要な変更は現行方針として理由を記し、履歴を積まない。証明済み・条件付き・未証明・予想・計算結果を区別し、既存と新規の成果を区別する。先行研究の一次資料と仮定を確認し、未確認の書誌・新規性を推測で補わない。論文は原則日本語LuaLaTeXで現在の成果と必要な証明を保持し、研究ノートは日誌にしない。旧ZIP・バックアップ・ログ・PDF・キャッシュをGitに入れず、必要なコード・入力・小証明書を保持する。

研究区切りには追加承諾なく現行軽量bundleをLibraryに保存してよい。GitHub mainはTeX研究の正本。GitHub push・Library保存・組版・計算実行は別々に確認する。既存Libraryファイルは明示指示なしに削除しない。

ambient認識の自動性は保留し、rank-one torsion-free exceptional構造対象の指定、AOU 標識付きとweakの有限Weyl商、weak→無標識のexact自己同値群oid、Picardの整数核・高次障害と慣性を最優先にする。非常に一般の一次変形の整数核ZKとPic/ZKのpointing分類は現行論文に証明したので、次は特別なNC fiberと高次形式変形を優先する。一つのCodexが逐次研究し、約15分を目安に区切りで原稿とノートを整理してGitHub mainへ通常のfast-forwardで直接pushする。PR・Actions・force pushは使わない。更新が競合したらfetchして差分を読んで両立させる。証明の不足と検証した計算を分離し、報告で生成・検証・pushを区別する。論文は`latexmk -lualatex papers/nc-cubic-ambient-moduli.tex`、検証は`python3 scripts/verify_surface_bundle.py`。重要な方針変更後も研究を継続し、未設定のバックグラウンド作業を約束しない。

日本語の用語は「標識」「標識付き」「弱標識付き」「無標識」「標識忘却」「標識変更」を使用する。引用文献の英語題名、ソースのファイル名、LaTeXの参照ラベルは変更しない。公表論文は標識忘却とambient射に分割する方針を検討し、現段階では分割を実施せず有効な証明を保持する。
