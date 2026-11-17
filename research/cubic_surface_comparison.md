# 現行研究ノート：R13・内在的三次曲面・Weyl商

2026-11-17 / surface-v6。最初に `00_research_plan.md` を読む。証明本文は `papers/nc-cubic-ambient-moduli.tex` とその唯一のinput。以下は作業日誌ではない。

## マーキング忘却・構造対象の現在の結論

- 現行のweakly marked公理は(A,O)をとり、H=S^{-1}[2]のt-exact性、AZ豊富性、三次曲面Hilbert値に加えてGabriel–Krullのrank-one torsion-free性（qO非零単純・A1からOへのHom消滅）とexceptionality（End(O)=k、Ext^{>0}(O,O)=0）を**独立に要求**する。ambientや一次生成性を仮定しない。圏論的な主定理と十分な証明は `papers/sections/marking_forgetful.tex` にある。

- 忘却は `M_AOU^adm -> C^w -> C^u`。固定圏上では許容九対象threadの選択群oid、許容構造対象の選択群oidとなる。圏の同定を忘れるとexact自己同値2-groupでのhomotopy quotientとなる。従ってPicard商と呼ぶときはraw 2-groupとスカラーrigidification、同型類集合の商を区別する。

- 可換滑らかな三次曲面Xでは許容構造対象EはL⊗I_Zとなるが、RRからχ(E,E)=1−2length(Z)、exceptionalityからZ=∅。従って線束Lだけが許容。自然同型で割ったexact自己同値はPic(X)⋊Aut(X)、pointedの選択商はBAut(X)。AOUのrelation algebra End(⊕E_i)は全対象の共通tensorで変わらず、relation GIT点をさらにPicで重複して割らない。

- 特殊ファイバーと同定したArtin flat Abel変形（相対Serre・perfect base change・heart保存を要求）では各線束と標準helixの持上げはExt¹=Ext²=0により一意。各標準markingの形式chartは同じweak deformationへ対応し、有限W(E6) torsorになる。全境界・非可換一般点における大域商は未証明。

- **新しい障害の公式**：u=(ξ,π)∈H¹(T_X)⊕H⁰(∧²T_X)、線束LのMorita re-markingによる一次変化は規約を除き (ξ,π)↦(ξ+δ_π(L),π)、δ_π(L)=H¹(π^sharp)c₁(L)。構造対象Lが圏の変形へ持ち上がることと、(-)⊗Lが**同じ変形**の自己同値へ持ち上がることは異なる。後者にはδ=0が必要。

- πの零因子Cが滑らかな反標準楕円曲線なら0→Ω¹_X→T_X→T_X|_C→0で、長完全列の階数は7−h⁰(T_X|_C)=3+r（r=0または1）。非空開でr=1：X={x³+y³+z³+txy+t³=0}, C={t=0}ではCの平面移動t=εzがJacobian環のxyzに対応しKS非零。従って一般にrank4。**反標準線束の方向はδの核**：局所Cの方程式s_iに対してπ^sharp(dlog s_i)は正則で、そのČech差がδ_π(O(C))。従ってroot格子Q=K^⊥へのδの制限は全Picに対して同じ階数、一般には4。非常に一般の(X,π)の整数kernelは下記の新定理で計算済み。高次障害は未計算。

- Pic(X) rank7、Q(E6) rank6、Pic/(Q+ZK)=Z/3、Pic/ZK≅Q^∨。AOU/OUのaffine Weyl translation QとPic全体を同一視しない。新しい計算スクリプト `computations/verify_marking_lattice.py` は72根、27線、E6判別式3とsmoothな例のJacobian確認をQQ上で行う。一次障害と相対降下の数学的証明はコードではなく本文にある。

## 非可換一次変形の整数Picard核と構造対象軌道

主論文の定理 `thm:very-general-picard-kernel` と系 `cor:first-order-pointings` に完全証明。

(1) marked滑らかな三次曲面の既約moduli M^m は六本の順序付き斜交直線のblow-down（一般位置のP²六点）で記述される。W(E6)がmarkingを変える。一次資料：Dolgachev–van Geemen–Kondō, *A complex ball uniformization of the moduli space of cubic surfaces via periods of K3 surfaces*, J. reine angew. Math. 588 (2005), 99–148, §§2.5–2.6, DOI 10.1515/crll.2005.2005.588.99（著者公開PDF https://sites.lsa.umich.edu/idolga/wp-content/uploads/sites/1334/2024/08/cubic05.pdf、p.105を確認）。一次re-markingにはToda, *Deformations and Fourier–Mukai transforms*, JDG 81 (2009) 197–224, arXiv:math/0502571を参照。

(2) smooth anticanonical Poisson sectionを持つmarked pair空間P^mも既約。標準Picard格子Λ=I_{1,6}を自明化してΛ_C=C K⊕Q_C、Q=K^⊥=E6。全パラメータのδ核の共通部分NはW(E6)安定でCKを含む。WのQ_C上の反射表現は既約：任意の非零W安定部分が根と非直交なvを含むなら反射差から根を含み、その軌道72根はQ_Cを張る。非空開でδのrank4なのでNはΛ_C全体でなく、N=CK。ゆえに各D∈Λ\ZKの零点条件δ(D)=0はP^m上の真の閉部分集合。可算個のDを除外すると、非常に一般の(X,π)についてker(δ:Pic(X)→H¹(T_X))=ZK。これは単一のZariski開上での一様な主張ではない。

(3) Aut(X)=1の非常に一般な滑らかな可換三次曲面Xと、Poisson成分πが上の条件に入る許容一次Abel変形A_εを考える。特別fiberのexact自己同値はBondal–Orlovによりtensor L（非零shiftなし）。これが固定A_εへ持ち上がればδ_π(L)=0、従ってL∈ZK。逆に相対反Serre H=S_ε^{-1}[2]はt-exactで、特殊fiber上でtensor(-K)なので全ZKを実現する。各LはExt¹=Ext²=0により唯一の許容構造対象L_εへ持ち上がるため、同じA_ε上のpointingをexact自己同値で割った同型類集合はPic/ZK≅Q(E6)^∨≅Z^6。**同型類の集合の結果であり、2-groupの慣性や大域stackの無限成分を主張しない**。当然、全非可換変形や高次形式変形へ無条件には拡張しない。

(4) 計算資産：`computations/verify_marking_lattice.py` はE6の72根・27直線・判別式3・rank4 witnessに加え、単純反射による一根のWeyl軌道72個とQ上のrank6張りをQQで検算する。既約性は本文の反射による通常証明から従い、コードだけが証明ではない。

### 主要な未解決箇所
1. NC fiberで許容構造対象のexact自己同値軌道・安定化群・相対慣性を具体化すること。
2. AOUの標準helix（relation stack）と数値markingの大域的降下を証明すること。
3. 非常に一般の一次変形の整数核は決定済み。特殊fiberの整数核、形式高次の障害、invertible bimoduleによる実際の作用を求めること。
4. AOU GIT compactificationのどこでheart/構造対象の許容性が保たれるか判定すること。

## 保持するambient比較と表示の区別

四窓のR_i∈Gr(6,V_i⊗V_(i+1))をGL4^4で割るのは、AS Z代数に任意の4周期τを指定した問題。非捩れpotentialはFrobenius適合周期の部分。可換Cの周期にdiag(2,1,1,1)を合成するとR0=R1=R2=Λ²V、R3=(1⊗σ^-1)Λ²V。最高syzygyがΛ⁴VなのにR3が交代でないため非捩れpotentialは存在しない。twisted potentialを使うときはNakayamaとtraceの同値関係も必要。

GL4^4の各矢空間スカラーは射影potentialに自明に作用する。67次元parameter componentのraw stack次元は3、四つのGmをrigidifyした商は7。pointed圏、裸のAbel圏、graded代数、周期構造付きZ代数を区別する。

## 三次元quadratic AS正則とdirected/rolled-up箙の比較（既知結果）

この話題は本稿の四頂点・四次superpotentialの場合と同一視しない。非可換 P^2 のdirected Beilinson箙には三頂点・六矢があり、関係は rank 3 の R⊂V0⊗V1 (dim V0=dim V1=3)。三本の矢 V2:2→0 を加えたrolled-up箙の**三次の通常の巡回potential**は w∈V0⊗V1⊗V2。flattening w:V2*→V0⊗V1 が単射である開集合 U 上で、w↦im(w)=R は GL(V2) の主束である。よって族・自己同型込みで
[U/(GL(V0)×GL(V1)×GL(V2))] ≃ [Gr(3,V0⊗V1)/(GL(V0)×GL(V1))]
が成り立つ。逆は V2=R* として恒等テンソル w=Σ r_i⊗c_i。rolled-up potential W=Σ r_i c_i の ∂_(c_i)W=r_i、他の微分はRから一意に定まる。これはAOU *Compact moduli of noncommutative projective planes*, arXiv:1411.7770, (7.27)–(7.28) で**既に証明されている**。同Theorem 1.1(2) は半安定GIT商 M_quad≅M_rel≅P(6,9,12) も述べる。full-rankでないpotentialも含むraw affine quotient stack全体は同値でなく、上記は開埋込みである。projectivized potentialにGL(V2)で作用させる場合は残存G_m慣性を処理する。

以前の「任意の3周期同型を固定した三頂点relationの表示はordinary potentialにならない」という反例は、**指定した周期との両立**を問題にしたものであり、directed箙のRだけを保持し新矢をR*として追加するこの同値の反例ではない。3次元AS正則幾何対象に制限するにはBP/VdBのgeometric quadruple条件（任意の非零縮約がrank≥2など）を対応する双方へ課す。単なるfull flattening rank 3からAS正則性を導かない。一般の長さ6,9等のpotentialまで自由に許すと、ここでの同値から外れる。

## P3のdirected 4頂点relationsとrolled-up 4頂点potential（現行結論）

P2のAOU arXiv:1411.7770 §7 の「directed R⊂V0⊗V1 → 新矢R* → 三次potential」に対応するP3の構成は、4頂点directed Beilinson箙0→1→2→3に4次元矢空間V0,V1,V2、各rank6の二次関係R0⊂V0⊗V1、R1⊂V1⊗V2を取ることから始まる。必要な新矢はR_iの双対ではなく三次syzygy
K=(R0⊗V2)∩(V0⊗R1)⊂V0⊗V1⊗V2
の双対V3=K*。標準AS4ではdimK=4。二つの縮約K⊗V2*→R0、V0*⊗K→R1が全射である層上ではcanonical coevaluation w=Σkα cα∈V0⊗V1⊗V2⊗K*から全4関係を二階縮約で回復する。非射影化wとGL4^4の商は、このdirected二関係のAS/Koszul非退化層とGL4^3の商に群oid同値。射影potentialとPGL商では両側のGm慣性を一致させること。現在のdirected/rolled-upの構成と同型範囲は本ノートに保持し、可換点の確認は computations/verify_directed_p3_syzygy.py に保持する。元分類側の単独のTeX節名を再開前提とはしない。

一般の二関係の交わりKは0になり得る。従って全Gr(6,16)^2にpotential表示はなく、K=4の局所閉rank層と縮約rank6・Koszul-AS正則性が必要。境界K>4ではGr(4,K)のsyzygy選択による別のコンパクト化が自然。四次potentialは通常の一階Jacobian（DWZ）ではなく二階微分。BSWのsigned CY superpotentialはW=w-cw+c²w-c³w（反巡回）、通常の符号なしcyclic wordに落とすと零になる。符号なしの巡回和は二階関係空間だけなら同じものを与えるので、potentialの意味を指定する。

可換P3についてQQ上で直接検算：K=Λ³k⁴、dimK=4、四つの二階flatteningの関係rankはすべて6。計算スクリプト computations/verify_directed_p3_syzygy.py。既存のpotential側の可換点projective接空間dim90から、V3のPGL4-torsor（dim15）を除くとdirected側の接空間dim75。directedのPGL4^3軌道のdim30を除けばHH²(P3)=45と一致。これはAS locusの大域成分計算ではない。

## 中心三次ペンシルの一般ファイバー（現行論文定理 thm:pencil-critical）

最高三次f3が滑らかなときJacobian環J_f=k[x,y,z]/(f_x,f_y,f_z)は長さ8の完全交差。臨界値多項式Δ_f(λ)=det(λI+m_f)はモニック8次で、X_λ=V_+(F+λt³)が特異であることとΔ_f(λ)=0は同値。一般には8根が相異なり、それぞれ1個のA1特異点を持つ。独立計算例はf=x³-3x+y³-12y+z³-48zで臨界値が±110,±114,±142,±146。検算コードcomputations/verify_pencil_discriminant.pyを収録する。無限遠点は三重平面で、量子中心三次商の特異値同定は未解決。

中心一次拡大B_fのt≠0のpoint moduleは、t m_n=m_{n+1}と基底を選ぶと、x,y,zが次数によらないスカラーa,b,cで作用する。二次関係の可換化は∂f=0と等価だから、parameter schemeはSpec J_f。一般の8点は可換ペンシルの8個のnodalな特異メンバーと一対一対応する（主論文prop:critical-point-modules）。LBS Math. Z. 222 (1996), Propositions 4.3.7, 4.3.9 は一般の中心一次拡大に8個の追加point moduleが存在することを既に証明している。本稿の追加はその臨界点表示とnodalメンバーへの対応であり、新規性の網羅的確認は未完。

## 量子中心三次値が可換臨界値と一致しない厳密計算例

体QQ、中心一次元tを持つ次数付き代数Bを、[t,x]=[t,y]=[t,z]=0 および
[y,z]=3x²−3t²、[z,x]=3y²−12t²、[x,y]=3z²−48t²
で定める。これはf=x³+y³+z³−3x−12y−48zに対応するJacobian型中心一次拡大。

t=1 の局所化では、次の次数≤3の元を考える。

Ω = x³+y³+z³ − 3(xyz+xzy+yxz+yzx+zxy+zyx) −3x−12y−48z。

computations/verify_quantum_casimir_obstruction.py は、3つの交換子[Ω,x],[Ω,y],[Ω,z]が3つの二次関係の両側倍からなる線型空間に含まれることをQQ上で検証する。長さ≤4の全121語、関係両側倍102本、そのrank86を使う。各交換子は長さ≤4なので、この有限な理想所属確認は中心性の厳密な証明書となる。次数をtで斉次化すれば中心三次元Ω_B∈B_3を得る。

8個のt≠0 point moduleは(x,y,z)=(±1,±2,±4)で、その上でΩはf−18xyzに等しい。古典臨界値の集合は {±110,±114,±142,±146}、量子中心値の集合は {±2,±30,±254,±290} である。対応する点を固定すると、f=aΩ+bを全点で満たすa,b∈QQ（さらにはC）は存在しない。計算では8×3行列(Ω(p),1,f(p))のrank3も検証した。

この計算は「point moduleの集合が同じなら中心三次ペンシルのパラメータ値も同じ」という誤った推論の障害になる。量子中心値の根が実際にB/(Ω_B−c t³)のhomological singularityやモジュライ境界を検出するかは未証明。新規性の網羅的調査、一般のfへの公式の拡張も未実施。

## 明示族と計算

F=a(x³+y³+z³)+bxyz+t(x²+c2y²+c3z²)+t²(d1x+d2y+d3z)。w=Alt(txyz)-3(1-c+c²-c³)(t sym F)。全二階微分で[t,x]=[t,y]=[t,z]=0、[y,z]=sym F_x等を得る。t³はwに寄与しない。

witness=(3,5,2,3,1,2,4)。二flatteningのrank6条件の微分Tは200×256、rank188。軌道Oは256×64、rank61。7slice+軌道S7は256×71、rank68。TS7=0はQQ上の恒等式。従ってprojective tangent=67、orbit=60、商=7。最大小行列式はJSONに行・列とともに保存。19独立係数で微分関係の恒等式も検算した。

sourceの全次数AS性はMori–Smith、PBW、中心一次拡大とKoszul complexの証明を使う。有限階数だけからAS性を結論していない。接空間同型からH×N→O13は適切に縮小してétale surjective。これが実際の有限型DM開部分。全成分境界のAS性やgeneric stabilizerの位数は未計算。

二因子stabilizerのrank30証明書により一般点でLie=0。四窓のArtin変形のNakayamaの射影像は消え、scalar c_iだけが残る。∏c_i=1なのでtrace rescalingで消せる。従ってこの一般点では任意周期の関係式の形式変形も非捩れpotentialになる。大域反例とは矛盾しない。

## 内在的定義と認識の境界

H=S^-1[2]は両方向でheartを保つことを要求する。smooth proper enhancement、noetherian heart、Hom有限性、族での平坦性・相対Serre・底変更を指定する。Γ_acの積はH^m(g)∘f。AZの有限性・ample性により(A,O,H)を回復する。

Hilbert級数(1-t³)/(1-t)^4だけから次数一生成・二次包絡AS4・正則三次核はまだ導いていない。一般反例を発見したという意味でもない。超曲面認識部分ではI3=1、I4=4から左右の生成像が一致してnormalityを得る。これによりambient射は自然かつ底変更に両立する。

## 形式Weyl商と未解決の大域商

一般可換Xの標準markingはW(E6)-torsor。Ext¹(E,E)=Ext²(E,E)=0とLowenにより九対象は各Artin変形へ一意に持ち上がる。DDLの幾何的helix比較で全関係式変形とAbel変形が一致。Oも唯一、逆Serre=helix九移動、ample列によるheartの検出でt-exactness、Artin帰納で反標準ample性とHilbert値が保たれる。HH²=8、HH¹=HH³=0。よって全usual-markingの形式chartのWeyl商はweak形式変形と一致する。

大域化には、全対象へのmarkingの局所存在、K0数値markingによる例外列の一意性、全同型・降下の比較が必要。形式chartの同型や8次元の一致だけで大域商やdegree=|W(E6)|を結論しない。Oを固定するだけでaffine Weyl由来の全追加同一視が自動的に消えるとはしていない。

## AOUからambientへの有限計算

AOU有限代数はrank45、globaldim≤2の三block quiver。Θ=RHom_(Λe)(Λ,Λe)はinverse Serre bimodule。P0=e_(0,0)ΛとしてK_m=RHom(P0,P0⊗Θ^⊗m[2m])、m=0..4を計算する。可換点近傍ではrank1,4,10,19,31、V=H0K1、R2=ker(V²→H0K2)でGrassmannianへの候補射がある。

AOU§9の(9.44),(9.55)–(9.57)でP0はOへ送られる。Lemma9.2でHは反標準shift。Fの深さ3とArtin–Zhangのsection環の完全列により、一般幾何学的点のinverse Serre orbit環はF=P/(G)と同型（現行論文命題prop:aou-orbit-generic）。ただしこれは導来同値であり、heartの一致や相対底変更は含まない。Sklyanin頂部でGが中心、σ(t)=t、σ(x_i)=x_i+c_i t、Hessian比較でc_i=0なので一般にはGも中心。

可換点でtruncation≤3の微分はinjective。関係module J/(VJ+JV)の次数>3が特殊化で零なのでArtin Nakayamaにより消える。このため低次数の自明化は全環・Abel圏の自明化となる。相対Serreと中心三次商の比較仮定が一般位置で成立する場合、AOUの8方向と射影基底15方向を加えた像は23次元。一般の固定ambient中心三次はP1なのでambient像≥22、既知R13族dim22より等号。四頂点rigidified商では8→7、一般fiber1、像の閉包codim0。

ここでは8座標→7座標の展開済み有理式を出していない。finite Serre algorithmの実装、generic degree、Weyl同定、境界での正則性は次の課題。全weakly marked stackの有限型性や全認識定理とも区別する。

## 一次資料（必要箇所）

- Bocklandt–Schedler–Wemyss, arXiv:0802.0162v3, §1、Theorems6.2/6.8。signed/twisted potentialとKoszul解消の関係。
- Mori–Smith, arXiv:1502.07403v2, Theorem4.2(1)。smoothなcommutative最高三次ならA_(f,λ)は3CY。
- Pym, arXiv:1403.6444, §2, §3.4。規格化graded CY変形とR13の中心拡大表示。全任意周期stackの分類ではない。
- AOU, arXiv:2404.00175v1, Introduction(2), §5.4, §9, Lemma9.2, Theorem9.4。(9.44)等のOとmarked threadの対応を確認。
- VdB, arXiv:math/9809116, Chapter12、Remark12.0.5。反標準モデルとblow-upそのものを区別。
- Le Bruyn–Smith–Van den Bergh, Math.Z.222(1996),171–212。一般中心一次拡大のAS性と7次元族。
- Etingof–Ginzburg, arXiv:0709.3593v4, Proposition7.3.1(ii)、Theorem3.3.2、§9。PBWと中心元。
- Lowen, arXiv:math/0407019, TheoremA。対象の持上げのExt²障害／Ext¹自由度。
- De Deken–Lowen, JNCG5(2011),477–505, DOI10.4171/JNCG/83, Theorems4.5/5.13/5.15、Definition5.12。公式PDF https://ems.press/content/serial-article-files/30497 。forward Ext消滅、flat性、Z生成helixを確認して使用。
- Okawa–Ueda, arXiv:2508.04986v1, Definition1.1, Theorem6.4。marked AS面と楕円データの双有理比較。weak Weyl quotient定理ではない。
- Okawa–Ueda, OWR44/2024, pp2557–2558, DOI10.4171/OWR/2024/44。affine Weyl、K0一意性、pure helixに関するConjectures1–3。

新規性の網羅的確認・外部査読は未実施。再現手順と今回の検証範囲は隣のreproduce/validationを読む。
