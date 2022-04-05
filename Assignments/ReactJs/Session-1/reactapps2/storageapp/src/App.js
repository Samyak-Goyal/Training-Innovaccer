import Login from './Components/Login/Login';
import Home from "./Components/Home/Home"
import Header from './Components/Header/Header';
import {useState, useEffect,Fragment} from "react"
import {Routes,Route} from "react-router-dom"
import Users from './Components/User/User';
import Profile from './Components/User/Profile';

function App() {
  const [isLoggedIn , setIsLoggedIn]=useState(false);


  useEffect(()=>{
    const localStorageData= localStorage.getItem("userLoginState");
    if(localStorageData=== "LOGGED_IN"){
      setIsLoggedIn(true);
    }
  
  },[])

  const loginHandler=(email,password)=>{
    console.log(email,password)
    setIsLoggedIn(true);
    localStorage.setItem('userLoginState','LOGGED_IN')
  }
  const logoutHandler=()=>{
    setIsLoggedIn(false);
    localStorage.removeItem('userLoginState')
  }
  return (
    <Fragment>
      <Header userLoggedIn={isLoggedIn} onLogoutClick={logoutHandler} />
      <main>
        {!isLoggedIn ? <Login onLoginClick={loginHandler}/> :
         <Home onLogoutClick={logoutHandler}/> }
        
      </main>

      {/* <Routes>
          <Route path="/users" element={<Users/>}/>
          <Route path="/profile" element={<Profile/>}/>
        </Routes>  */}
    </Fragment>  
  );
}

export default App;
