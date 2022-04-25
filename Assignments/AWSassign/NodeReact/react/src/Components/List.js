import UserService from '../Services/UserService'
import { Fragment, useEffect } from 'react'

const List = () => {
    let data;
    const getBuckets = () => {
        UserService.listBuckets().then((res) => {
            data = res.data
            console.log(typeof(res.data))
            console.log(data)
        })
    }
    useEffect(() => {
        getBuckets()
    })
    return (
        <Fragment>
            {data.map((user) =>(
                {user}
            ))}
        </Fragment>
    )
}

export default List
