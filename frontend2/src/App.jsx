// in src/App.js
import React from 'react';

import {Admin, Resource, ListGuesser} from 'react-admin';
// import {UserList} from "./users";
// import jsonServerProvider from 'ra-data-json-server';
// import {PostList} from "./PostList";
// import {PostEdit} from "./PostEdit";
// import {PostCreate} from "./PostCreate";
// import PostIcon from '@material-ui/icons/Book';
// import UserIcon from '@material-ui/icons/Group';
// import Dashboard from "./Dashboard";
// import authProvider from './authProvider';
import drfProvider from './dataprovider/index'

const dataProvider = drfProvider('https://localhost/api');
const App = () => (
   <Admin dataProvider={dataProvider}>
      <Resource name="warehouse/rolls" list={ListGuesser} />
   </Admin>
);

export default App;
