import { Link } from "react-router-dom";
const Product=()=>{
    const PRODUCT_ARRAY=[
        {
            id: "p1",
            name: "Books"
        },
        {
            id: "p2",
            name: "Paper"
        },
        {
            id: "p3",
            name: "Pens"
        },
        
    ]
    return (
        <section>
        <h1>Products Page</h1>
        <ul>
            {PRODUCT_ARRAY.map((item)=>(
                <li key={item.id}>
                    <p>{item.name}</p>
                    <Link className="btn" to={`/product/${item.id}`}>
                        Details
                    </Link>
                </li>
            ))}
            {/* <li>
                <Link to="/product/1">Books</Link>
            </li>
            <li>
                <Link to="/product/2">Papers</Link>
            </li>
            <li>
                <Link to="/product/3">Best Sellers</Link>
            </li> */}
        </ul>
        </section>
        )
}
export default Product;