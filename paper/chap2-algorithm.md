# 模型和相关算法

## 模型及相关概念

### 相关概念

* 有效粉丝

## 社交网络影响力计算模型

在社交网络影响力最大化的问题中，将社交网络建模为一个有向图 G=(V, E)，其中 V 代表用户节点的集合， E 属于 V*V 是用户之间关注关系的有向边集合。

* EF(i) 表示用户 i 的有效粉丝数。
* inf(u(i), d) 表示用户 i 在主题 d 下的影响力，根据所有 inf 值，找出影响力前 K 大的用户集合。

例如，独立级联模型和线性阀值模型，给出有向图 G=(v, E) 和参数 K，影响力最大化问题是在节点集合 V 中挑选 K 个节点，组成 S 集合，使得影响力传播 theta(S) 最大。

## InDegree

最简单的入度算法，在一个给定的社交网络中，拥有的粉丝数量越多，则影响力越大。

## TunkRank

Daniel Tunkelang 在 2009 年提出了基于 PageRank 算法的 TunkRank 算法进行用户影响力度量，该方法根据粉丝的影响力作为个体影响力衡量的主要因素。

## NLP

Natural Language Processing（自然语言处理）把自然语言处理为机器易于处理的形式。

分词 -> 去停用词 -> 去标点符号 -> 去无用词

## LDA Gibbs Sampling

LDA（Latent Dirichlet Allocation） 是用来分类文本内容的算法。

## Topic-sensitive Rank




## Twitter Rank （基于 Topic-sensitive Rank）

Jianshu Weng， Ee-Peng 在2010年提出了 TwitterRank ， 该算法在 PageRank 算法上进行拓展，基于用户间主题相似性及用户声明的好友关系网络，通过用户所发布的微博数量及其粉丝接受信息的多少来决定衡量用户的影响力。

## TAP

Topical Affinity Propagation（话题亲和力传播模型）

## 本文算法

基于用户有效粉丝数和特定主题计算社交网络中用户的影响力。
