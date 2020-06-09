import React from "react";
import {List, Datagrid, TextField, NumberField, DateField, Filter, TextInput, ReferenceInput, SelectInput} from 'react-admin';

const RollsFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn />
        <ReferenceInput label="Format" source="paper__paper_format_id" reference="warehouse/papers/formats" allowEmpty>
            <SelectInput optionText="format" />
        </ReferenceInput>

    </Filter>
);

export const RollsList = props => (
    <List  filters={<RollsFilter/>} {...props}>
        <Datagrid>
            <TextField source="roll_id"/>
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