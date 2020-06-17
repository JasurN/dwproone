import React from "react";
import {
    List, Datagrid, TextField, NumberField, DateField,
    EditButton, Filter, TextInput, ReferenceInput, SelectInput
} from 'react-admin';
import RollConsumeButton from "./RollConsumeButton";

const RollsFilter = (props) => (
    <Filter {...props}>
        <TextInput label="Search" source="search" alwaysOn/>
        <ReferenceInput label="Format" source="paper__paper_format__id" reference="warehouse/papers/formats" allowEmpty>
            <SelectInput optionText="format"/>
        </ReferenceInput>

        <ReferenceInput label="Grammage" source="paper__grammage__id" reference="warehouse/papers/grammage" allowEmpty>
            <SelectInput optionText="grammage"/>
        </ReferenceInput>
    </Filter>
);

export const RollsList = props => (
    <List
        filters={<RollsFilter/>}
        title={"All Rolls"}
        {...props}
        bulkActionButtons={<RollConsumeButton/>}
    >
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
            <EditButton/>
        </Datagrid>
    </List>
);