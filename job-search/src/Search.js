import React, { Component } from "react";
import "./Search.css";

class Search extends Component {
    state = {
        searchValue: "",
        meals: []
    };

    handleOnChange = event => {
        this.setState({ searchValue: event.target.value });
    };

    handleSearch = () => {
        this.makeApiCall(this.state.searchValue);
    };

    makeApiCall = searchInput => {
        var searchUrl = `https://www.themealdb.com/api/json/v1/1/search.php?s=${searchInput}`;
        fetch(searchUrl)
            .then(response => {
                return response.json();
            })
            .then(jsonData => {
                this.setState({ meals: jsonData.meals });
            });
    };

    render() {
        return (
            <div>
                <h1>Job Search Engine</h1>
                <input name="text" type="text" onChange={event => this.handleOnChange(event)} value={this.state.searchValue} placeholder="Search" />
                <button onClick={this.handleSearch}>Search Lucene</button>
                <button onClick={this.handleSearch}>Search MapReduce</button>
                {this.state.meals ? (
                    <div id="results-container">
                        {this.state.meals.map((meal, index) => (
                            <div class="single-result" key={index}>
                                <h2>{meal.strMeal}</h2>
                                <img src={meal.strMealThumb} alt="meal-thumbnail" />
                            </div>
                        ))}
                    </div>
                ) : (
                    <p>Try searching for a meal</p>
                )}
            </div>
        );
    }
}
export default Search;