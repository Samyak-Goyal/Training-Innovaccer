// function myFunction() {
//     var element = document.getElementById('mydiv')
//     element.classList.toggle("divstyle")
// }


// let keyboard = document.querySelector("#keyboard")
// keyboard.addEventListener("keydown", (event) => {
//     console.log(event)
//     if (event.key == "@") {
//         alert("Key not allowed")
//         event.preventDefault()
//     }
// })

// const card = document.querySelector('aside')
// card.addEventListener('mousedown', (event) => {
//     console.log(event)
//     document.getElementById("para").style.color = "red"
//     //card.classList.toggle('large');
// })
// console.log('File loaded')

// function logkey(event){
//     screenlog.innerText=`
//     Screen X/Y : ${event.screenX} ${event.screenY}
//     Client X/Y : ${event.clientX} ${event.clientY}
//     Page X/Y : ${event.pageX} ${event.pageY}

//     `
// }
// let screenlog= document.querySelector("#screen-log")
// document.addEventListener("mousemove",logkey)

const ul = document.createElement("ul")
document.body.appendChild(ul);

const li1= document.createElement("li")
li1.innerText= "This is first line";
const li2= document.createElement("li");
li2.innerText= "This is second line";

ul.appendChild(li1);
ul.appendChild(li2);

function changecolor(event){
    console.log(event.target);
    event.target.style.color= "red";
}
ul.addEventListener("click",changecolor)
