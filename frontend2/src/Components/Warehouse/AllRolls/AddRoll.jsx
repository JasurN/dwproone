import React from "react";
import {
    ArrayInput,
    SimpleFormIterator,
    AutocompleteInput,
    ReferenceInput,
    Create,
    SimpleForm,
    TextInput, SelectInput, Filter,

} from 'react-admin';

export const AddRoll = (props) => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="title"/>
            <TextInput source="teaser" options={{multiLine: true}}/>
            <ArrayInput source="Format">
                <SimpleFormIterator>
                    <ReferenceInput label="Format" source="paper__paper_format__id"
                                    reference="warehouse/papers/formats">
                        <SelectInput optionText="format"/>
                    </ReferenceInput>
                </SimpleFormIterator>
            </ArrayInput>
        </SimpleForm>
    </Create>
);