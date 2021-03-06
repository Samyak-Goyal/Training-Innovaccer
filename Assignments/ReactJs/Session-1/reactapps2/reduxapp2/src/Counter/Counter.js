import { useDispatch, useSelector } from "react-redux";
const Counter = () =>{
    const counterValue= useSelector(state => state.counter)
    const show= useSelector(state => state.showCounter)
    const dispatch=useDispatch()
    const incrementHandler=()=>{
        dispatch({type: "increment"})
    }
    const decrementHandler=()=>{
        dispatch({type: "decrement"})
    }
    const increaseHandler=()=>{
        dispatch({type: "increase",value:10})
    }
    const toggleHandler=()=>{
        dispatch({type: "toggle"})
    }
    return (
        <main>
            <h1>Redux Counter</h1>
            {show ? <div>Counter value from store {counterValue}</div> : ""}
            <button onClick={incrementHandler}>Increment</button>
            <button onClick={decrementHandler}>decrement</button>
            <button onClick={increaseHandler}>Increase</button>
            <button onClick={toggleHandler}>Toggle</button>
        </main>
    );
};

export default Counter;