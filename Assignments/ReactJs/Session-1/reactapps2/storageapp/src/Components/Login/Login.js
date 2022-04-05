import Button from "../UI/Buttons/Button"
import Card from "../UI/Card/Card"
import "./Login.css"
import { useEffect, useState } from "react"
const Login=(props)=>{
    const [userEmail, setUserEmail]=useState("");
    const [emailIsValid, setEmailIsValid]=useState();

    const [userPassword, setUserPassword]=useState("");
    const [passwordIsValid, setPasswordIsValid]=useState();   

    const [formIsValid, setFormIsValid]= useState(false);

    useEffect(()=>{
        const identifier=setTimeout(()=>{
            setFormIsValid(userEmail.includes("@") && userPassword.trim().length >6)

        },5000);
        return ()=>{
            clearTimeout(identifier)
        }
    },[userEmail,userPassword])

    const emailChangeHandler=(event)=>{
        setUserEmail(event.target.value);
        
    }
    
    const emailBlurHandler=()=>{
        setEmailIsValid(userEmail.includes("@"));
    }

    const passwordChangeHandler=(event)=>{
        setUserPassword(event.target.value);
    }

    const passwordBlurHandler=()=>{
        setPasswordIsValid(userPassword.trim().length >6);
    }

    const submitHandler=(event)=>{
        event.preventDefault();
        console.log("UserEmail:",userEmail,"UserPassword:",userPassword);
        props.onLoginClick(userEmail,userPassword)
    }
    return( 
    <Card className="login">
        <form onSubmit={submitHandler}>
            <div className={`control ${emailIsValid==false ? "invalid": ""}`}>
                <label htmlFor="email">E-Mail</label>
                <input 
                type="email" 
                name="email" 
                id="email" 
                onChange={emailChangeHandler}
                onBlur={emailBlurHandler}
                />
            </div>
            <div className={`control ${passwordIsValid==false ? "invalid": ""}`}>
                <label htmlFor="password">Password</label>
                <input type="password" 
                name="password" 
                id="password" 
                onChange={passwordChangeHandler}
                onBlur={passwordBlurHandler}
                />
            </div>
            <div className="actions">
                <Button type="submit" btnDisable={!formIsValid}>Login</Button>
            </div>
        </form>
    </Card>
    )
}

export default Login 