### 2.2 강의내용정리  
  

```
<!-- This html is for practice ReactJS again -->

<!DOCTYPE html>
<html>
    <body>
        <div id="root"></div>
    </body>
    <script src="https://unpkg.com/react@17.0.2/umd/react.development.js"></script>
    <script src ="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
    <script>
        const root= document.getElementById("root");
        const span= React.createElement(
            "span",
            {id:"spanspan",style:{color:"red"}},
            "Hi I'm a span"
        );
        ReactDOM.render(span,root); 
</script>
    </html>
``` 
위 코드는, 단지 빨간 span을 페이지에 두는 데 코드가 많다고 느낄 수 있다.  
즉 : 
root를 생성하고, 두 가지를 import하고, root를 가져오고, element를 생성하고, element를 render해야한다.

`React.createElement("span",{span의 property}, "span의 내용")` 과 같이 작성한다. ->이때 property는 class name,id,style 가능  

\* 바닐라JS : HTML ->JS 의 순서  
\* 리액트 : JS->HTML 의 순서  
