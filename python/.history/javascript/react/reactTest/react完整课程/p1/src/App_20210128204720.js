import './App.css';
import Navbar from './Navbar'

function App() {
  return (
    <div className="App">
      <div className="content">
        <h1> { title }</h1>
        <p>Liked { likes } times </p>
        <p> { 10 }</p>
        <p> { "hello ninjas" }</p>
        <p> { [1, 2, 3, 4, 5] }</p>
        <p> { Math.random() * 10 }</p>
        <a href={baidu}>baidu site</a>
      </div>
    </div>
  );
}

export default App;
