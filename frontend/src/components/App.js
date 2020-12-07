import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import { BrowserRouter, Route } from "react-router-dom";
import Home from "./Home";
import Header from "./Header";
import Trendings from "./Trendings";
import Wishlist from "./Wishlist";
import Cart from "./Cart";
import Search from "./Search";

class App extends Component {
    render() {
        return (
            <Fragment>
            <Header />
            <Route exact path="/" component={Home} />
            <Route exact path="/trendings" component={Trendings} />
            <Route exact path="/wishlist" component={Wishlist} />
            <Route exact path="/cart" component={Cart} />
            <Route exact path="/search" component={Search} />
            </Fragment>
    );
    }
}
export default App;
const container = document.getElementById("app");
render(<BrowserRouter><App/></BrowserRouter>, container);