import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import axios from "axios";
import Item from "./Item";

class Trendings extends Component {
    constructor(props) {
        super(props);
    this.state =  {
        data: []
    }
    }

    componentDidMount() {

        axios.get("api/items/")
            .then(res => {
                const data = res.data;
                this.setState({ data });
            })
    }
    render() {
        return (
            <div className="items">
            <div className="case-cont">
                <span className="case">Trendings</span>
            </div>
            { this.state.data.map(item => <Item image={item.image_url} caption={item.caption} price={item.price} />)}
            </div>
      );
    }
}
export default Trendings;