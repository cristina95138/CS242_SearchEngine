import React, { Component } from "react";
import "./Search.css";

class Search extends Component {
    state = {
        searchValue: "",
        data: []
    };

    handleOnChange = event => {
        this.setState({ searchValue: event.target.value });
    };

    handleSearch = () => {
        this.makeApiCall();
    };

    makeApiCall = () => {
        fetch("./output.json")
            .then(response => {
                return response.json();
            })
            .then(jsonData => {
                this.setState({ data: jsonData });
                alert(this.state.data[0]);
            });
    };

    render() {
        return (
            <div>
                <h1>Job Search Engine</h1>
                <input name="text" type="text" onChange={event => this.handleOnChange(event)} value={this.state.searchValue} placeholder="Search" />
                <button onClick={this.handleSearch}>Search Lucene</button>
                <button onClick={this.handleSearch}>Search Hadoop MapReduce</button>
                {this.state.data ? (
                    <div id="results-container">
                        {this.state.data.map((result, index) => (
                            <div class="single-result" key={index}>
                                <h2>{result.job_title}</h2>
                            </div>
                        ))}
                    </div>
                ) : (
                    <p>Try searching</p>
                )}
            </div>
        );
    }
}
export default Search;