import React, {Component, Fragment} from 'react';
import {HashRouter as Router, Route, Switch} from "react-router-dom";
import {Provider as AlertProvider} from 'react-alert'
import AlertTemplate from "react-alert-template-basic";

import {Provider} from 'react-redux';
import store from "./store";

import Header from "./components/layout/Header";
import Main from "./components/leads/Main";
import Alerts from "./components/layout/Alerts";
import Login from "./components/accounts/Login";
import Register from "./components/accounts/Register";
import PrivateRoute from "./components/common/PrivateRoute";
import {loadUser} from "./actions/auth";

// ALERT OPTIONS
const alertOptions = {
    timeout: 2000,
    position: 'top center'
};

export default class App extends Component {
    componentDidMount() {
        store.dispatch(loadUser());
    }
    render() {
        return (
            <Provider store={store}>
                <AlertProvider template={AlertTemplate}
                               {...alertOptions}>
                    <Router>
                        <Fragment>
                            <Header/>
                            <Alerts/>

                                <Switch>
                                    <PrivateRoute exact path="/" component={Main}/>

                                    <Route exact path="/register" component={Register}/>
                                    <Route exact path="/login" component={Login}/>

                                </Switch>

                        </Fragment>
                    </Router>
                </AlertProvider>
            </Provider>
        )
    }
}

