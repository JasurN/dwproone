import * as React from 'react';
import PropTypes from 'prop-types';
import CheckIcon from '@material-ui/icons/Check';
import {
    useUpdateMany,
    useRefresh,
    useNotify,
    useUnselectAll,
    Button,
    CRUD_UPDATE_MANY,
} from 'react-admin';
import {allRollsConsumptionRoute} from "../../../dataprovider/apiRoutes";


const RollConsumeButton = ({resource, selectedIds, label}) => {
    const notify = useNotify();
    const unselectAll = useUnselectAll();
    const refresh = useRefresh();
    const [updateMany, {loading}] = useUpdateMany(
        allRollsConsumptionRoute,
        selectedIds,
        {views: 0},
        {
            action: CRUD_UPDATE_MANY,
            onSuccess: () => {
                notify(
                    'ra.notification.updated',
                    'info',
                    {smart_count: selectedIds.length},
                    true
                );
                unselectAll(resource);
                refresh();
            },
            onFailure: error =>
                notify(
                    typeof error === 'string'
                        ? error
                        : error.message || 'ra.notification.http_error',
                    'warning'
                ),
            undoable: true,
        }
    );

    return (
        <Button
            label={label}
            disabled={loading}
            onClick={updateMany}
        >
            <CheckIcon/>
        </Button>
    );
};

RollConsumeButton.propTypes = {
    basePath: PropTypes.string,
    label: PropTypes.string,
    resource: PropTypes.string.isRequired,
    selectedIds: PropTypes.arrayOf(PropTypes.any).isRequired,
};

export default RollConsumeButton;
