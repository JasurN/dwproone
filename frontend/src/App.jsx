// in src/App.js
import React from 'react';

import {Admin, Resource} from 'react-admin';
import CachedIcon from '@material-ui/icons/Cached';
import LowPriorityIcon from '@material-ui/icons/LowPriority';
import HomeWorkIcon from '@material-ui/icons/HomeWork';
import GetAppIcon from '@material-ui/icons/GetApp';
// import drfProvider from './dataprovider/index'
import drfProvider, { tokenAuthProvider, fetchJsonWithAuthToken } from 'ra-data-django-rest-framework';

import {RollsList} from "./components/warehouse/allRolls/RollsList";
import Dashboard from "./components/dashboard/Dashboard";
import {
    devApiRoute,
    allPaperFormatRoute, allPaperGrammageRoute, allPaperProducersRoute,
    allRollsConsumptionRoute,
    allRollsIncomeRoute,
    allRollsReturnRoute,
    allRollsRoute, productionApiRoute, allPaperTypesRoute
} from "./dataprovider/apiRoutes";
import {RollsConsumptionList} from "./components/warehouse/rollsConsumption/RollsConsumptionList";
import {AddRoll} from "./components/warehouse/allRolls/AddRoll";


let apiUrl = devApiRoute;
if (process.env.NODE_ENV === 'production') {
    apiUrl = productionApiRoute;
}
let Options = {
    obtainAuthTokenUrl: `${apiUrl}/api-token-auth/`
};
const authProvider = tokenAuthProvider(Options);

const dataProvider = drfProvider(`${apiUrl}/api`, fetchJsonWithAuthToken);
const App = () => (
    <Admin dataProvider={dataProvider}
           dashboard={Dashboard}
           authProvider={authProvider}
           title="My Custom Admin">
        <Resource name={allRollsRoute}
                  options={{label: 'All Rolls'}}
                  list={RollsList}
                  create={AddRoll}
                  icon={HomeWorkIcon}/>
        <Resource name={allRollsConsumptionRoute}
                  options={{label: 'Rolls Consumption'}}
                  list={RollsConsumptionList}
                  icon={LowPriorityIcon}/>
        <Resource name={allRollsIncomeRoute}
                  options={{label: 'Rolls Income'}}
                  list={RollsConsumptionList}
                  icon={GetAppIcon}/>
        <Resource name={allRollsReturnRoute}
                  options={{label: 'Rolls Return'}}
                  list={RollsList}
                  icon={CachedIcon}/>
        <Resource name={allPaperFormatRoute}/>
        <Resource name={allPaperGrammageRoute}/>
        <Resource name={allPaperProducersRoute}/>
        <Resource name={allPaperTypesRoute}/>
    </Admin>
);
export default App;
