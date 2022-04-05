import logo from './logo.svg';
import './App.css';
import Welcome from './Components/Welcome/Welcome';
import Product from './Components/Products/Product';
import {Routes,Route, Navigate} from 'react-router-dom'
import Header from './Components/MainHeader/Header';
import {Fragment} from 'react';
import ProductDetails from './Components/Products/ProductDetails';
import NotFound from './Components/NotFound';

function App() {
  return (
    <Fragment>
      <Header/>
    <main>
      <Routes>
        <Route path="/" element={<Navigate to="/welcome"/>}/>
        <Route path='/welcome/*' element={<Welcome/>} >
          <Route path="guest-user" element={<p>This is for Guest user</p>} 
          />
          <Route path="parent-user" element={<p>This is for Parent user</p>} 
          />
        </Route>
        <Route path='/product' element={<Product/>} />
        <Route path='/product/:productId' element={<ProductDetails/>} />
        <Route path="*" element={<NotFound/>}/>
      </Routes>
    </main>
    </Fragment>
  );
}

export default App;
