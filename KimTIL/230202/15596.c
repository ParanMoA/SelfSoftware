#include <stdio.h>

long long sum(int *a, int n){
    long long result=0;
    for(int i=0; i<n; i ++){
        result+=a[i];
    }

    return result;
}

// 정수 n개가 주어졌을 때 이 n개의 합을 구하는 함수를 작성하는 것이 문제.
