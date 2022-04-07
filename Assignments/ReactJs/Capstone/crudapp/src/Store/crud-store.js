import {createStore} from "redux"

const initialState={
    email:"",
    password:"",
};
const crudReducer= (state=initialState,action)=>{
    return state;
}

const crudStore= createStore(crudReducer)

export default crudStore;