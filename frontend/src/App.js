import logo from './logo.svg';
import './App.css';
import React from "react";
import UsersList from "./components/User";
import axios from "axios";
import Menu from "./components/Menu";
import Footer from "./components/Footer";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            'users': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/user/').then(
            response => {
                const users = response.data
                this.setState(
                    {
                        'users': users
                    }
                )
            }
        ).catch(error => console.log(error))


    }

    render() {
        return (
            <div>
                <Menu></Menu>
                <UsersList users={this.state.users}/>
                <Footer></Footer>
            </div>

        )
    }
}

export default App;