# 入群小游戏解答

4.证明： $\displaystyle{  d \left( n \right)   }$ 是奇数当且仅当 $\displaystyle{  n  }$ 是平方数  
解：注意到 $\displaystyle{  n  }$ 是平方数当且仅当 $\displaystyle{  d \left( n \right) =  \sum _ { \substack {d< \sqrt {n}\\d|n}} 1 + 1 +  \sum _ { \substack {d> \sqrt {n}\\d|n}} 1 = 2   \sum _ { \substack {d< \sqrt {n}\\d|n}} 1 + 1   }$ 

5.求单摆摆动的微分方程。  
解：设 $\displaystyle{   \theta }$ 为单摆与垂直于地面的夹角。不管 $\theta >0$ 还是 $\theta <0$ ，垂直于单摆的加速度始终是 $-g\sin \theta$，即 $\displaystyle{ \ddot x=-g  \sin   \theta }$ 。设某段弧长度为 $\displaystyle{  x  }$ ，那么与对应的角度 $\displaystyle{   \theta }$ 的关系为 $\displaystyle{  x=r  \theta   }$ 。于是联立二式，得 $\displaystyle{  r  \ddot   \theta  =-g  \sin   \theta }$ ，即 $\displaystyle{   \ddot   \theta  = -  \frac{ g }{ r }   \sin   \theta }$ .

6.证明：任意维空间中，任意个质点按照牛顿力学运行，则这些质点的整体的质心随时间而匀速直线运动。  
解法一：设 $\displaystyle{   \vec {p_i}  }$ 为第 $\displaystyle{  i  }$ 个质点的坐标向量， $\displaystyle{   \vec {a_{i,j}}  }$ 为第 $\displaystyle{  j  }$ 个质点对第 $\displaystyle{  i  }$ 个质点产生的加速度向量，于是质心坐标向量为：
$$\displaystyle{ \begin{align*} & \frac{ \sum \vec{p_i} }{ m } \\=& \frac{ 1 }{ m } \sum _ {i= 1 } ^ {m} \int   \int   \sum _ b  \vec {a_{i,b}}\, \mathrm{d}t   \mathrm{d}t \\=& \frac{ 1 }{ m } \int   \int   \sum _ {i= 1 } ^ {m} \sum _ b  \vec {a_{i,b}}\, \mathrm{d}t   \mathrm{d}t \\=& \frac{ 1 }{ m } \int   \int   \vec { 0 }\, \mathrm{d}t   \mathrm{d}t \\=& \frac{ 1 }{ m } \left( \vec {C_ 1 }t+ \vec {C_ 2 } \right)  \end{align*} }$$ 
因为 $\displaystyle{   \frac{ 1 }{ m } \left( \vec {C_ 1 }t+ \vec {C_ 2 } \right)   }$ 是线性的，因此得证.  
解法二：因为这个整体不受外力.