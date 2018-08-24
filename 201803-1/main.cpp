/*

如果没有跳到下一个方块上则游戏结束。

如果跳到了方块上，
但没有跳到方块的中心，则获得1分；
跳到方块中心时，

若上一次的得分为1分或这是本局游戏的第一次跳跃则此次得分为2分，
否则此次得分比上一次得分多两分（即连续跳到方块中心时，总得分将+2，+4，+6，+8...）。

if(没有跳到下一个方块上){
	游戏结束
}
else {//跳到了方块上
	if(没有跳到方块的中心){
		获得1分
	}
	else{//跳到方块中心
		if(上一次的得分为1分||这是本局游戏的第一次跳跃){//????这是本局游戏的第一次跳跃
			得分为2分
		}
		else{
			此次得分比上一次得分多两分
		}
	}
}
*/



#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    int jump;
    int score=0;
    int sum=0;
    int times=0;

    while(scanf("%d",&jump),jump){
        if(jump==1){
            score=1;

        }
        else{
            if(++times==1||score==1){
                score=2;
            }
            else{
                score+=2;
            }
        }
        sum+=score;
    }
    printf("%d",sum);
    return 0;
}
