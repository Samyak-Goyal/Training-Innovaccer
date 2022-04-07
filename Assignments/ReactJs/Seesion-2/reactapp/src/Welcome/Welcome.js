import { Fragment, useState } from "react";

function Welcome(){
    const [changeText,setChangeText]=useState(false);
    const changeTextHandler=()=>{
        setChangeText(true);
    }
    return(
        <Fragment>
            <h2>Hello World</h2>
            {!changeText ? <p>Good Morning</p>: <p>Good Night</p>}
            <button onClick={changeTextHandler}>Change Text</button>
        </Fragment>
    )
}
export default Welcome;