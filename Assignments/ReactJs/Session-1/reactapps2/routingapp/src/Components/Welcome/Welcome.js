import { Fragment } from "react";
import { Link, Outlet, Route, Routes, useNavigate } from "react-router-dom";

const Welcome=()=>{
    const navigate =useNavigate();
    const buttonClickHandler=()=>{
        navigate("/product")
    }
    return (
        <Fragment>
            <h1>This is the Welcome Page</h1>
            <Link to="guest-user">Guest User </Link>
            <Link to="parent-user">Parent User</Link>
            <Outlet/>
            {/* <Routes>
                <Route path="guest-user" element={<p>This is for Guest user</p>} />
            </Routes> */}
            <button onClick={buttonClickHandler}>Visit Products</button>
            <button>
                <Link to="/product">Product</Link>
            </button>
        </Fragment>
    )
}
export default Welcome;