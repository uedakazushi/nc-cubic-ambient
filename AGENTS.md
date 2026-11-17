# Codex研究指示 — nc-cubic-ambient-moduli

2026-11-17。このリポジトリはambientとmarked/intrinsicモジュライ比較の正本。研究方針 `00_research_plan.md`、ノート、原稿、証明書の順に読む。全H3分類・楕円E6・非AS短報の別論文は各独立GitHub mainを正本とし、ここから内容を勝手に同期したり編集しない。

数学的重要性、新規性、理解の深化、実現可能性、正確性を重視し研究方針を柔軟に更新する。重要な変更は現行方針として理由を記し、履歴を積まない。証明済み・条件付き・未証明・予想・計算結果を区別し、既存と新規の成果を区別する。先行研究の一次資料と仮定を確認し、未確認の書誌・新規性を推測で補わない。論文は原則日本語LuaLaTeXで現在の成果と必要な証明を保持し、研究ノートは日誌にしない。旧ZIP・バックアップ・ログ・PDF・キャッシュをGitに入れず、必要なコード・入力・小証明書を保持する。

研究区切りで承諾なくLibrary保存する一般許可はあるが、このリポジトリはGitHub mainが正本であり、push成功時はLibrary保存せず、GitHub失敗時の緊急避難に限る。既存Libraryファイルは明示指示なしに削除しない。

一つのCodexが逐次研究し、約15分を目安に区切りで原稿とノートを整理してGitHub mainへ通常のfast-forwardで直接pushする。PR・Actions・force pushは使わない。更新が競合したらfetchして差分を読んで両立させる。証明の不足と検証した計算を分離し、報告で生成・検証・pushを区別する。論文は`latexmk -lualatex papers/cubic_surface_ambient_moduli.tex`、検証は`python3 scripts/verify_surface_bundle.py`。重要な方針変更後も研究を継続し、未設定のバックグラウンド作業を約束しない。
