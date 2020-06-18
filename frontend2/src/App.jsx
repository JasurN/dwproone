// in src/App.js
import React from 'react';

import {Admin, Resource} from 'react-admin';
import CachedIcon from '@material-ui/icons/Cached';
import LowPriorityIcon from '@material-ui/icons/LowPriority';
import HomeWorkIcon from '@material-ui/icons/HomeWork';
import GetAppIcon from '@material-ui/icons/GetApp';
import drfProvider from './dataprovider/index'
import {RollsList} from "./components/warehouse/allRolls/RollsList";
import Dashboard from "./components/dashboard/Dashboard";
import authProviders from "./authentication/authProviders";
import {
    getAllPaperFormatRoute, getAllPaperGrammageRoute,
    getAllRollsConsumptionRoute,
    getAllRollsIncomeRoute,
    getAllRollsReturnRoute,
    getAllRollsRoute
} from "./dataprovider/apiRoutes";
import {RollsConsumptionList} from "./components/warehouse/rollsConsumption/RollsConsumptionList";
import {AddRoll} from "./components/warehouse/allRolls/AddRoll";

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
        <Resource name={getAllRollsRoute}
                  options={{label: 'All Rolls'}}
                  list={RollsList}
                  create={AddRoll}
                  icon={HomeWorkIcon}/>
        <Resource name={getAllRollsConsumptionRoute}
                  options={{label: 'Rolls Consumption'}}
                  list={RollsConsumptionList}
                  icon={LowPriorityIcon}/>
        <Resource name={getAllRollsIncomeRoute}
                  options={{label: 'Rolls Income'}}
                  list={RollsList}
                  icon={GetAppIcon}/>
        <Resource name={getAllRollsReturnRoute}
                  options={{label: 'Rolls Return'}}
                  list={RollsList}
                  icon={CachedIcon}/>
        <Resource name={getAllPaperFormatRoute}/>
        <Resource name={getAllPaperGrammageRoute}/>
    </Admin>
);
export default App;
