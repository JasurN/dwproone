import React from "react";
import {List, Datagrid, TextField, NumberField, DateField, EditButton, Filter, TextInput, ReferenceInput, SelectInput} from 'react-admin';

const RollsFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn />
        {/*<ReferenceInput label="User" source="userId" reference="users" allowEmpty>*/}
        {/*    <SelectInput optionText="name" />*/}
        {/*</ReferenceInput>*/}
    </Filter>
);

export const RollsList = props => (
    <List  filters={<RollsFilter/>} {...props}>
        <Datagrid>
            {/*<TextField source="id"/>*/}
            <TextField source="roll_id"/>
            <NumberField source="initial_weight"/>
            <NumberField source="current_weight"/>
            <DateField source="income_date"/>
            <TextField source="paper.paper_type.name" label="Type"/>
            <TextField source="paper.grammage.grammage" label="Grammage"/>
            <TextField source="paper.paper_format.format" label="Format"/>
            <TextField source="paper.company.name" label="Company"/>
            <EditButton />
        </Datagrid>
    </List>
);