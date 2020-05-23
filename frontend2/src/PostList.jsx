// in src/posts.js
import React from 'react';
import {
    List,
    Datagrid,
    TextField,
    ReferenceField,
    EditButton,
    Filter,
    TextInput,
    ReferenceInput,
    SelectInput,
    SimpleList
} from 'react-admin';
import {useMediaQuery} from '@material-ui/core';

const PostFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="q" alwaysOn/>
        <ReferenceInput label="User" source="userId" reference="users" alwaysOn>
            <SelectInput optionText="name"/>
        </ReferenceInput>
        <ReferenceInput label="Id" source="id" reference="users" alwaysOn>
            <SelectInput optionText="id"/>
        </ReferenceInput>
    </Filter>
);

export const PostList = props => {
    const isSmall = useMediaQuery(theme => theme.breakpoints.down('sm'));
    return (
        <List {...props}>
            {isSmall ? (
                <SimpleList
                    primaryText={record => record.title}
                    secondaryText={record => `${record.views} views`}
                    tertiaryText={record => new Date(record.published_at).toLocaleDateString()}
                />
            ) : (
                <Datagrid>
                    <TextField source="id" />
                    <ReferenceField label="User" source="userId" reference="users">
                        <TextField source="name" />
                    </ReferenceField>
                    <TextField source="title" />
                    <TextField source="body" />
                    <EditButton />
                </Datagrid>
            )}
        </List>
    );
};