//1 const q=document.getElementById("container");
// console.log(q)


//2 const q=document.querySelector("#container")
// console.log(q)

//3 const q=document.querySelectorAll(".second")
// console.log(q)
// var q = document.querySelectorAll('.second')
// for (let i = 0; i < q.length; i++) {
//     console.log(q[i].innerText)
// }

//4 var q4 = document.querySelector('ol >li.third')
// console.log(q4.innerHTML)

// var q5 = document.getElementById("container")
// q5.insertAdjacentHTML("beforeBegin","hello")


// var q6 = document.querySelector('.footer')
// q6.classList.add("main")

// var q7 = document.querySelector('.main')
// q7.classList.remove("main")


// var q8 = document.createElement('li')
// q8.innerText = "four"

// const ul = document.querySelector('ul')
// ul.appendChild(q8)


//11 var temp = document.querySelectorAll("ol li");
// for(var i = 0; i < temp.length; i++){
// temp[i].style.backgroundColor = "green";
// } 

// const q12 = document.querySelectorAll(".footer")
// for (const q of q12) {
//     q.parentNode.removeChild(q)
// }

// var x = document.querySelector(".footer");
// x.remove("footer");
// console.log(x); 




// Assign 2


// const arr = [
//     {
//     firstName: 'Samyak',
//     lastName: 'Goyal',
//     age: 22,
//     likes: ['b','d','c']
//     },
//     {
//     firstName: 'Jeff',
//     lastName: 'Bezos',
//     age: 46,
//     likes: ['a','c']
//     },
//     {
//     firstName: 'Elon',
//     lastName: 'Musk',
//     age: 43,
//     likes: ['e','a']
//     },
//     {
//     firstName: 'Sundar',
//     lastName: ' Pichai',
//     age: 35,
//     likes: ['c','d']
//     },
//     {
//     firstName: 'Satya',
//     lastName: 'Nadella',
//     age: 53,
//     likes: ['a','b']
//     }] 


//     function myfunc(name, property) {
//         for (let i = 0; i < arr.length; i++) {
            
//             if (arr[i].firstName == name) {
//                 return arr[i].hasOwnProperty(property)
//             }
//         }
//     }
    
//     console.log(myfunc("Samyak", "age"))





// Assign 3


// let exp=document.getElementById("one");
// exp.addEventListener("click",(event)=>{
//     console.log(event);
//     var table= document.getElementById("tbl");
//     var row=table.insertrow()
// })

// function myFunc() {
//     var table = document.getElementById("tbl");
//     var row = table.insertRow(0);
//     var nc1 = row.insertCell(0);
//     var nc2 = row.insertCell(1);

//     nc1.innerHTML = "* ";
//     nc2.innerHTML = "* ";
// }


// const btn = document.querySelector("button");

// btn.addEventListener('click',()=>{
// var table = document.querySelector("table");
// var row = table.insertRow(0);
// var cell1 = row.insertCell(0);
// var cell2 = row.insertCell(1);
// cell1.innerHTML = "*";
// cell2.innerHTML = "*";
// }) 



const employee=[
    {
        id: 1,
        name: "E1",
        age: 20,
        designation: "Developper",
        salary: 40000,
        phone: 234358239
    },
    {
        id: 2,
        name: "E2",
        age: 25,
        designation: "Accountant",
        salary: 50000,
        phone: 234358239
    },{
        id: 3,
        name: "E3",
        age: 40,
        designation: "Developper",
        salary: 80000,
        phone: 234358239
    },{
        id: 4,
        name: "E4",
        age: 24,
        designation: "Developper",
        salary: 80000,
        phone: 234358239
    },{
        id: 5,
        name: "E5",
        age: 20,
        designation: "Accountant",
        salary: 30000,
        phone: 234358239
    },
]

const result= employee.filter((e)=>{

    // if(e.designation=="Developper"){
    //     console.log(e)
    // }

    // if(e.age < 30){
    //     console.log(e)
    // }

    // if(e.age < 30 && e.salary >70000)
    // console.log(e)

    // if(e.designation=="Accountant" && e.salary <40000)
    // console.log(e)
})