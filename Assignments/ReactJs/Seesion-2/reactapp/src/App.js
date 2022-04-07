import logo from './logo.svg';
import './App.css';
import Welcome from './Welcome/Welcome';
import Async from './AsyncFiles/Async';

function App() {
  return (
    <div >
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <Welcome />
        <Async/>
    </div>
  );
}

export default App;
