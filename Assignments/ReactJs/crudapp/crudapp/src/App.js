import "bootstrap/dist/css/bootstrap.min.css"
import Login from "./Components/Login/Login";
import { Routes, Route } from 'react-router-dom'
import { useSelector } from 'react-redux'
import ListUser from "./User/ListUser";
import AddUser from "./User/AddUser";
import EditUser from "./User/EditUser";
import Header from "./Components/Header/Header";

function App() {
    const { isLogged } = useSelector((state) => state)
    const localData=localStorage.getItem("token");
    return (
        <div className="container mt-3 mb-3">
          {localData? <Header/>:""}
            {/* <h2>This is CRUD app</h2> */}
            {/* {!isLogged ? <Login /> : ""} */}
            <Routes>
                <Route path="/" element={< Login />} />
                <Route path="/list" element={< ListUser />} />
                <Route path="/create" element={<AddUser />} />
                <Route path="/edit/:id" element={<EditUser />} />
            </Routes>
        </div>
    );
}

export default App;