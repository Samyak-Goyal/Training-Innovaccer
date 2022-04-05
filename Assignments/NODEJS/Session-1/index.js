const EventHelper = require("./eventhelper")

console.log("Hi")

// function math(op, v1,v2){
//     if(op ==="add")
//     return v1+v2;
//     else if(op==="sub")
//     return v1-v2;
//     else
//     return v1*v2;
// }

// let res=math("add",10,50);
// console.log(res)

// let x= require("./helper.js")

// x.printlog("Hello")

// const os = require("os")

// console.log(os.freemem());
// console.log(os.hostname());
// console.log(os.type());
// console.log(os.version());
// console.log(os.homedir());

// const dns =require("dns");

// dns.lookup('google.com',(err, address, family)=>{
//     console.log(JSON.stringify(address))
//     console.log('address: %j family: IPv%s',address,family);
// });



// const fs =require("fs");
// // console.log(__dirname)
// console.log(fs.readdirSync(__dirname))

// console.log("End of Sync call");

// fs.readdir(__dirname, function(err,list){
//     console.log(list);
// })

// console.log("End of Async call")

const eventobj = new EventHelper();

eventobj.on("LogRecorded", (result)=>{
    console.log(JSON.stringify(result))
})

eventobj.triggerEvent("Data Passed")













