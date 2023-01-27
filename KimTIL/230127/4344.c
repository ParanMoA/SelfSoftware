#include <stdio.h>

int main(){
    int c,n,s; // c:테스트케이스 수, n:학생 수, s:점수 
    scanf("%d",&c); //테스트케이스 수 입력 받기
    
    
    for(int i=0; i<c; i++){
        int arr[1001]={0};
        int sum=0, avg=0, count=0;
        
        scanf("%d",&n); // 학생 수 입력받기 

        for(int j=0; j<n; j++){
            
            scanf("%d",&s); //점수 입력받기
            arr[n]=s;  
            // printf("배열:%d\n",arr[n]); //배열로 점수를 받음
            sum+=arr[n];

        }
        avg= sum/n;
        printf("avg:%d\n",avg);

    }
        

    // for(int i=0; i<c; i++){
    //     for(int j=0; j<n; j++){
    //         if(s>avg){
    //             count ++;
    //             printf("%d\n %d\n",s,count);
    //         }
    //     }
    //     // printf("%.3f",count/n *100);
    // }
    
}
// 점수의 평균을 구하고, 그 평균을 넘는 점수의 비율을 구한다.
// 예를들어, 첫 번째 줄에서 50,50,70,80,100 이므로 이들의 평균은 70이 된다.
// 평균70을 넘는 점수는 80,100 두 가지이므로 2/5 *100=40%비율이다.
