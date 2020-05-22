// in src/posts.js
import React from 'react';
import {List, Datagrid, TextField, ReferenceField} from 'react-admin';

export const PostList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <ReferenceField source="userId" reference="users">
                <TextField source="id"/>
            </ReferenceField>
            <TextField source="name"/>
            <TextField source="title"/>
            <TextField source="body"/>
        </Datagrid>
    </List>
);