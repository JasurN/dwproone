import React from "react";
import {
    Create,
    SimpleForm,
    TextInput,

} from 'react-admin';

export const AddRoll = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="title"/>
            <TextInput source="teaser" options={{multiLine: true}}/>
        </SimpleForm>
    </Create>
);