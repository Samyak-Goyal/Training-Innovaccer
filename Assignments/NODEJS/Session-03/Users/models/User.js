const {Schema}= require("mongoose")

const UserSchema= new Schema({
    fullname: String,
    email: String,
    gender: String,
    phone: String,
    isDel:{
        type: Boolean,
        default: false
    },
    salt: String,
    hash: String
});

module.exports = UserSchema;