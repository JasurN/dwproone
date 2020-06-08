import React from "react";
import {List, Datagrid, TextField,  ReferenceField, NumberField, DateField} from 'react-admin';

export const RollsList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="id"/>
            <ReferenceField source="id" reference="rolls"><TextField source="roll_id"/></ReferenceField>
            <NumberField source="initial_weight"/>
            <NumberField source="current_weight"/>
            <DateField source="income_date"/>
            <TextField source="paper.paper_type.name"/>
        </Datagrid>
    </List>
);