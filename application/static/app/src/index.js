import React from 'react';
import ReactDOM from 'react-dom';
import { MyForm } from './components/MyForm.jsx'
import { WindowAbout } from './components/WindowAbout.jsx'
import * as serviceWorker from './serviceWorker'

ReactDOM.render(<div><WindowAbout /></div>, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
