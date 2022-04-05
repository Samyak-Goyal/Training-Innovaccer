
// import Ti from "./Components/TodoItem/ToDoItem"
import Todos from './Components/Todos/Todos';
import NewTodo from './Components/NewTodo/NewTodo';
import { useState } from "react";
function App() {
  const INITIAL_TODO = [
    {
      id: 't1',
      title: "this is the first title",
      priority: "High",
      date: new Date(2022, 7, 11)
    },
    {
      id: 't2',
      title: "this is the second title",
      priority: "Low",
      date: new Date(2022, 8, 11)
    },
    {
      id: 't3',
      title: "this is the third title",
      priority: "Low",
      date: new Date(2022, 7, 5)
    },
    {
      id: 't4',
      title: "this is the fourth title",
      priority: "Medium",
      date: new Date(2022, 7, 15)
    },
  ]
  const [allTodos,setAllTodos]= useState(INITIAL_TODO);

  const dataSaveHandller=(usertodo)=>{

    console.log(usertodo)
    setAllTodos((prevData)=>{
      return [usertodo, ...prevData]
    })
  }

  return (
    <div>
      <NewTodo onDataReceive={dataSaveHandller}/>
      <Todos todo={allTodos} />
      
    </div>
  );
}

export default App;
