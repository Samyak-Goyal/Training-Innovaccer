import axios from 'axios'

const USER_BASE_URL = 'http://localhost:3001/s3'

const headers={
    'Content-Type': 'application/json'
}

class UserService{
    listBuckets(){
        return axios.get(USER_BASE_URL + '/list')
    }
}

export default new UserService()