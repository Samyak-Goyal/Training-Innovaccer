const express = require("express");
const { default: helmet } = require("helmet");
const { default: mongoose } = require("mongoose");
const app= express()
const {Schema}= require("mongoose");


app.use("/assets", express.static("./assets"))
// app.use("/user", require("./router/users"));
// app.use("/provider", require("./router/provider"))
app.use("/admin", require("./router/admin"))
// app.use(cors())
// app.use(helmet())

app.get("/",(req,res)=>{
    res.send("Welcome to Home Page")
})
app.get("/dashboard",(req,res)=>{
    res.send("Welcome to Dashboard")
})

app.get("/employee",(req,res)=>{
    const EmployeeSchema = new Schema({
        firstname: String,
        lastname: String,
        email: String,
        isMarried: Boolean
    });

    let Employee = mongoose.model("employee", EmployeeSchema);
    const AllEmployees2= Employee.find({}).then((err,emp)=>{
        console.log(emp)
        console.log(err)
    });
    res.send("Employee list")
})


app.listen(3000, (obj)=>{
    mongoose.connect("mongodb://localhost/innovaccerdb").then(()=>{
        console.log("Database connected Successfully")
    }).catch((err)=>{
        console.log("Database connection denied")
        console.log(JSON.stringify(err))
    })
    console.log("Connected....")
})