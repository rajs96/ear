import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { render } from 'react-dom';
import Application from './containers/app/app';

import { Provider } from 'react-redux';
import { createStore } from 'redux';
import rootReducer from './reducers';

const store = createStore(rootReducer);

const renderApplication = () => {
    render(
            <Provider store={store}>
                <Application/>
            </Provider>, document.getElementById('rootDiv'));
}

renderApplication();

Object.defineProperty(window, 'store', {
    value: store,
    writable: true
});