import { useParams,useNavigate} from 'react-router-dom';
import React from 'react';

const ProductDetails=()=>{
    const navigate=useNavigate();
    const PRODUCT_ARRAY=[
        {
            id: "p1",
            name: "Books",
            description: "This is for Books"
        },
        {
            id: "p2",
            name: "Paper",
            description: "This is for Paper"
        },
        {
            id: "p3",
            name: "Pens",
            description: "This is for Pens"
        },
        
    ]
    const params= useParams()
    const product_data=PRODUCT_ARRAY.find(
        (product)=> product.id ===params.productId
    );
    console.log(product_data);
    if(!product_data){
        return <p>No product Found</p>
    }
    // console.log(params)
    
    const backButton=()=>{
        navigate(-1)
    }
    return (
        <React.Fragment>
            <button onClick={backButton}>Back</button>
        <h1>Product Details</h1>
        <p>{product_data.name}</p>
        <p>{product_data.description}</p>

        </React.Fragment>
        )
}
export default ProductDetails;