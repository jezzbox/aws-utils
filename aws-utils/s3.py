import pandas as pd

def read_s3_file(bucket, client, key, aws_details,file_type="csv"):

    file_location = f"s3://{bucket}/{client}/{key}"
    storage_options={
                "key": aws_details["access_key_id"],
                "secret": aws_details["secret_access_key_id"],
                }
    if file_type == "csv":
        df = pd.read_csv(file_location,
            storage_options=storage_options,
            )
        return df

    elif file_type == "xlsx" or file_type == "xls":
        df = pd.read_excel(file_location,engine="openpyxl",
            storage_options=storage_options,
            )
        return df


def write_s3_file(bucket, client, key, aws_details):

    file_location = f"s3://{bucket}/{client}/{key}"
    storage_options={
                "key": aws_details["access_key_id"],
                "secret": aws_details["secret_access_key_id"],
                }
    
    pd.to_csv(file_location,
            index=False,
            storage_options=storage_options,
            )

    print("Success")