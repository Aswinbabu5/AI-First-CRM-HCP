import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { getHcps } from '../Service/api';
import {
    setFormField,
    setHcps,
    setLoading,
    setError
} from "../Store/InteractionSlice";

function HcpSelect() {
    const dispatch = useDispatch();

    const hcps = useSelector(
        (state) => state.interaction.hcps
    );

    const selectedHcpId = useSelector(
        (state) => state.interaction.form.hcp_id
    );

    const loading = useSelector(
        (state) => state.interaction.loading
    );

    const error = useSelector(
        (state) => state.interaction.error
    );


    useEffect(() => {
        const fetchHcps = async () => {
            try {
                dispatch(setLoading(true));
                dispatch(setError(null));

                const response = await getHcps();

                dispatch(setHcps(response.data));

            } catch (error) {
                console.error(error);

                dispatch(
                    setError(
                        error.response?.data?.detail ||
                        "Failed to load HCPs"
                    )
                );

            } finally {
                dispatch(setLoading(false));
            }
        };

        fetchHcps();
    }, [dispatch]);


    const handleChange = (event) => {
        dispatch(
            setFormField({
                field: "hcp_id",
                value: Number(event.target.value)
            })
        );
    };


    if (loading) {
        return <p>Loading HCPs...</p>;
    }


    return (
        <div>
            <label htmlFor="hcp_id">
                HCP *
            </label>

            <select
                id="hcp_id"
                name="hcp_id"
                value={selectedHcpId}
                onChange={handleChange}
            >
                <option value="">
                    Select HCP
                </option>

                {hcps.map((hcp) => (
                    <option
                        key={hcp.id}
                        value={hcp.id}
                    >
                        {hcp.name}
                    </option>
                ))}
            </select>

            {error && (
                <p>
                    {error}
                </p>
            )}
        </div>
    );
}

export default HcpSelect;