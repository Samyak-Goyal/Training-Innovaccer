import Card from "../UI/Card/Card";
import Ti from "../TodoItem/ToDoItem"
import "./Todos.css"
const Todos = (props)=>{
    const ALL_TODOS=props.todo;
    return(
        <Card className="todos">
            {ALL_TODOS.map((todo)=>(
                <Ti 
                title={todo.title} 
                priority={todo.priority} 
                date={todo.date} 
                key={todo.id}
                />
            ))}  
//                   {/* <Ti title= {INITIAL_TODO[0].title} priority={INITIAL_TODO[0].priority} date={INITIAL_TODO[0].date} />
//       <Ti title={INITIAL_TODO[1].title} priority={INITIAL_TODO[1].priority} date={INITIAL_TODO[1].date} />
//       <Ti title={INITIAL_TODO[2].title} priority={INITIAL_TODO[2].priority} date={INITIAL_TODO[2].date} />
//       <Ti title={INITIAL_TODO[3].title} priority={INITIAL_TODO[3].priority} date={INITIAL_TODO[3].date} />
//  */}

    </Card>
       
    )
}

export default Todos