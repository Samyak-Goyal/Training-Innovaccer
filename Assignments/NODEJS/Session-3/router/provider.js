const express= require("express")
const router= express.Router()

router.get("/home",(req,res)=>{
    res.send("Welcome to the Provider home page")
})

router.get("/info/:id/:name",(req,res)=>{
    res.send("Welcome to the info page for id "+req.params.id + " and name "+req.params.name)
})

module.exports= router;