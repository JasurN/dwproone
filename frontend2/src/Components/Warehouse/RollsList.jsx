import React from "react";
import {List, Datagrid, TextField, ReferenceField, NumberField, DateField} from 'react-admin';

export const RollsList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            {/*<TextField source="id"/>*/}
            <ReferenceField source="id" reference="warehouse/rolls" label="Roll ID">
                <TextField source="roll_id" />
            </ReferenceField>
            <NumberField source="initial_weight"/>
            <NumberField source="current_weight"/>
            <DateField source="income_date"/>
            <TextField source="paper.paper_type.name" label="Type"/>
            <TextField source="paper.grammage.grammage" label="Grammage"/>
            <TextField source="paper.paper_format.format" label="Format"/>
            <TextField source="paper.company.name" label="Company"/>
        </Datagrid>
    </List>
);