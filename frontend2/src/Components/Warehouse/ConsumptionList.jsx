import React from "react";
import {List, Datagrid, TextField, NumberField, DateField, EditButton, Filter, TextInput, ReferenceInput, SelectInput} from 'react-admin';



export const ConsumptionList = props => (
    <List   {...props}>
        <Datagrid>
            {/*<TextField source="id"/>*/}
            <TextField source="roll_id"/>
            <NumberField source="initial_weight"/>
            <NumberField source="current_weight"/>
            <DateField source="income_date"/>
            <EditButton />
        </Datagrid>
    </List>
);