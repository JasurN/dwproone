import React from "react";
import {List, Datagrid, TextField, NumberField, DateField, EditButton} from 'react-admin';


export const RollsConsumptionList = props => (
    <List   {...props}>
        <Datagrid>
            {/*<TextField source="id"/>*/}
            <TextField source="roll.roll_id" label="Roll ID"/>
            <NumberField source="amount"/>
            <DateField source="date"/>
            <TextField source="roll.paper.paper_type.name" label="Type"/>
            <TextField source="roll.paper.grammage.grammage" label="Grammage"/>
            <TextField source="roll.paper.paper_format.format" label="Format"/>
            <TextField source="roll.paper.company.name" label="Company"/>
        </Datagrid>
    </List>
);