import './App.css';
import { Route, Routes } from 'react-router-dom'
import List from './Components/List'

function App() {
    return (
        <div className="App">
            hi
            <Routes>
                <Route path="/list" element={<List />} />
            </Routes>
        </div>
    );
}

export default App;
