#include <stdio.h>

int main(){
    int h,m;
    scanf("%d %d",&h,&m);
    
    if(m>=45 && m<60){
        m=m-45;
        printf("%d %d",h,m);
    }
   /* else if(m==45){ //m이 45분일 때 시만 출력
        printf("%d",h);
    }*/
    else { // m이 45분보다 작은 경우 
        if(h==0){ //0시인 경우
            h=23;
            m=(m-45)+60;
            printf("%d %d",h,m);
        }
        else{
            h=h-1;
            m=(m-45)+60;
            printf("%d %d",h,m);
        }
    }
    return 0;
}
