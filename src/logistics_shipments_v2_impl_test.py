import resources


async def retrieve_list_of_shipments(**kwargs) -> dict[str, object]:
    df = resources.dfs["logistics_shipments"]
    df = df[df['client_id'] == kwargs['client_id']]
    #    df = df[df['client_id'] == 'C0001']
    result = df[['shipment_number', 'parcel_no', 'shipment_destination_address', 'parcel_weight', 'status',
                 'client_id']].to_dict(
        orient='records')
    return {"result_data": result}
