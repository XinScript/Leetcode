# Leetcode

##69.Sqrt(X)
>Implement int sqrt(int x).Compute and return the square root of x.

###解题思路
其实就是整数版本的二分法求根号（其实计算机就是这么做的)  
简单来说，二分法就是令left = 0 ,right = n/2,平方根必然在0到n/2之间.  
因为求解当n>=0,令(n/2)²=n得出n=4这确保了当n>4时，n/2的平方总是大于n的.  

##100 Same Tree
>Given two binary trees, write a function to check if they are equal or not.
Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
Subscribe to see which companies asked this question

###解题思路
这题没什么好说的，果断递归  

##337.House Robber 3
>The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.  
Example 1:  
     3  
    / \  
   2   3  
    \   \  
     3   1  
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.  

Example 2:  

     3  
    / \  
   4   5  
  / \   \  
 1   3   1   
Maximum amount of money the thief can rob = 4 + 5 = 9.  


###解题思路
对于解决树相关的问题，首先想到的就是递归  
因为两个相连结点不能连续偷钱，所以对于当前结点，返回抢劫和不抢劫两个状态下的所抢到的金额。只要保证这两种状态都要是当前状态的最优即可,我认为实质上这是个动态规划问题.  
当前结点的左右子结点只要有一个已经被抢劫，当前结点就不能抢劫，只有当两个子结点都没有被抢劫的状态才能抢劫当前结点，即  
    `rob = left.unRob + right.unRob`  
    `unRob = max(left.unRob,left.rob)+max(right.unRob,right.rob)`  
    `return rob,unRob`  

因为OJ的固定返回格式，我使用了内嵌函数来完成递归，内嵌函数完成递归，最后外层函数返回  
`max(rob,unRob)`


##338.Counting Bits
>Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.
Example:
For num = 5 you should return [0,1,1,2,1,2].

###解题思路
0-7的二进制表示如下：  
0  
1  
10  
11  
100  
101  
110  
111  
好像看不出什么规律？这样来：  
000  
001  
010  
011  
100  
101  
110  
111  
***经观察规律如下：***  
当一个新的位从左边出现，它必然为1，而其他的位数，都和前2的n次方个数的位数是一样的，即  
i = 0 ,count = 0  
i = 1 ,count = result[1%1]+1  
i = 2, count = result[2%2]+1  
......  
i = 7, count = result[7%4]+1   
......  
i = i, count = result[i%2的n次方]  
n初始值为0，当且仅当i等于2的n+1次方减1的时候，n=n+1.
