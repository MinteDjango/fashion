import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import { Link } from "react-router-dom";

const style = {
    float:"right",
    marginRight:"10px",
}
class Header extends Component {
    render() {
        return (
            <Fragment>
        <div className="nav">
            <span className="brand">Fashion Gebeya</span>
            	<Link to="/search" style={style} >
	<svg width="18px" height="18px" viewBox="0 0 16 16" fill="#000000">
   <path fill-rule="evenodd" d="M10.442 10.442a1 1 0 0 1 1.415 0l3.85 3.85a1 1 0 0 1-1.414 1.415l-3.85-3.85a1 1 0 0 1 0-1.415z"/>
  <path fill-rule="evenodd" d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zM13 6.5a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0z"/>
</svg>

</Link>
<div className="navs">
    <Link to="/" className="navs-link">Home</Link>
    <Link to="/trendings" className="navs-link">Trendings</Link>
    <Link to="/wishlist" className="navs-link">Wishlist</Link>
    <Link to="/cart" className="navs-link">Cart</Link>
</div>
</div>
<div style={{ marginTop: "120px" }}></div>
</Fragment>
);
}
}
export default Header;