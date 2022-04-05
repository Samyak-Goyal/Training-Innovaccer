import {useState} from "react"
import "./TodoItem.css";
import TodoDate from "../TodoDate/TodoDate";
import Card from "../UI/Card/Card";
function ToDoItem(props) {
    const [usertitle, setTitle]= useState(props.title)
    const [textChange, setTextChanged]= useState(false);
    const [newPriority, setPriority]= useState(props.priority);
    const title = props.title
    const priority = props.priority
    const todoDate = props.date

    const buttonClickHandler= ()=>{
        setTitle("This is the new text")
        setTextChanged(true);
        setPriority("High")
        console.log(usertitle);
    }
    return (
        <Card className="todo-item">
           <TodoDate userDate={todoDate}/>
            <div className="todo-description">
                <h2 className={
                `${textChange== true ? "color2" : "color1"}`}
                >{usertitle}</h2>
                <div className="todo-priority">{newPriority}</div>
                <button onClick={buttonClickHandler}>Change Text </button>
            </div>
        </Card>
    )
}

export default ToDoItem