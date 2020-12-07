import React, { Component, Fragment } from "react";
import { render } from "react-dom";
import axios from "axios";
import Item from "./Item";

const searchstyle = {
    width: "280px",
    margin: "auto",
    padding: "10px",
    fontFamily: "Roboto",
    border: "1px solid #efefef",
    borderRadius: "3px"
}
class Search extends Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.state = {
            data: []
        }
    }
    handleChange(e) {
        const val = e.target.value;
        if (val.length > 3) {
        axios.get(`/api/items?search=${val}`)
        .then(res => {
            const data = res.data;
            this.setState({ data });
        })
        }
    }
    render() {
        return (
            <div>
            <form>
                <input onChange={this.handleChange} type="text" name="search" placeholder="Search here..." style={searchstyle} />
            </form>
            {this.state.data.map(item => {
                return (
                <Item key={item.id} image={item.image} caption={item.caption} price={item.price}/>
                );
            })}
            </div>
      );
    }
}
export default Search;