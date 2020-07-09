import React from "react";
import {
    ReferenceInput,
    Create,
    SimpleForm,
    SelectInput,
    NumberInput
} from 'react-admin';

export const AddRoll = (props) => (
    <Create {...props} title={"Add Roll Income"}>
        <SimpleForm>
            <ReferenceInput label="Producer" source="producer_id"
                            reference="warehouse/papers/producers">
                <SelectInput optionText="name"/>
            </ReferenceInput>
            <ReferenceInput label="Format" source="format_id"
                            reference="warehouse/papers/formats">
                <SelectInput optionText="format"/>
            </ReferenceInput>
            <ReferenceInput label="Grammage" source="grammage_id"
                            reference="warehouse/papers/grammage">
                <SelectInput optionText="grammage"/>
            </ReferenceInput>
            <ReferenceInput label="Paper Type" source="paper_type_id"
                            reference="warehouse/papers/types">
                <SelectInput optionText="name"/>
            </ReferenceInput>
            <NumberInput
                min='0' max='3000'
                source="initial_weight"/>
        </SimpleForm>
    </Create>
);