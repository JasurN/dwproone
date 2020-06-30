import React, {Fragment} from "react";
import {
    List, Datagrid, TextField, NumberField, DateField,
    Filter, TextInput, ReferenceInput, SelectInput,
    BulkExportButton
} from 'react-admin';
import RollConsumeButton from "./RollConsumeButton";

const RollsFilter = (props) => (
    <Filter {...props}>
        <ReferenceInput label="Format" source="paper_format"
                        reference="warehouse/papers/formats" alwaysOn>
            <SelectInput optionText="format"/>
        </ReferenceInput>
        <ReferenceInput label="Grammage" source="grammage"
                        reference="warehouse/papers/grammage" alwaysOn>
            <SelectInput optionText="grammage"/>
        </ReferenceInput>
        <ReferenceInput label="Producer" source="paper_company"
                        reference="warehouse/papers/producers" alwaysOn>
            <SelectInput optionText="name"/>
        </ReferenceInput>
    </Filter>
);

const PostBulkActionButtons = props => (
    <Fragment>
        <RollConsumeButton label="Make Consume" {...props} />
        <BulkExportButton  {...props} />
    </Fragment>
);


export const RollsList = props => (
    <List
        filters={<RollsFilter/>}
        title={"All Rolls"}
        {...props}
        bulkActionButtons={<PostBulkActionButtons/>}
        perPage={50}
    >
        <Datagrid>
            <TextField source="roll_id" label="Roll ID"/>
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