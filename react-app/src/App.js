import React from 'react';
import './App.css';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import Home from './Home/index';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/react-app"  name="Home" render={props => <Home {...props}/>} />
        <Redirect from="/" to="/react-app"/>
      </Switch>
    </BrowserRouter>
  )
}

export default App;
