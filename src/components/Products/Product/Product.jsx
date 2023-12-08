import React from "react";
import { useNavigate } from "react-router-dom";
import "./Product.scss";

const Product = ({ data, id }) => {
  const navigate = useNavigate();
  return (
    <div className="product-card" onClick={() => navigate("/product/" + id)}>
      <div className="thumbnail">
        <img
          src={
            process.env.REACT_APP_STRIPE_APP_DEV_URL +
            data.Img.data[0].attributes.url
            // data[0]?.attributes?.Img?.data[0]?.attributes?.url
          }
        />
      </div>
      <div className="prod-details">
        <span className="name">{data.title}</span>
        <span className="price">&#8377;{data.price}</span>
      </div>
    </div>
  );
};

// const Product = ({ data, id }) => {
//   const navigate = useNavigate();

//   // Check if data is defined before accessing its properties
//   if (!data || !data.image || !data.image.data || !data.image.data[0]) {
//     // Return some placeholder or loading content
//     return <div>Loading...</div>;
//   }

//   // Now, you can safely access the properties
//   const imageUrl =
//     process.env.REACT_APP_STRIPE_APP_DEV_URL +
//     data.image.data[0].attributes.url;

//   return (
//     <div className="product-card" onClick={() => navigate("/product/" + id)}>
//       <div className="thumbnail">
//         <img src={imageUrl} alt="Product Thumbnail" />
//       </div>
//       <div className="prod-details">
//         <span className="name">{data.title}</span>
//         <span className="price">&#8377;{data.price}</span>
//       </div>
//     </div>
//   );
// };

export default Product;
