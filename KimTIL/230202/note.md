### 4.1 Memo

- html요소 안에다가 onClick과 같은 evnt를 작성하면, 이는 EventListner이고 내 커스텀 컴포넌트에 작성하면 prop일 뿐이다.  
  즉, 내가 작성한 컴포넌트에 style을 적용하고 싶다면 prop을 가져와서 적용시켜야 한다.

- React.memo() :  
  컴포넌트가 React.memo()로 감싸져있을 때, 컴포넌트를 렌더링하고 그 결과를 memo한다. 다음 렌더링이 일어날 때 prop이 같으면 memo된 내용을 재사용한다.
