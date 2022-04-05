// // console.log('hello')
// function Circle(radius){
//     let color= "red";
//     this.radius=radius;
//     let defaultLocation= {x:20};
//     this.draw=function(){
//         console.log("Draw Function")
//     }
//     Object.defineProperty(this, "defaultLocation",{
//         get: function(){
//             console.log(defaultLocation);
//         },
//         set: function(num){
//             defaultLocation=num
//         }
//     });
// }

// const c1=new Circle(25);
// // console.log(defaultLocation)

// c1.defaultLocation;
// c1.defaultLocation={x:30}
// c1.defaultLocation;



// function Clock(t){
//     this.t =t
//     let startTime 
//     let endTime 
//     let running= false;
//     let duration=0
    
//     this.start = function(){
//         if(running){
//             throw "Error the clock is already running"
//         }
//         else{
//             running=true;
//             startTime=new Date().getTime()/1000
//             console.log("Started at: "+ startTime+" sec")
//         }
//     }
//     this.stop = function(){
//         if(running){
//             running= false;
//             endTime=new Date().getTime()/1000
//             console.log("Stopped at: "+ endTime+" sec")

//         }
//         else{
//             throw "Error the clock is not running";
//             console.log()
//         }
//     }

//     this.reset= function(){
//         startTime=0;
//         endTime=0;
//         duration=NaN;
//         running=false;
//     }

//     Object.defineProperty(this,"duration",{
//         get: function(){
//             let t=endTime-startTime;
//             if(t<0){
//                 t+=60
//             }
//             console.log("The Duration was: " +t+" sec")
//         }
//     })
// }

// const c1= new Clock(3);
// console.log(d.getSeconds())



// class Rectangle{
//     constructor(width, height, color){
//         console.log("Class created")
//         this.width=width;
//         this.height=height;
//         this.color=color;
//     }
//     getArea(){
//         return this.height* this.width;
//     }
//     get area(){
//         return this.height* this.width;
//     }
//     set area(h){
//         this.height=h;
//     }
//     static hello(x){
//         console.log("this is hello")
//         console.log(x.width);
//     }
// }


// let rec1= new Rectangle(20,6,"red")

// console.log(rec1)
// console.log(rec1.area)
// console.log(rec1.area=10)
// console.log(rec1.area)

// Rectangle.hello(rec1)


// class Person{
//     constructor(name,age){
//         this.name= name;
//         this.age=age;
//     }
//     describe(){
//         console.log(`My name is ${this.name} and I am ${this.age}years old`)
//     }
// }

const posts=[
    {title: "post 1", body:"this is body 1"},
    {title: "post 2", body:"this is body 2"},

]

function getPost(){
    setTimeout(()=>{
        let output="";
        posts.forEach((post)=>{
            output+=   `<li>${post.title}</li>`
        });
        document.body.innerHTML=output;
    },1000)
}

function createPost(post,callback){
    setTimeout(()=>{
        posts.push(post);
    },2000)
}

function createPost2(post){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            posts.push(post);
            const error=false;
            if(!error){
                resolve();
            }
            else{
                reject("Something went wrong")
            }
        },2000)
    })
}

createPost2({title: "post 3", body:"this is body 3"}).then(getPost).catch((err)=>console.error(err));


const prom= fetch("https://jsonplaceholder.typicode.com/users").then((value)=>value.json()).then((res)=>console.log(res));

async function init(){
    let res= await fetch("https://jsonplaceholder.typicode.com/posts");
    let data= await res.json();
    console.log(data)
}
init()






