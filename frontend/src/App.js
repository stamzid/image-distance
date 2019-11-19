import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';

const server_url = 'http://localhost:8000/upload';

class App extends Component {
    constructor() {
        super();
        this.state = {
            selectedFile: null,
        };
    };

    onChangeHandler = event => {
        this.setState({
            selectedFile: event.target.files[0],
        });
    }

    onClickHandler = () => {
        const data = new FormData();
        data.append('csv_file', this.state.selectedFile);
        axios.post(server_url, data, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(res => {
            console.log(res.statusText);
            this.setState({
                selectedFile: null,
            });
        });
        window.location.reload();
    }

    render () {
        return (
            <div className="App">
                <header className="App-header">
                    <img src={logo} className="App-logo" alt="logo" />
                    <input type="file" name="csv_file" onChange={this.onChangeHandler}/>
                    <button className="App-button" onClick={this.onClickHandler}>Upload</button>
                </header>

            </div>
        );
    }
}

export default App;
