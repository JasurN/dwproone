// in src/App.js
import React from 'react';

import {Admin, Resource} from 'react-admin';

import drfProvider from './dataprovider/index'
import {RollsList} from "./Components/Warehouse/RollsList";

let apiUrl = 'http://localhost:8000/api';
if (process.env.NODE_ENV === 'production') {
    apiUrl = 'https://dwproone.uz/api'
}
const dataProvider = drfProvider(apiUrl);
const App = () => (
    <Admin dataProvider={dataProvider}>
        <Resource name='warehouse/rolls/consumption' options={{label: 'Rolls Consumption'}} list={RollsList}/>
        <Resource name='warehouse/rolls/income' options={{label: 'Rolls Income'}} list={RollsList}/>
        <Resource name="warehouse/rolls/return" options={{label: 'Rolls Return From Production'}} list={RollsList}/>
        <Resource name='warehouse/rolls' options={{label: 'All Rolls'}} list={RollsList}/>
        <Resource name='warehouse/papers/formats'/>
    </Admin>
);

export default App;
