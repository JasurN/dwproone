import React from "react";
import {List, Datagrid, TextField, NumberField, DateField, Filter, DateInput} from 'react-admin';

const ListFilters = (props) => (
    <Filter {...props}>
        <DateInput label="From" source="date_gte" alwaysOn/>
        <DateInput label="To" source="date_lte" alwaysOn/>
    </Filter>
);
export const RollsConsumptionList = props => (
    <List   {...props}
            title={"Rolls Consumption"}
            filters={<ListFilters/>}>
        <Datagrid>
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