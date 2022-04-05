import Navigation from "../Navigation/Navigation"
import "./Header.css"
const Header= (props)=>{
    return (
        <header className="header">
            <h1>Storage App</h1>
            <Navigation userLogState={props.userLoggedIn} userLogout={props.onLogoutClick}/>
        </header>
    )
}

export default Header 