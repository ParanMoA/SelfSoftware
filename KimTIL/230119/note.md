### 2.4 Recap: 강의내용정리  

요약:  
이전까지는 React JS와 ReactDOM을 먼저 import하고 이후 createElement를 통해 코드를 작성하였다. props 안에서 event listener을 등록할 수 있다. 예를들어 on으로 시작하는 event를 작성하면 React JS가 event listener임을 알아챈다. 

### 2.5 JSX 강의내용정리  
목표:  
createElement를 대체하고자 한다(by JSX:JavaScript를 확장한 문법, HTML과 유사).  
예시:  
```
const h3= React.createElement(
            "h3",
            {
                onMouseEnter: () => console.log("mouse enter!"),
            },
            "Hi I'm a span"
            );
```
를 JSX로 바꾸면 다음과 같다.  
```
const Title = ( <h3 id="title onMouseEnter={() => console.log("mouse enter")}> Hello I'm a Title</h3>);
```  
