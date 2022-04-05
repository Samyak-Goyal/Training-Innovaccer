const express = require("express")
const mongoose = require("mongoose")
const UserSchema = require("../models/User");
const router= express.Router();
const UserService= require("../services/UserService");

const userServiceObj= new UserService();

router.get("/", (req,res)=>{
    res.send("Index user Listing");
})

router.get("/list", async(req,res)=>{
    let users= await userServiceObj.getUsers();
    res.send(users);
})



router.get("/add", (req,res)=>{
    res.send("User add page");
})
router.get("/create", async(req,res)=>{
    let result = await userServiceObj.createUser({
        fullname: "Saksham Goyal",
        email: "Saksham@google.com",
        gender: "Male",
        phone: "976899",
        salt: "",
        hash: ""
    })
    res.send(result)
})


router.delete("/:id", async (req,res)=>{
    const result= await userServiceObj.deleteUser(req.params.id)
    res.send(result);
})

module.exports = router;