import React from "react";
import {
    ReferenceInput,
    Create,
    SimpleForm,
    SelectInput,
} from 'react-admin';

export const AddRoll = (props) => (
    <Create {...props} title={"Add Roll Income"}>
        <SimpleForm>
            <ReferenceInput label="Format" source="paper__paper_format__id"
                            reference="warehouse/papers/formats">
                <SelectInput optionText="format"/>
            </ReferenceInput>
            <ReferenceInput label="Grammage" source="paper__grammage__id"
                            reference="warehouse/papers/grammage">
                <SelectInput optionText="grammage"/>
            </ReferenceInput>
        </SimpleForm>
    </Create>
);