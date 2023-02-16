### 7.3 Movie App part One

```C
import { useState, useEffect } from "react";

function App5() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
    )
      .then((response) => response.json())
      .then((json) => {
        setMovies(json.data.movies);
        setLoading(false);
      });
  }, []);
  return <div>{loading ? <h1>Loading ... </h1> : null}</div>;
}

export default App5;
```

-> then 대신 async-await을 사용하면 아래와 같다.

```C
import { useState, useEffect } from "react";

function App5() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  const getMovies = async() => {
    const response = await fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
    );
      const json = await response.json();
        setMovies(json.data.movies);
        setLoading(false);
  };
  useEffect(() => {
    getMovies();
  }, []);
  return <div>{loading ? <h1>Loading ... </h1> : null}</div>;
}

export default App5;
```

이를 한 번 더 await으로 묶어주면,

```C
 const getMovies = async () => {
    const json = await (
      await fetch(
        `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
      )
    ).json();

    setMovies(json.data.movies);
    setLoading(false);
  };
```

와 같이 작성이 가능하다.

\*리스트에 있는 내용을 보여주기 위한 방법 : map함수 사용  
(오래된 array를 가져가서 그 array의 각각의 item을 변형시킨다. 변형돼서 return 된 것들을 새로운 array에 넣어준다.)
예시) [1,2,3,4,5,6].map(x=>x\*2) 라고 입력시 [2,4,6,8,10,12]를 return한다.

또한 map을 사용할 때마다 우리는 key를 element에 주어야 한다. (key값이 존재하지 않는 경우 설정한 Argument값을 key값으로 써주어도 된다. 단, 그 argument가 고유한 값일 경우에만 가능)
