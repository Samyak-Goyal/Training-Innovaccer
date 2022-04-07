const Login=()=>{
    return(
        <div className="container mt-3">
            <form>
                <div className="mb-3 mt-3">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        name="email"
                        id="email"
                        className="form-control"
                        placeholder="Enter Email"
                        />

                </div>
                <div className="mb-3 mt-3">
                    <label htmlFor="password">Password</label>
                    <input
                        type="password"
                        name="password"
                        id="password"
                        className="form-control"
                        placeholder="Enter password"
                        />

                </div>
                <button type="submit" className="btn btn-primary">Login</button>
            </form>
        </div>
    )
}
export default Login;