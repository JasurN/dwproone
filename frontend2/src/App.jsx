// in src/App.js
import React from 'react';

import {Admin, Resource} from 'react-admin';
import CachedIcon from '@material-ui/icons/Cached';
import LowPriorityIcon from '@material-ui/icons/LowPriority';
import HomeWorkIcon from '@material-ui/icons/HomeWork';
import GetAppIcon from '@material-ui/icons/GetApp';
import drfProvider from './dataprovider/index'
import {RollsList} from "./Components/Warehouse/RollsList";
import Dashboard from "./Components/Dashboard/Dashboard";
import authProviders from "./Authentication/authProviders";

let apiUrl = 'http://localhost:8000/api';
if (process.env.NODE_ENV === 'production') {
    apiUrl = 'https://dwproone.uz/api'
}
const dataProvider = drfProvider(apiUrl);
const App = () => (
    <Admin dataProvider={dataProvider}
           dashboard={Dashboard}
           authProvider={authProviders}
           title="My Custom Admin">
        <Resource name='warehouse/rolls/all' options={{label: 'All Rolls'}}
                  list={RollsList} icon={HomeWorkIcon}/>
        <Resource name='warehouse/rolls/consumption' options={{label: 'Rolls Consumption'}}
                  list={RollsList} icon={LowPriorityIcon} exact={true}/>
        <Resource name='warehouse/rolls/income' options={{label: 'Rolls Income'}}
                  list={RollsList} icon={GetAppIcon}/>
        <Resource name="warehouse/rolls/return" options={{label: 'Rolls Return From Production'}}
                  list={RollsList} icon={CachedIcon}/>
        <Resource name='warehouse/papers/formats'/>
        <Resource name='warehouse/papers/grammage'/>
    </Admin>
);
export default App;
