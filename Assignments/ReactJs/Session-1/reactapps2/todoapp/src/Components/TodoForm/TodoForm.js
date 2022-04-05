import "./TodoForm.css"
import { useState } from "react";

const TodoForm=(props)=>{
    const [title,setTitle]=useState('My title')
    const [todoDate,setTodoDate]=useState('')
    const [priority,setPriority]=useState('Low')

    // const [userInput, setInput]= useState({
    //     title: "",
    //     todoDate: "",
    //     priority: "",
    // })

    const titleChangeHandller=(event)=>{
        // setInput((prevState)=>{
        //     return{...prevState,
        //     title: event.target.value,}
        // })
        // console.log(event.target.value)
        setTitle(event.target.value)
    }
    const dateChangeHandller=(event)=>{
        // setInput({
        //     ...userInput,
        //     todoDate: event.target.value,
        // })
        setTodoDate(event.target.value)
    }
    const priorityChangeHandller=(event)=>{
        // setInput({
        //     ...userInput,
        //     priority: event.target.value,
        // })
        setPriority(event.target.value)
    }
    const submitHandller=(event)=>{
        event.preventDefault();
        const userData={
            title: title,
            date: new Date(todoDate),
            priority: priority
        }
        console.log("Title: ",title, "Date: ",todoDate,"Priority: ",priority)
        props.onSaveClick(userData)
        setPriority("")
        setTitle("")
        setTodoDate("")
    }
    return (
        <form onSubmit={submitHandller}>
            <div className="todo-controls">
                <div className="todo-control">
                    <label htmlFor="title">Title</label>
                    <input type="text" name="title" id="title" value={title} onChange={titleChangeHandller}/>
                </div>
                <div className="todo-control">
                    <label htmlFor="date">Date</label>
                    <input type="date" name="date" id="date" value={todoDate} onChange={dateChangeHandller}/>
                </div>
                <div className="todo-control">
                    <label htmlFor="priority">Priority</label>
                    <select onChange={priorityChangeHandller} value={priority} >
                        <option value="High">High</option>   
                        <option value="Medium">Medium</option>   
                        <option value="Low">Low</option>   
                    </select>    
                </div> 
            </div>
            <div className="todo-actions">
                <button type="submit" className="btn">Add Todo</button>
            </div>
        </form>
    );
};
export default TodoForm;