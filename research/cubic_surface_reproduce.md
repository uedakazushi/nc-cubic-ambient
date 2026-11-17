# ambient射・R(1,3)成分の再現

2026-11-17 / ambient-v2。再開時は `00_research_plan.md` を先に読む。

Python3、SymPy（`requirements-surface.txt`）、日本語LuaLaTeX、LuaTeX-ja、HaranoAji、latexmkが必要。リポジトリrootで実行する。

```sh
python3 -m pip install -r requirements-surface.txt
python3 computations/verify_r13_affine_quotient.py
python3 computations/verify_directed_p3_syzygy.py
python3 computations/verify_r13_potential.py
python3 computations/verify_surface_incidence.py
python3 computations/verify_pencil_discriminant.py
python3 computations/verify_quantum_casimir_obstruction.py
python3 scripts/verify_surface_bundle.py
latexmk -lualatex papers/nc-cubic-ambient.tex
```

`verify_r13_potential.py`はR13の四flattening、全接空間、群軌道と横断方向を有理数上で検証し、`r13_potential_certificate.json` を再生成する。 `verify_surface_incidence.py` はPoisson接空間と二因子stabilizerを検査し、`surface_incidence_certificate.json` を再生成する。大量のminorの列挙は`--quick`では省略するため、完全再現には通常実行を使う。

`verify_r13_affine_quotient.py`はaffine座標変換での勾配・臨界scheme・八次判別式の共変性、Aff3 Lie安定化群rank12、8点からの勾配の積分可能性のrank8（12×9行列）をQQで検査する。一般定理の証明は論文本体を参照。

`verify_pencil_discriminant.py`は臨界値と8個のnodeの具体例、`verify_quantum_casimir_obstruction.py`は量子中心値の相違の有限証明を再現する。いずれもambientのAS正則性の全次数、標識忘却の降下、全境界の比較を有限計算だけで証明するものではない。

PDFは`build/`へ出力し、Gitはソースと小さな証明書だけを追跡する。論文・参照・コードが欠落していないことを`scripts/verify_surface_bundle.py`で点検する。現行の実行状態は`research/surface_validation.json`を読む。
