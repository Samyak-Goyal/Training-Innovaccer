const { default: mongoose } = require("mongoose");
const UserSchema = require("../models/User")
class UserService{
    getUsers(){
        // let User = mongoose.model("User",UserSchema)
        let User= this.getModel()
        return User.find({})
    }
    async createUser(userObj){
        let User= this.getModel();
        const userInstance= new User(userObj);
        const result = await userInstance.save();
        return result;
    }



    deleteUser(id){
        let User = this.getModel();
        return User.updateOne({_id: id}, {$set: {isDel: true}})
    }

    updateUser(){
        
    }

    searchUser(){
        
    }

    getModel(){
        return mongoose.model("User", UserSchema)
    }
}

module.exports= UserService;