import "./Button.css"
const Button= (props)=>{
    return (
        <button
         type={props.type || "button"}
         onClick={props.onBtnClick}
         disabled={props.btnDisable}
         className={`button ${props.btnClassName}`}
        >
            {props.children}
        </button>
    )
}

export default Button;