import React, { Component } from "react";
import { render } from "react-dom";

class Item extends Component {
render() {
return (

<div className="post">
    <img src={ this.props.image } className="post-image" />
    <div className="post-footer">

        <div className="caption-cont">
            <span className="caption">{ this.props.caption }</span>
        </div>

        <div className="flex">
            <span className="price">{ this.props.price }</span>
            <a href="/" className="buy-btn">Buy</a>
        </div>

        <div>
            <div className="add-btn">Add to cart</div>
            <div className="add-btn">Add to wishlist</div>
        </div>

    </div>
</div>
);
}
}
export default Item;