/*

���û��������һ������������Ϸ������

��������˷����ϣ�
��û��������������ģ�����1�֣�
������������ʱ��

����һ�εĵ÷�Ϊ1�ֻ����Ǳ�����Ϸ�ĵ�һ����Ծ��˴ε÷�Ϊ2�֣�
����˴ε÷ֱ���һ�ε÷ֶ����֣�������������������ʱ���ܵ÷ֽ�+2��+4��+6��+8...����

if(û��������һ��������){
	��Ϸ����
}
else {//�����˷�����
	if(û���������������){
		���1��
	}
	else{//������������
		if(��һ�εĵ÷�Ϊ1��||���Ǳ�����Ϸ�ĵ�һ����Ծ){//????���Ǳ�����Ϸ�ĵ�һ����Ծ
			�÷�Ϊ2��
		}
		else{
			�˴ε÷ֱ���һ�ε÷ֶ�����
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